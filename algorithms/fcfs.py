def fcfs(processes):
    time = 0

    for p in processes:
        if time < p.arrival_time:
            time = p.arrival_time

        p.waiting_time = time - p.arrival_time
        time += p.burst_time
        p.turnaround_time = p.waiting_time + p.burst_time

    return processes
