class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = None
        self.end_time = None
        self.waiting_time = None

class FCFS:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def execute(self):
        current_time = 0
        for process in self.processes:
            if current_time < process.arrival_time:
                current_time = process.arrival_time
            process.start_time = current_time
            process.end_time = current_time + process.burst_time
            process.waiting_time = process.start_time - process.arrival_time
            current_time = process.end_time

    def get_average_waiting_time(self):
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

# Instantiate the FCFS scheduler and add the list of Process objects to it
scheduler = FCFS()
for process in processes:
    scheduler.add_process(process)

# Run the simulation
scheduler.execute()

# Print the average waiting time
print("Average waiting time:", scheduler.get_average_waiting_time())