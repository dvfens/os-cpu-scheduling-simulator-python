def srtf(processes):
    time = 0
    completed = 0
    n = len(processes)

    processes.sort(key=lambda p: p.arrival_time)

    while completed < n:
        # get available processes
        available = [
            p for p in processes
            if p.arrival_time <= time and p.remaining_time > 0
        ]

        if not available:
            time += 1
            continue

        # pick shortest remaining time
        current = min(available, key=lambda p: p.remaining_time)

        current.remaining_time -= 1
        time += 1

        if current.remaining_time == 0:
            completed += 1
            current.completion_time = time
            current.turnaround_time = (
                current.completion_time - current.arrival_time
            )
            current.waiting_time = (
                current.turnaround_time - current.burst_time
            )

    return processes
