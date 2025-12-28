from core.process import Process
from algorithms.fcfs import fcfs
from algorithms.round_robin import round_robin

print("CPU Scheduling Simulator Started\n")

processes = [
    Process(1, 0, 5),
    Process(2, 1, 3),
    Process(3, 2, 8)
]

print("=== FCFS ===")
fcfs_result = fcfs(processes)
for p in fcfs_result:
    print(f"P{p.pid} WT={p.waiting_time} TAT={p.turnaround_time}")

# recreate processes (important)
processes = [
    Process(1, 0, 5),
    Process(2, 1, 3),
    Process(3, 2, 8)
]

print("\n=== Round Robin (TQ = 2) ===")
rr_result = round_robin(processes, time_quantum=2)
for p in rr_result:
    print(f"P{p.pid} WT={p.waiting_time} TAT={p.turnaround_time}")
