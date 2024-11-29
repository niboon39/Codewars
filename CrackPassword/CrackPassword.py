import numpy as np
from numba import cuda
import time
import socket
import time  # Importing time for adding delay

# GPU Kernel Function
@cuda.jit
def gpu_brute_force(char_set_len, password_len, found_flag, result_index, start_index):
    # Create a local array to store the current password attempt for each thread
    local_attempt = cuda.local.array(64, dtype=np.int32)

    # Unique thread ID across all blocks and threads
    thread_id = cuda.grid(1)
    global_id = thread_id + start_index

    # Exit if this thread's global ID exceeds the search space
    if global_id >= char_set_len ** password_len:
        return

    # Generate the current password attempt based on global ID
    temp_id = global_id
    for i in range(password_len - 1, -1, -1):
        local_attempt[i] = temp_id % char_set_len
        temp_id //= char_set_len

    # If password hasn't been found yet, write it to result_index
    for i in range(password_len):
        result_index[thread_id, i] = local_attempt[i]

# Main GPU Brute-Force Function
def brute_force_gpu(char_set, max_password_len=10, debug_interval=1000000):
    char_set_len = len(char_set)

    # Set up GPU parameters
    threads_per_block = 256
    blocks_per_grid = 8
    total_threads = threads_per_block * blocks_per_grid

    # Convert character set to numpy array
    char_set_array = np.array([c for c in char_set], dtype=np.unicode_)

    start_time = time.time()

    # Iterate over possible password lengths, starting from 1 until password is found
    password_len = 1
    while True:
        # Set up found flag and result index for each length
        found_flag = np.zeros(1, dtype=np.int32)
        result_index = np.zeros((total_threads, password_len), dtype=np.int32)

        # Copy data to GPU
        found_flag_device = cuda.to_device(found_flag)
        result_index_device = cuda.to_device(result_index)

        # Iterate over the search space in chunks for the current length
        total_combinations = char_set_len ** password_len
        for start_index in range(0, total_combinations, total_threads):
            gpu_brute_force[blocks_per_grid, threads_per_block](
                char_set_len,
                password_len,
                found_flag_device,
                result_index_device,
                start_index
            )
            cuda.synchronize()

            # Retrieve result attempts from GPU
            result_index = result_index_device.copy_to_host()

            # Iterate over all generated attempts and send them for verification
            for i in range(total_threads):
                attempt = "".join([char_set[result_index[i, j]] for j in range(password_len)])
                is_correct = send_attempt_to_server(attempt)
                print(f"Trying: {attempt}")

                # If the password is correct, return it
                if is_correct:
                    end_time = time.time()
                    print(f"Password found: {attempt}")
                    print(f"Time taken (GPU): {end_time - start_time:.2f} seconds")
                    return attempt

            # Update progress in the console
            progress_percentage = (start_index / total_combinations) * 100
            print(f"Progress: {progress_percentage:.2f}%")

        password_len += 1  # Increase the password length to try longer passwords

    print("Password not found in the search space.")
    print(f"Total time taken (GPU): {time.time() - start_time:.2f} seconds")
    return None

# Function to send the password attempt to the verification server (Script 2)
def send_attempt_to_server(password_attempt):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allow reuse of the socket address
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Connect to the server (Script 2)
    server_address = ('localhost', 65432)
    try:
        client_socket.connect(server_address)
        print(f"Connected to server at {server_address}")  # Confirmation message

        # Send the password attempt
        client_socket.sendall(password_attempt.encode('utf-8'))

        # Receive the response from the server
        data = client_socket.recv(1024)
        response = data.decode('utf-8')
        return response == "True"
    except Exception as e:
        print(f"Error connecting to server: {e}")
        return False
    finally:
        # Close the socket
        client_socket.close()
        # Adding a small delay to ensure connection closure
        time.sleep(0.01)

def main():
    # Character set includes lowercase, uppercase, numbers, and symbols
    char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+[]{}|:;\"<,>.?/"

    print(f"Attempting to crack the password using GPU brute-force...")

    found_password = brute_force_gpu(char_set)

    if found_password:
        print("Password successfully cracked!")
    else:
        print("Password cracking failed or password not found.")

if __name__ == "__main__":
    main()
