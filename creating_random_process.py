# create random process data and save to csv
import random
import csv
# create random process data and save to csv
# first is process id
# second is arrival time
# third is burst time
# Define the number of processes and pages
num_processes = 200
data = []
for i in range(num_processes):
    process_id = i
    arrival_time = random.randint(0, 100)
    burst_time = random.randint(1, 10)
    data.append([process_id, arrival_time, burst_time])

# Sort the data by arrival time
data.sort(key=lambda x: x[1])
# save to csv
with open('random_process_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['process_id', 'arrival_time', 'burst_time'])
    writer.writerows(data)

