import plotly.express as px

# Define the data
data = [dict(Task="Task 1", Start='2023-01-01', Finish='2023-01-05', Resource='Project Manager, Researcher', Cost='$ 7,250'),
        dict(Task="Task 2", Start='2023-01-06', Finish='2023-01-12', Resource='Project Manager, Legal Advisor', Cost='$ 15,000'),
        dict(Task="Task 3", Start='2023-01-13', Finish='2023-01-22', Resource='Project Manager, Booking Agent', Cost='$ 73,000'),
        dict(Task="Task 4", Start='2023-01-23', Finish='2023-02-05', Resource='Project Manager, Marketing Team', Cost='$ 44,000'),
        dict(Task="Task 5", Start='2023-02-06', Finish='2023-02-12', Resource='Project Manager, Event Coordination', Cost='$ 22,000'),
        dict(Task="Task 6", Start='2023-02-13', Finish='2023-02-17', Resource='Project Manager, Security Specialist', Cost='$ 29,000'),
        dict(Task="Task 7", Start='2023-02-18', Finish='2023-02-20', Resource='Project Manage, Event Coordinator', Cost='$ 7,500'),
        dict(Task="Task 8", Start='2023-02-21', Finish='2023-02-25', Resource='Project Management, Legal Advisor', Cost='$ 3,000'),
        dict(Task="Task 9", Start='2023-02-26', Finish='2023-02-27', Resource='Project Manager, Technical Team', Cost='$ 22,000'),
        dict(Task="Task 10", Start='2023-03-01', Finish='2023-03-05', Resource='Project Management, Event Coordinator', Cost='$ 44,000')]

# Plot the Gantt chart
fig = px.timeline(data, x_start='Start', x_end='Finish', y='Task', color='Cost', text='Resource')
fig.show()
