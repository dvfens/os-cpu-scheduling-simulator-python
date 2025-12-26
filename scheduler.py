class Process:
    def __init__(self, name, arrival, service):
        self.name = name
        self.arrival = arrival
        self.service = service
        self.remaining= service


def fcfs_schedule(processes):
    
    processes.sort(key=lambda x: x.arrival)
    
    current_time = 0
    for process in processes:
        if current_time < process.arrival:
            current_time = process.arrival
        print(f"Process {process.name} runs from {current_time} to {current_time + process.service}")
        current_time += process.service

from collections import deque

def round_robin_schedule(processes, quantum):
    processes.sort(key=lambda x: x.arrival)
    queue = deque()
    time = 0
    index = 0
    n = len(processes)

    print(f"\nRound Robin Scheduling (Quantum = {quantum})")

    while queue or index < n:

        while index < n and processes[index].arrival <= time:
            queue.append(processes[index])
            index += 1

        if not queue:
            time = processes[index].arrival
            continue

        process = queue.popleft()
        exec_time = min(quantum, process.remaining)

        print(f"Process {process.name} runs from {time} to {time + exec_time}")

        time += exec_time
        process.remaining -= exec_time

       
        while index < n and processes[index].arrival <= time:
            queue.append(processes[index])
            index += 1

        if process.remaining > 0:
            queue.append(process)

if __name__ == "__main__":
    processes = [
        Process("P1", 0, 5),
        Process("P2", 1, 3),
        Process("P3", 2, 1)
    ]

    fcfs_schedule(processes)

    
    processes_rr = [
        Process("P1", 0, 5),
        Process("P2", 1, 3),
        Process("P3", 2, 1)
    ]

    round_robin_schedule(processes_rr, quantum=2)
