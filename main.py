from core.process import Process
from algorithms.fcfs import fcfs

print("Scheduler started")

processes = [
    Process(1, 0, 5),
    Process(2, 1, 3),
    Process(3, 2, 8)
]

result = fcfs(processes)

print("PID | WT | TAT")
for p in result:
    print(p.pid, p.waiting_time, p.turnaround_time)
