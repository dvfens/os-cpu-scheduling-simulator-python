from core.process import Process
from core.process import Process

from algorithms.fcfs import fcfs
from algorithms.round_robin import round_robin
from algorithms.priority import priority_scheduling
from algorithms.preemptive_priority import preemptive_priority_scheduling
from algorithms.sjf import sjf
from algorithms.srtf import srtf


def create_processes(with_priority=False):
    if with_priority:
        return [
            Process(1, 0, 5, priority=2),
            Process(2, 1, 3, priority=1),
            Process(3, 2, 8, priority=3),
        ]
    else:
        return [
            Process(1, 0, 5),
            Process(2, 1, 3),
            Process(3, 2, 8),
        ]


def print_result(title, processes):
    print(f"\n=== {title} ===")
    print("PID | WT | TAT")
    for p in processes:
        print(f"P{p.pid}  | {p.waiting_time}  | {p.turnaround_time}")


if __name__ == "__main__":
    print("CPU Scheduling Simulator\n")

    # FCFS
    processes = create_processes()
    result = fcfs(processes)
    print_result("FCFS", result)

    # Round Robin
    processes = create_processes()
    result = round_robin(processes, time_quantum=2)
    print_result("Round Robin (TQ=2)", result)

    # Priority (Non-Preemptive)
    processes = create_processes(with_priority=True)
    result = priority_scheduling(processes)
    print_result("Priority (Non-Preemptive)", result)

    # Priority (Preemptive)
    processes = create_processes(with_priority=True)
    result = preemptive_priority_scheduling(processes)
    print_result("Priority (Preemptive)", result)

    # SJF
    processes = create_processes()
    result = sjf(processes)
    print_result("SJF (Non-Preemptive)", result)

    # SRTF
    processes = create_processes()
    result = srtf(processes)
    print_result("SRTF (Preemptive)", result)





