from core.process import Process
from algorithms.priority import priority_scheduling

processes = [
    Process(1, 0, 5, priority=2),
    Process(2, 1, 3, priority=1),
    Process(3, 2, 8, priority=3),
]

print("\n=== Priority Scheduling (Non-Preemptive) ===")
ps_result = priority_scheduling(processes)

for p in ps_result:
    print(f"P{p.pid} PR={p.priority} WT={p.waiting_time} TAT={p.turnaround_time}")
