# algorithms.py

from utils import calculate_metrics

def count_context_switches(gantt_chart):
    if not gantt_chart:
        return 0
    
    switch_count = 0
    last_pid = gantt_chart[0][0]
    
    for pid, _, _ in gantt_chart[1:]:
        if pid != 'IDLE' and last_pid != 'IDLE' and pid != last_pid:
            switch_count += 1
        
        if pid != last_pid:
             last_pid = pid

    return switch_count

# --- 1. FCFS (First Come First Served) ---
def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    gantt_chart = []
    
    for process in processes:
        
        if current_time < process.arrival_time:
            idle_start = current_time
            current_time = process.arrival_time
            if current_time > idle_start:
                 gantt_chart.append(('IDLE', idle_start, current_time))
        
        process.start_time = current_time
        start_exec_time = current_time
        current_time += process.burst_time
        process.completion_time = current_time
        
        gantt_chart.append((process.pid, start_exec_time, current_time))
            
    context_switch_count = count_context_switches(gantt_chart)
            
    metrics = calculate_metrics(processes, gantt_chart, context_switch_count)
    return processes, gantt_chart, metrics

# --- 2. Preemptive SJF (Shortest Job First) ---
def psjf_scheduling(processes):
    processes_to_arrive = sorted(processes, key=lambda x: x.arrival_time)
    current_time = 0
    gantt_chart = []
    ready_queue = []
    finished_count = 0
    last_pid = None

    while finished_count < len(processes) or ready_queue or processes_to_arrive:
        
        while processes_to_arrive and processes_to_arrive[0].arrival_time <= current_time:
            ready_queue.append(processes_to_arrive.pop(0))
        
        if not ready_queue:
            if not processes_to_arrive:
                break
            
            idle_start = current_time
            current_time = processes_to_arrive[0].arrival_time
            gantt_chart.append(('IDLE', idle_start, current_time))
            last_pid = 'IDLE' 
            continue

        ready_queue.sort(key=lambda x: x.remaining_time)
        current_p = ready_queue[0]

        next_arrival = processes_to_arrive[0].arrival_time if processes_to_arrive else float('inf')
        run_duration = min(current_p.remaining_time, next_arrival - current_time)

        if current_p.start_time == -1:
            current_p.start_time = current_time
        
        current_p.remaining_time -= run_duration
        new_time = current_time + run_duration
        
        if gantt_chart and gantt_chart[-1][0] == current_p.pid and gantt_chart[-1][2] == current_time:
            gantt_chart[-1] = (current_p.pid, gantt_chart[-1][1], new_time)
        else:
            gantt_chart.append((current_p.pid, current_time, new_time))
        
        current_time = new_time
        
        if current_p.remaining_time == 0:
            current_p.completion_time = current_time
            ready_queue.pop(0)
            finished_count += 1
            last_pid = None
        else:
            last_pid = current_p.pid

    context_switch_count = count_context_switches(gantt_chart)
    metrics = calculate_metrics(processes, gantt_chart, context_switch_count)
    return processes, gantt_chart, metrics

# --- 3. Non-Preemptive SJF (Shortest Job First) ---
def npsjf_scheduling(processes):
    processes_to_arrive = sorted(processes, key=lambda x: x.arrival_time)
    current_time = 0
    gantt_chart = []
    ready_queue = []
    
    while processes_to_arrive or ready_queue:
        
        while processes_to_arrive and processes_to_arrive[0].arrival_time <= current_time:
            ready_queue.append(processes_to_arrive.pop(0))
        
        if not ready_queue:
            if not processes_to_arrive:
                break
            idle_start = current_time
            current_time = processes_to_arrive[0].arrival_time
            gantt_chart.append(('IDLE', idle_start, current_time))
            continue
            
        ready_queue.sort(key=lambda x: (x.burst_time, x.arrival_time))
        process = ready_queue.pop(0)

        if process.start_time == -1:
            process.start_time = current_time

        start_exec_time = current_time
        current_time += process.burst_time
        process.completion_time = current_time
        
        gantt_chart.append((process.pid, start_exec_time, current_time))
            
    context_switch_count = count_context_switches(gantt_chart)
            
    metrics = calculate_metrics(processes, gantt_chart, context_switch_count)
    return processes, gantt_chart, metrics

# --- 4. Round Robin (RR) ---
def rr_scheduling(processes, quantum=4):
    processes_to_arrive = sorted(processes, key=lambda x: x.arrival_time)
    current_time = 0
    gantt_chart = []
    ready_queue = []
    finished_count = 0
    
    while processes_to_arrive and processes_to_arrive[0].arrival_time <= current_time:
         ready_queue.append(processes_to_arrive.pop(0))
         
    while finished_count < len(processes) or ready_queue:
        
        if not ready_queue:
            if not processes_to_arrive:
                break
            
            idle_start = current_time
            current_time = processes_to_arrive[0].arrival_time
            gantt_chart.append(('IDLE', idle_start, current_time))
            
            while processes_to_arrive and processes_to_arrive[0].arrival_time <= current_time:
                ready_queue.append(processes_to_arrive.pop(0))
            continue
            
        current_p = ready_queue.pop(0)
        
        run_duration = min(current_p.remaining_time, quantum)

        if current_p.start_time == -1:
            current_p.start_time = current_time
            
        current_p.remaining_time -= run_duration
        new_time = current_time + run_duration
        
        gantt_chart.append((current_p.pid, current_time, new_time))
        current_time = new_time
        
        while processes_to_arrive and processes_to_arrive[0].arrival_time <= current_time:
            ready_queue.append(processes_to_arrive.pop(0))

        if current_p.remaining_time == 0:
            current_p.completion_time = current_time
            finished_count += 1
        else:
            ready_queue.append(current_p)
            
    context_switch_count = count_context_switches(gantt_chart)
    metrics = calculate_metrics(processes, gantt_chart, context_switch_count)
    return processes, gantt_chart, metrics


# --- 5. Preemptive Priority Scheduling ---
def ppriority_scheduling(processes):
    processes_to_arrive = sorted(processes, key=lambda x: x.arrival_time)
    current_time = 0
    gantt_chart = []
    ready_queue = []
    finished_count = 0
    last_pid = None
    
    while finished_count < len(processes) or ready_queue or processes_to_arrive:
        
        while processes_to_arrive and processes_to_arrive[0].arrival_time <= current_time:
            ready_queue.append(processes_to_arrive.pop(0))
        
        if not ready_queue:
            if not processes_to_arrive:
                break
            
            idle_start = current_time
            current_time = processes_to_arrive[0].arrival_time
            gantt_chart.append(('IDLE', idle_start, current_time))
            last_pid = 'IDLE' 
            continue

        ready_queue.sort(key=lambda x: (-x.priority, x.arrival_time))
        current_p = ready_queue[0]

        next_arrival = processes_to_arrive[0].arrival_time if processes_to_arrive else float('inf')
        run_duration = min(current_p.remaining_time, next_arrival - current_time)

        if current_p.start_time == -1:
            current_p.start_time = current_time

        current_p.remaining_time -= run_duration
        new_time = current_time + run_duration
        
        if gantt_chart and gantt_chart[-1][0] == current_p.pid and gantt_chart[-1][2] == current_time:
            gantt_chart[-1] = (current_p.pid, gantt_chart[-1][1], new_time)
        else:
            gantt_chart.append((current_p.pid, current_time, new_time))
        
        current_time = new_time
        
        if current_p.remaining_time == 0:
            current_p.completion_time = current_time
            ready_queue.pop(0) 
            finished_count += 1
            last_pid = None
        else:
             last_pid = current_p.pid

    context_switch_count = count_context_switches(gantt_chart)
    metrics = calculate_metrics(processes, gantt_chart, context_switch_count)
    return processes, gantt_chart, metrics


# --- 6. Non-Preemptive Priority Scheduling ---
def nppriority_scheduling(processes):
    processes_to_arrive = sorted(processes, key=lambda x: x.arrival_time)
    current_time = 0
    gantt_chart = []
    ready_queue = []

    while processes_to_arrive or ready_queue:
        
        while processes_to_arrive and processes_to_arrive[0].arrival_time <= current_time:
            ready_queue.append(processes_to_arrive.pop(0))
        
        if not ready_queue:
            if not processes_to_arrive:
                break
            idle_start = current_time
            current_time = processes_to_arrive[0].arrival_time
            gantt_chart.append(('IDLE', idle_start, current_time))
            continue
            
        ready_queue.sort(key=lambda x: (-x.priority, x.arrival_time))
        process = ready_queue.pop(0)

        if process.start_time == -1:
            process.start_time = current_time

        start_exec_time = current_time
        current_time += process.burst_time
        process.completion_time = current_time
        
        gantt_chart.append((process.pid, start_exec_time, current_time))
            
    context_switch_count = count_context_switches(gantt_chart)
    metrics = calculate_metrics(processes, gantt_chart, context_switch_count)
    return processes, gantt_chart, metrics