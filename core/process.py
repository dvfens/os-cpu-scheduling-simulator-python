class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority

        self.waiting_time = 0
        self.turnaround_time = 0
        self.completion_time = 0

    def __repr__(self):
        return f"P{self.pid}"
