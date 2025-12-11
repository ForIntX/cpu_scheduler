# 🚀 EBLM341 - İşletim Sistemleri Ödev 1: İşlemci Zamanlama Algoritmaları Karşılaştırması

AD-SOYAD:MUHAMMET BURAK AKKAŞ 
OKUL NO:20232013032

Bu proje, İstanbul Nişantaşı Üniversitesi Bilgisayar Mühendisliği Bölümü EBLM341 İşletim Sistemleri dersi kapsamında hazırlanmıştır. Amaç, farklı süreç yükleri (Case 1 ve Case 2) altında altı temel CPU zamanlama algoritmasının performansını eş zamanlı olarak test etmek ve detaylı metrikler üzerinden analiz etmektir.

## 📚 Algoritmalar

Aşağıdaki 6 CPU zamanlama algoritması uygulanmış ve test edilmiştir:

1.  FCFS (First Come First Served)
2.  Preemptive SJF (Shortest Job First)
3.  Non-Preemptive SJF (Shortest Job First)
4.  Round Robin (Quantum Q=4 birim zaman)
5.  Preemptive Priority Scheduling
6.  Non-Preemptive Priority Scheduling

## ✨ Bonus Özellikler

* **Çoklu İş Parçacığı (Threading):** Tüm algoritma/durum kombinasyonları eş zamanlı olarak ayrı thread'lerde çalıştırılmıştır. 

## 📂 Proje Yapısı

Proje, modüler ve temiz bir yapıya sahiptir.




## 🛠️ Kurulum ve Çalıştırma

### 1. Gereksinimler

Proje, Python 3 ortamında geliştirilmiştir. Ek kütüphane gereksinimi yoktur (yalnızca standart `os`, `threading`, `copy` kullanılır).

### 2. Dosyaları Hazırlama

1.  Projeyi klonlayın veya indirin.

2.  Output klasörü içerisindekileri indirmenize gerek yok, data kısmındaki dosyaları hazır bir şekilde ben ayarladım isterseniz siz tekrardan yeni dosyalar koyabilirsiniz. Ancak dosya isimlerinin aynı olması gerekmektedir. 

3.  Docs kısmında dosyalar hakkında bilgiler bulunmaktadır. O kısımdan yardım alabilirsiniz.

4.  `data` klasörünün içine `odev1_case1.txt` ve `odev1_case2.txt` dosyalarını koyun.


### 3. Çalıştırma

Projenin kök dizininde (yani `src` ve `data` klasörlerinin bulunduğu yerde) terminali açın ve aşağıdaki komutu çalıştırın:

```bash
python3 src/main_scheduler.py


