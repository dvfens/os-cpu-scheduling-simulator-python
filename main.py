from core.process import Process
from algorithms.srtf import srtf


# ---------- SRTF ----------
processes = [
    Process(1, 0, 5),
    Process(2, 1, 3),
    Process(3, 2, 8),
]

print("\n=== SRTF (Preemptive SJF) ===")
srtf_result = srtf(processes)
for p in srtf_result:
    print(f"P{p.pid} WT={p.waiting_time} TAT={p.turnaround_time}")




