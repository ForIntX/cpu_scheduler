# utils.py

CONTEXT_SWITCH_TIME = 0.001

def calculate_metrics(processes, gantt_chart, context_switch_count):
    total_burst_time = sum(p.burst_time for p in processes)
    total_waiting_time = 0
    total_turnaround_time = 0
    max_waiting_time = 0
    max_turnaround_time = 0
    
    if not processes:
        return {}

    for p in processes:
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time
        
        total_waiting_time += p.waiting_time
        total_turnaround_time += p.turnaround_time
        max_waiting_time = max(max_waiting_time, p.waiting_time)
        max_turnaround_time = max(max_turnaround_time, p.turnaround_time)

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)
    
    throughput_times = [50, 100, 150, 200]
    throughput = {t: len([p for p in processes if p.completion_time <= t]) for t in throughput_times}
    
    total_time = gantt_chart[-1][2] if gantt_chart else 0
    idle_time = sum(duration for pid, start, end in gantt_chart if pid == 'IDLE' for duration in [end - start])
    
    total_overhead = context_switch_count * CONTEXT_SWITCH_TIME
    cpu_active_time = total_burst_time
    
    total_elapsed_time = cpu_active_time + idle_time + total_overhead
    
    cpu_utilization = (cpu_active_time / total_elapsed_time) * 100 if total_elapsed_time > 0 else 0
    
    return {
        'avg_waiting_time': avg_waiting_time,
        'max_waiting_time': max_waiting_time,
        'avg_turnaround_time': avg_turnaround_time,
        'max_turnaround_time': max_turnaround_time,
        'throughput': throughput,
        'cpu_utilization': cpu_utilization,
        'context_switch_count': context_switch_count,
        'total_elapsed_time': total_elapsed_time
    }

def write_results(filename, algorithm_name, processes, gantt_chart, metrics):
    with open(filename, 'w') as f:
        f.write(f"### İşletim Sistemleri ÖDEV 1 - {algorithm_name} Sonuçları ###\n\n")

        f.write("a) Zaman Tablosu (Gantt Chart):\n")
        gantt_str = ""
        for pid, start, end in gantt_chart:
            gantt_str += f"[{start}]--{pid}--[{end}] "
        f.write(gantt_str.strip() + "\n\n")

        f.write(f"b) Maksimum ve Ortalama Bekleme Süresi (Waiting Time):\n")
        f.write(f"   Ortalama Bekleme Süresi: {metrics.get('avg_waiting_time', 0):.3f}\n")
        f.write(f"   Maksimum Bekleme Süresi: {metrics.get('max_waiting_time', 0)}\n\n")

        f.write(f"c) Maksimum ve Ortalama Tamamlanma Süresi (Turnaround Time):\n")
        f.write(f"   Ortalama Tamamlanma Süresi: {metrics.get('avg_turnaround_time', 0):.3f}\n")
        f.write(f"   Maksimum Tamamlanma Süresi: {metrics.get('max_turnaround_time', 0)}\n\n")

        f.write("d) T=[50, 100, 150, 200] için İş Tamamlama Sayısı (Throughput):\n")
        for t, count in metrics.get('throughput', {}).items():
             f.write(f"   T={t}: {count} adet süreç tamamlandı\n")
        f.write("\n")

        f.write(f"e) Ortalama CPU Verimliliği (Context Switch Time={CONTEXT_SWITCH_TIME}):\n")
        f.write(f"   CPU Verimliliği: {metrics.get('cpu_utilization', 0):.2f}%\n\n")

        f.write(f"f) Toplam Bağlam Değiştirme Sayısı: {metrics.get('context_switch_count', 0)}\n")