class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = None
        self.end_time = None
        self.waiting_time = None

class STCF:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def execute(self):
        current_time = 0
        remaining_processes = self.processes.copy()
        completed_processes = []
        while remaining_processes:
            # Sort the remaining processes by remaining time
            remaining_processes.sort(key=lambda process: process.remaining_time)

            # Get the next process with the shortest remaining time
            process = remaining_processes.pop(0)

            # Update the start and end times for the process
            if current_time < process.arrival_time:
                current_time = process.arrival_time
            process.start_time = current_time
            process.end_time = current_time + process.remaining_time
            process.waiting_time = process.start_time - process.arrival_time

            # Update the remaining time for all other processes
            for other_process in remaining_processes:
                if other_process.arrival_time <= process.end_time:
                    other_process.remaining_time -= process.remaining_time

            # Update the current time and add the process to the completed list
            current_time = process.end_time
            completed_processes.append(process)

        # Replace the processes list with the completed list
        self.processes = completed_processes

    def get_average_waiting_time(self):
        if len(self.processes) == 0:
            return 0
        total_waiting_time = 0
        for process in self.processes:
            total_waiting_time += process.waiting_time
        return total_waiting_time / len(self.processes)

# Create a list of Process objects
processes = [
    Process(1, 0, 10),
    Process(2, 2, 5),
    Process(3, 5, 2),
    Process(4, 6, 3),
    Process(5, 8, 4)
]

# Instantiate the STCF scheduler and add the list of Process objects to it
scheduler = STCF()
for process in processes:
    scheduler.add_process(process)

# Run the simulation
scheduler.execute()

# Print the average waiting time
print("Average waiting time:", scheduler.get_average_waiting_time())