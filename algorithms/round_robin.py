from collections import deque

def round_robin(processes, time_quantum):
    time = 0
    queue = deque()
    completed = []

    processes = sorted(processes, key=lambda p: p.arrival_time)
    i = 0
    n = len(processes)

    while i < n or queue:
        # Add arrived processes to queue
        while i < n and processes[i].arrival_time <= time:
            queue.append(processes[i])
            i += 1

        if not queue:
            time = processes[i].arrival_time
            continue

        current = queue.popleft()

        exec_time = min(time_quantum, current.remaining_time)
        current.remaining_time -= exec_time
        time += exec_time

        # Add newly arrived processes during execution
        while i < n and processes[i].arrival_time <= time:
            queue.append(processes[i])
            i += 1

        if current.remaining_time == 0:
            current.completion_time = time
            current.turnaround_time = (
                current.completion_time - current.arrival_time
            )
            current.waiting_time = (
                current.turnaround_time - current.burst_time
            )
            completed.append(current)
        else:
            queue.append(current)

    return completed
