class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.change_in_burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = None
        self.end_time = None
        self.waiting_time = 0
        self.consecutive_waiting_time = 0
        self.response_time = None

class PTL_WT:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def execute(self):
        current_time = 0
        remaining_processes = self.processes.copy()
        second_queue = []
        
        while remaining_processes:
            print("current time:",current_time)
            queue_and_running_processes = []
            for process in remaining_processes:
                if process.arrival_time <= current_time:
                    queue_and_running_processes.append(process)
                    if len(queue_and_running_processes) > 1:
                        pop_previous_process = queue_and_running_processes.pop(0)
                        if (pop_previous_process.burst_time - pop_previous_process.remaining_time) > 3:
                            second_queue.append(pop_previous_process)
                            if len(second_queue) > len(queue_and_running_processes)*20:
                                second_queue.sort(key=lambda process: (process.remaining_time - (process.consecutive_waiting_time)))
                                queue_and_running_processes.append(second_queue.pop(0))
                        else:
                            queue_and_running_processes.append(pop_previous_process)
                    
                    else:
                        pop_previous_process = queue_and_running_processes.pop(0)
                        if (pop_previous_process.burst_time - pop_previous_process.remaining_time) > 3:
                            second_queue.append(pop_previous_process)
                            if len(second_queue) > len(queue_and_running_processes)*20:
                                second_queue.sort(key=lambda process: (process.remaining_time - (process.consecutive_waiting_time)))
                                queue_and_running_processes.append(second_queue.pop(0))
                        else:
                            queue_and_running_processes.append(pop_previous_process)
                else:
                    if len(queue_and_running_processes) == 0:
                        second_queue.sort(key=lambda process: (process.remaining_time - (process.consecutive_waiting_time)))
                        queue_and_running_processes.append(second_queue.pop(0))
                        
            queue_and_running_processes.sort(key=lambda process: (process.remaining_time - (process.consecutive_waiting_time)))

            print("Number of processes in queue:",len(queue_and_running_processes))
            process = queue_and_running_processes.pop(0)
            if process.arrival_time <= current_time:
                print("currently running process:",process.pid)
                if process.start_time == None:
                    process.start_time = current_time
                    process.response_time = process.start_time - process.arrival_time
                process.remaining_time -= 1
                if process.remaining_time == 0:
                    process.end_time = current_time + 1
                    process.waiting_time = process.end_time - process.arrival_time - process.burst_time
                    remaining_processes.remove(process)
            
            for process in queue_and_running_processes:
                process.consecutive_waiting_time += 1
            current_time += 1

            for process in remaining_processes:
                print("remaining processes:{}, remaining time:{}".format(process.pid,process.remaining_time))
                
            

    def get_average_waiting_time(self):
        if len(self.processes) == 0:
            return 0
        total_waiting_time = 0
        for process in self.processes:
            print("Process: {}, waiting_time: {}".format(process.pid, process.waiting_time))
            total_waiting_time += process.waiting_time
        return total_waiting_time / len(self.processes)
    
    def get_average_response_time(self):
        if len(self.processes) == 0:
            return 0
        total_response_time = 0
        for process in self.processes:
            print("Process: {}, response_time: {}".format(process.pid, process.response_time))
            total_response_time += process.response_time
        return total_response_time / len(self.processes)

# Create a list of Process objects
processes = [
    Process(1, 0, 20),
    Process(2, 2, 3),
    Process(3, 5, 2),
    Process(4, 6, 3),
    Process(5, 7, 4),
    Process(6, 8, 2),
    Process(7, 9, 2),
    Process(8, 10, 2),
    Process(9, 11, 2),
    Process(10, 12, 2),
    Process(11, 13, 2),
    Process(12, 14, 2),
    Process(13, 15, 2),
    Process(14, 18, 20),
    Process(15, 20, 8),
    Process(16, 23, 8),
    Process(17, 25, 8),
    Process(19, 30, 8),
    Process(20, 30, 8),
    Process(21, 30, 8),
    Process(22, 30, 8),
]

# Instantiate the PTL_WT scheduler and add the list of Process objects to it
scheduler = PTL_WT()
for process in processes:
    scheduler.add_process(process)

# Run the simulation
scheduler.execute()

# Print the average waiting time
print()
print("Average waiting time:", scheduler.get_average_waiting_time())
print()
print("Average response time:", scheduler.get_average_response_time())