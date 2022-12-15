import matplotlib.pyplot as plt
from PID import PID
# Create an instance of the PID controller
pid = PID(kp=2, ki=0.5, kd=0)

# Set the initial setpoint and process variable
setpoint = 10
process_variable = 5

# Set the initial time and time step
time = 0
dt = 0.1

# Arrays to store the data for plotting
time_data = []
setpoint_data = []
process_variable_data = []

# Loop for a certain number of iterations
for i in range(100):
    # Calculate the error between the setpoint and the process variable
    error = setpoint - process_variable
    
    # Update the PID controller
    output = pid.update(error, dt)
    
    # Use the output of the PID controller to adjust the system
    process_variable += output * dt
    
    # Store the data for plotting
    time_data.append(time)
    setpoint_data.append(setpoint)
    process_variable_data.append(process_variable)
    
    # Update the time
    time += dt

# Plot the data
plt.plot(time_data, setpoint_data, label="Setpoint")
plt.plot(time_data, process_variable_data, label="Process Variable")
plt.legend()
plt.show()
