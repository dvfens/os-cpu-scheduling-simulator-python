from core.process import Process
from algorithms.sjf import sjf


# ---------- SJF ----------
processes = [
    Process(1, 0, 5),
    Process(2, 1, 3),
    Process(3, 2, 8),
]

print("\n=== SJF (Non-Preemptive) ===")
sjf_result = sjf(processes)
for p in sjf_result:
    print(f"P{p.pid} WT={p.waiting_time} TAT={p.turnaround_time}")




