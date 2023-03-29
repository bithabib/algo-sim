class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = None
        self.end_time = None
        self.waiting_time = None
        self.response_time = 0

class RoundRobin:
    def __init__(self, quantum):
        self.processes = []
        self.quantum = quantum

    def add_process(self, process):
        self.processes.append(process)

    def execute(self):
        current_time = 0
        remaining_processes = self.processes.copy()
        completed_processes = []
        while remaining_processes:
            # Iterate over the remaining processes and execute them for the quantum time
            for process in remaining_processes:
                if process.remaining_time <= self.quantum:
                    # If the remaining time for the process is less than or equal to the quantum, execute the process to completion
                    if process.start_time == None:
                        process.start_time = current_time
                        process.response_time = process.start_time - process.arrival_time
                    process.start_time = current_time
                    process.end_time = current_time + process.remaining_time
                    process.waiting_time = process.start_time - process.arrival_time
                    current_time = process.end_time
                    process.remaining_time = 0
                    completed_processes.append(process)
                else:
                    # Otherwise, execute the process for the quantum time and move on to the next process
                    process.start_time = current_time
                    process.end_time = current_time + self.quantum
                    process.waiting_time = process.start_time - process.arrival_time
                    current_time = process.end_time
                    process.remaining_time -= self.quantum

            # Remove any completed processes from the remaining processes list
            remaining_processes = [process for process in remaining_processes if process.remaining_time > 0]

        # Replace the processes list with the completed list
        self.processes = completed_processes

    def get_average_waiting_time(self):
        if len(self.processes) == 0:
            return 0
        total_waiting_time = 0
        for process in self.processes:
            total_waiting_time += process.waiting_time
        return total_waiting_time / len(self.processes)

    def response_time(self):
        if len(self.processes) == 0:
            return 0
        total_response_time = 0
        for process in self.processes:
            total_response_time += process.response_time
        return total_response_time / len(self.processes)

# Create a list of Process objects
processes = [
    Process(1, 0, 10),
    Process(2, 2, 5),
    Process(3, 5, 2),
    Process(4, 6, 3),
    Process(5, 7, 4),
    Process(5, 8, 2),
    Process(5, 9, 2),
    Process(5, 10, 2),
    Process(5, 11, 2),
    Process(5, 12, 2),
    Process(5, 13, 2),
    Process(5, 14, 2),
    Process(5, 15, 2),
    Process(5, 16, 8),
    Process(5, 16, 8),
    Process(5, 16, 8),
    Process(5, 16, 8),
    Process(5, 16, 8),
]
# Instantiate the RoundRobin scheduler with a quantum of 3 and add the list of Process objects to it
scheduler = RoundRobin(3)
for process in processes:
    scheduler.add_process(process)

# Run the simulation
scheduler.execute()

# Print the average waiting time
print("Average waiting time:", scheduler.get_average_waiting_time())
print("Average response time:", scheduler.response_time())