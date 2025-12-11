# process.py

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority_str):
        self.pid = pid
        self.arrival_time = int(arrival_time)
        self.burst_time = int(burst_time)
        self.remaining_time = int(burst_time)
        self.priority_str = priority_str
        self.priority = self._set_numeric_priority(priority_str)
        self.start_time = -1
        self.completion_time = -1
        self.turnaround_time = 0
        self.waiting_time = 0

    def _set_numeric_priority(self, priority_str):
        prio_str = priority_str.lower()
        if prio_str == 'high':
            return 3
        elif prio_str == 'normal':
            return 2
        elif prio_str == 'low':
            return 1
        else:
            return 0

    def __repr__(self):
        return (f"({self.pid}, AT:{self.arrival_time}, BT:{self.burst_time}, "
                f"Prio:{self.priority} ({self.priority_str}), RT:{self.remaining_time})")

def load_processes(filename):
    processes = []
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines[1:]: 
                parts = line.strip().split(',')
                if len(parts) == 4:
                    pid, at, bt, prio = parts
                    processes.append(Process(pid, at, bt, prio))
        return processes
    except FileNotFoundError:
        return []