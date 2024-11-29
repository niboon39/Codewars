import numpy as np
from numba import cuda
import time
import threading


# GPU Kernel Function
@cuda.jit
def gpu_brute_force(target_password, char_set, char_set_len, password_len, found_flag, result_index, start_index,
                    debug_array):
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

    # Compare the generated attempt with the target password
    if found_flag[0] == 0:  # Proceed only if the password hasn't been found yet
        match = True
        for i in range(password_len):
            if char_set[local_attempt[i]] != target_password[i]:
                match = False
                break

        if match:
            found_flag[0] = 1  # Indicate that a match has been found
            for i in range(password_len):
                result_index[i] = local_attempt[i]


# Main GPU Brute-Force Function
def brute_force_gpu(target_password, char_set, max_password_len=10, debug_interval=1000000):
    char_set_len = len(char_set)

    # Set up GPU parameters
    threads_per_block = 512 # 256
    blocks_per_grid = 1024 # 512
    total_threads = threads_per_block * blocks_per_grid

    # Convert character set and target password to numpy arrays
    char_set_array = np.array([c for c in char_set], dtype=np.unicode_)
    target_password_array = np.array([c for c in target_password], dtype=np.unicode_)

    start_time = time.time()

    # Iterate over possible password lengths, starting from 1 up to the maximum password length
    for password_len in range(1, max_password_len + 1):
        # Set up found flag and result index for each length
        found_flag = np.zeros(1, dtype=np.int32)
        result_index = np.zeros(password_len, dtype=np.int32)
        debug_array = np.zeros((5, password_len), dtype=np.int32)

        # Copy data to GPU
        found_flag_device = cuda.to_device(found_flag)
        result_index_device = cuda.to_device(result_index)
        debug_array_device = cuda.to_device(debug_array)

        # Iterate over the search space in chunks for the current length
        total_combinations = char_set_len ** password_len
        for start_index in range(0, total_combinations, total_threads):
            gpu_brute_force[blocks_per_grid, threads_per_block](
                target_password_array,
                char_set_array,
                char_set_len,
                password_len,
                found_flag_device,
                result_index_device,
                start_index,
                debug_array_device
            )
            cuda.synchronize()

            # Update progress in the console
            progress_percentage = (start_index / total_combinations) * 100
            print(f"Progress: {progress_percentage:.2f}%")

            # Debugging: Retrieve and print debug information for the first few threads
            if start_index % debug_interval == 0:
                debug_array = debug_array_device.copy_to_host()
                print(f"[DEBUG] Length {password_len}, Batch starting at index {start_index}")
                for i in range(5):
                    decoded_debug = ''.join([char_set[idx] for idx in debug_array[i]])
                    print(f"[DEBUG] Thread {i} Attempt: {decoded_debug}")

            # Check if the password was found
            found_flag = found_flag_device.copy_to_host()
            if found_flag[0] == 1:
                result_index = result_index_device.copy_to_host()
                found_password = "".join([char_set[result_index[i]] for i in range(password_len)])
                end_time = time.time()
                print(f"Password found: {found_password}")
                print(f"Time taken (GPU): {end_time - start_time:.2f} seconds")


                if found_password == target_password:
                    return found_password

    print("Password not found in the search space.")
    print(f"Total time taken (GPU): {time.time() - start_time:.2f} seconds")
    return None


# Main function to run the password cracker
def main():
    # User inputs for simulation
    char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+[]{}|:;\"<,>.?/"
    password = input("Enter the password to crack: ")  # Example: 'abc'
    max_password_len = int(input("Enter the maximum password length to search: "))  # Example: 10

    print(f"Attempting to crack the password using GPU brute-force...")


    found_password = brute_force_gpu(password, char_set, max_password_len)

    if found_password == password:
        print("Password successfully cracked!")
    else:
        print("Password cracking failed or password not found.")


if __name__ == "__main__":
    main()
