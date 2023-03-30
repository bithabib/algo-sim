import time
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
        self.number_of_time_run = 1

class PTL_WT:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def execute(self):
        current_time = 0
        remaining_processes = self.processes.copy()
        second_queue = []
        runned_process_id_list = []
        while remaining_processes:
            print("current time:",current_time)
            queue_and_running_processes = []
            for process in remaining_processes:
                if process.arrival_time <= current_time:
                    queue_and_running_processes.append(process)
                    if len(queue_and_running_processes) > 1:
                        pop_previous_process = queue_and_running_processes.pop(0)
                        if (pop_previous_process.burst_time - pop_previous_process.remaining_time) >= 3 * pop_previous_process.number_of_time_run:
                            second_queue.append(pop_previous_process)
                            if len(second_queue) > len(queue_and_running_processes)*2:
                                second_queue.sort(key=lambda process: (process.remaining_time - (process.consecutive_waiting_time)))
                                queue_and_running_processes.append(second_queue.pop(0))
                        else:
                            # There is no problem to append first or last in the queue because the queue is sorted by remaining time
                            queue_and_running_processes.append(pop_previous_process) 
                    
                    else:
                        pop_previous_process = queue_and_running_processes.pop(0)
                        if (pop_previous_process.burst_time - pop_previous_process.remaining_time) >= 3 * pop_previous_process.number_of_time_run:
                            second_queue.append(pop_previous_process)
                            if len(second_queue) > len(queue_and_running_processes)*2:
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
            # runned_process_id_list = []
            if process.arrival_time <= current_time:

                if process.pid in runned_process_id_list:
                    if runned_process_id_list[-1] != process.pid:
                        process.number_of_time_run += 1
                    else:
                        process.number_of_time_run = process.number_of_time_run
                runned_process_id_list.append(process.pid)

                print("currently running process:{}, Number of time run:{}".format(process.pid,process.number_of_time_run))
                for processss in remaining_processes:
                    print("remaining processes:{}, remaining time:{}".format(processss.pid,processss.remaining_time))
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
            # time.sleep(5)

            # for process in remaining_processes:
            #     print("remaining processes:{}, remaining time:{}".format(process.pid,process.remaining_time))
                
            

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
    Process(1, 0, 6),
    Process(2, 2, 3),
    Process(3, 5, 2),
    Process(4, 5, 2),
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