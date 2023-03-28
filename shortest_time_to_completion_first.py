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
        
        while remaining_processes:
        # while current_time < 10:
            print("current time:",current_time)
            queue_and_running_processes = []
            for process in remaining_processes:
                if process.arrival_time <= current_time:
                    queue_and_running_processes.append(process)
            queue_and_running_processes.sort(key=lambda process: process.remaining_time)
            process = queue_and_running_processes.pop(0)
            if process.arrival_time <= current_time:
                print("currently running process:",process.pid)
                process.remaining_time -= 1
                if process.remaining_time == 0:
                    process.end_time = current_time + 1
                    process.waiting_time = process.end_time - process.arrival_time - process.burst_time
                    remaining_processes.remove(process)
            current_time += 1

            for process in remaining_processes:
                print("remaining processes:{}, remaining time:{}".format(process.pid,process.remaining_time))
                
            

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