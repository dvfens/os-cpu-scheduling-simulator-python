from core.process import Process
from algorithms.preemptive_priority import preemptive_priority_scheduling

# recreate processes (important)
processes = [
    Process(1, 0, 5, priority=2),
    Process(2, 1, 3, priority=1),
    Process(3, 2, 8, priority=3),
]

print("\n=== Preemptive Priority Scheduling ===")
pp_result = preemptive_priority_scheduling(processes)

for p in pp_result:
    print(f"P{p.pid} PR={p.priority} WT={p.waiting_time} TAT={p.turnaround_time}")
