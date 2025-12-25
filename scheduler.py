class Process:
    def __init__(self, name, arrival, service):
        self.name = name
        self.arrival = arrival
        self.service = service


def fcfs_schedule(processes):
    
    processes.sort(key=lambda x: x.arrival)
    
    current_time = 0
    for process in processes:
        if current_time < process.arrival:
            current_time = process.arrival
        print(f"Process {process.name} runs from {current_time} to {current_time + process.service}")
        current_time += process.service

if __name__ == "__main__":
     processes = [
         Process("P1", arrival=0, service=3),
         Process("P2", arrival=1, service=2)
     ]
     
     # Run the FCFS scheduler
     fcfs_schedule(processes)