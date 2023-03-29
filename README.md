# Scheduling Algorithms in Python
This repository contains Python implementations of three different scheduling algorithms:

First Come, First Serve (FCFS)
Shortest Job First (SJF)
Round Robin
Each implementation consists of a Python class that represents a scheduling algorithm, along with a Process class that represents a process that can be scheduled by the algorithm. The implementations include methods for adding processes to the scheduler, executing the scheduler, and calculating the average waiting time of the processes.

## Installation
To use these scheduling algorithms, you will need Python 3 installed on your computer. You can download Python 3 from the official website: https://www.python.org/downloads/

Once you have Python 3 installed, you can clone this repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/yourusername/scheduling-algorithms.git
Usage
Each scheduling algorithm implementation is contained in a separate Python file (fcfs.py, sjf.py, and round_robin.py). To use an implementation, you can import the corresponding class into your Python code and create an instance of the class:

python
Copy code
from fcfs import FCFS

scheduler = FCFS()
To add processes to the scheduler, you can create Process objects and add them to the scheduler using the add_process method:

python
Copy code
from fcfs import FCFS, Process

scheduler = FCFS()

process1 = Process(1, 0, 10)
process2 = Process(2, 2, 5)
process3 = Process(3, 5, 2)

scheduler.add_process(process1)
scheduler.add_process(process2)
scheduler.add_process(process3)
To execute the scheduler and calculate the average waiting time, you can call the execute method and the get_average_waiting_time method:

python
Copy code
scheduler.execute()

average_waiting_time = scheduler.get_average_waiting_time()
print("Average waiting time:", average_waiting_time)
Contributing
If you find a bug or would like to suggest an improvement to these scheduling algorithm implementations, please create a GitHub issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

I hope this helps! Let me know if you have any questions.
