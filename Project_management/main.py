import numpy as np
import matplotlib.pyplot as plt

# Define the task data
task_names = ['T1', 'T2', 'T3', 'T4', 
             'T5', 'T6', 'T7', 'T8', 
             'T9', 'T10']
durations = [5, 7, 10, 14, 7, 5, 3, 5, 2, 5]
costs = [7250, 15000, 73000, 44000, 22000, 29000, 7500, 3000, 22000, 44000]

# Calculate the expected duration and cost using the Three Point Estimation formula
# expected_durations = [np.mean([durations[i]-2, durations[i], durations[i]+2]) for i in range(len(durations))]
expected_durations = [(durations[i]-1 + (4*durations[i]) + durations[i]+2)/6  for i in range(len(durations))]
expected_costs = [np.mean([costs[i]-costs[i]/2, costs[i], costs[i]+costs[i]/2]) for i in range(len(costs))]

# Plot the expected duration and cost
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Task')
ax1.set_ylabel('Duration (Days)', color=color)
ax1.bar(task_names, expected_durations, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Cost ($)', color=color)  # we already handled the x-label with ax1
ax2.bar(task_names, expected_costs, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
