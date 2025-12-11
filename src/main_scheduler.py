# main_scheduler.py

import threading
import os
import copy
import sys

# Projenin diğer modüllerini içe aktar
from process import load_processes, Process 
from utils import write_results
from algorithms import (
    fcfs_scheduling, 
    psjf_scheduling, 
    npsjf_scheduling, 
    rr_scheduling, 
    ppriority_scheduling, 
    nppriority_scheduling
)

# --- Proje Yapılandırması ---

current_file_dir = os.path.dirname(os.path.abspath(__file__)) 
project_root = os.path.abspath(os.path.join(current_file_dir, os.pardir)) 
data_dir = os.path.join(project_root, 'data')
output_dir = os.path.join(project_root, 'output')

case1_data_file = os.path.join(data_dir, 'odev1_case1.txt')
case2_data_file = os.path.join(data_dir, 'odev1_case2.txt')

RR_QUANTUM = 4

ALGORITHMS = {
    'FCFS': fcfs_scheduling,
    'Preemptive SJF': psjf_scheduling,
    'Non-Preemptive SJF': npsjf_scheduling,
    f'Round Robin (Q={RR_QUANTUM})': lambda p: rr_scheduling(p, quantum=RR_QUANTUM),
    'Preemptive Priority': ppriority_scheduling,
    'Non-Preemptive Priority': nppriority_scheduling,
}

# --- Thread Fonksiyonu ---

def run_algorithm(case_name, initial_processes, algo_name, algo_func):
    print(f"[{case_name}] Başlatılıyor: {algo_name}")
    
    try:
        processes_copy = copy.deepcopy(initial_processes)
        
        completed_processes, gantt_chart, metrics = algo_func(processes_copy)
        
        case_output_dir = os.path.join(output_dir, case_name.lower().replace(' ', '_'))
        os.makedirs(case_output_dir, exist_ok=True)
        
        filename = os.path.join(case_output_dir, f"{algo_name.lower().replace(' ', '_').replace('-', '')}_results.txt")
        write_results(filename, f"{algo_name} ({case_name})", completed_processes, gantt_chart, metrics)
        
        print(f"[{case_name}] Tamamlandı: {algo_name}. Sonuçlar kaydedildi: {filename}")
        
    except Exception as e:
        print(f"[{case_name}] HATA {algo_name} çalışırken: {e}")

# --- Ana Çalıştırıcı Fonksiyon ---

def main():
    print(f"Veri Yolu Kontrolü: Data Dir: {data_dir} | Output Dir: {output_dir}")
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)
    
    print("Giriş dosyaları yükleniyor...")
    
    case1_processes = load_processes(case1_data_file)
    case2_processes = load_processes(case2_data_file)
    
    if not case1_processes:
        print(f"Hata: Case 1 ({case1_data_file}) yüklenemedi. Lütfen dosyayı kontrol edin.")
        return
    if not case2_processes:
        print(f"Hata: Case 2 ({case2_data_file}) yüklenemedi. Lütfen dosyayı kontrol edin.")
        return

    print(f"Case 1: {len(case1_processes)} süreç yüklendi. | Case 2: {len(case2_processes)} süreç yüklendi.")
    print("-" * 50)
    
    threads = []
    
    for case_name, processes in [('Case 1', case1_processes), ('Case 2', case2_processes)]:
        for algo_name, algo_func in ALGORITHMS.items():
            t = threading.Thread(target=run_algorithm, 
                                 args=(case_name, processes, algo_name, algo_func))
            threads.append(t)

    print(f"Toplam {len(threads)} iş parçacığı eş zamanlı olarak başlatılıyor...")
    for t in threads:
        t.start()

    for t in threads:
        t.join()
        
    print("-" * 50)
    print("--- TÜM İŞLEMLER TAMAMLANDI ---")
    print("Sonuçlar '/output/case1' ve '/output/case2' dizinlerine kaydedilmiştir.")


if __name__ == "__main__":
    main()