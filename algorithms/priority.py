def priority_scheduling(processes):
    time = 0
    completed = []
    ready = []

    processes = sorted(processes, key=lambda p: p.arrival_time)
    n = len(processes)
    i = 0

    while len(completed) < n:
        # add arrived processes
        while i < n and processes[i].arrival_time <= time:
            ready.append(processes[i])
            i += 1

        if not ready:
            time = processes[i].arrival_time
            continue

        # pick highest priority (lowest number)
        ready.sort(key=lambda p: p.priority)
        current = ready.pop(0)

        time += current.burst_time
        current.completion_time = time
        current.turnaround_time = time - current.arrival_time
        current.waiting_time = current.turnaround_time - current.burst_time

        completed.append(current)

    return completed
