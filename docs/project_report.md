# PROJE RAPORU: İşlemci Zamanlama Algoritmaları Analizi (EBLM341 Ödev 1)

## 1. Giriş ve Metodoloji

### 1.1. Amaç
[cite_start]Bu rapor, EBLM341 İşletim Sistemleri dersi Ödev 1 kapsamında, 6 temel CPU zamanlama algoritmasının iki farklı süreç yükü (Case 1 ve Case 2) altındaki performansını ölçmek ve elde edilen metrikleri karşılaştırmalı olarak analiz etmeyi amaçlamaktadır[cite: 10].

### 1.2. Algoritmalar ve Parametreler
Projede uygulanan algoritmalar ve temel parametreler şunlardır:
* [cite_start]**Algoritmalar:** FCFS (First Come First Served) [cite: 11][cite_start], Preemptive SJF (Shortest Job First) [cite: 12][cite_start], Non-Preemptive SJF (Shortest Job First) [cite: 13][cite_start], Round Robin [cite: 14][cite_start], Preemptive Priority Scheduling [cite: 15][cite_start], Non-Preemptive Priority Scheduling[cite: 16].
* [cite_start]**Context Switch Time:** $0.001$ birim zaman[cite: 27].
* **Round Robin Quantum (Q):** 4 birim zaman.

---

## 2. Case 1 Analizi (odev1_case1.txt)

### 2.1. Süreç Yükü Özeti
Case 1, 200 adet süreçten oluşmaktadır. Varış zamanları (AT) 0'dan başlayıp ikişer ikişer artmaktadır. CPU Burst Time (BT) değerleri ise 1'den 20'ye kadar tekrar eden döngüdedir. Bu, Burst Time varyasyonunun geniş olduğu dengeli bir yük durumudur.

### 2.2. Zaman Tabloları (Gantt Chart)

| Algoritma | Örnek Zaman Tablosu (İlk 6 Süreç) |
| :--- | :--- |
| **FCFS** | [0]--P001--[1] [1]--IDLE--[2] [2]--P002--[4] [4]--P003--[7] [7]--P004--[11] [11]--P005--[16] |
| **PSJF** | [0]--P001--[1] [1]--IDLE--[2] [2]--P002--[4] [4]--P003--[7] [7]--P004--[11] [11]--P005--[16] |
| **NPSJF** | [0]--P001--[1] [1]--IDLE--[2] [2]--P002--[4] [4]--P003--[7] [7]--P004--[11] [11]--P005--[16] |
| **RR (Q=4)** | [0]--P001--[1] [1]--IDLE--[2] [2]--P002--[4] [4]--P003--[7] [7]--P004--[11] [11]--P005--[15] |
| **PP** | [0]--P001--[1] [1]--IDLE--[2] [2]--P002--[4] [4]--P003--[6] [6]--P004--[10] [10]--P005--[12] |
| **NPP** | [0]--P001--[1] [1]--IDLE--[2] [2]--P002--[4] [4]--P003--[7] [7]--P004--[11] [11]--P005--[16] |

### 2.3. Performans Metrikleri Karşılaştırması

Aşağıdaki tabloda, Case 1 için tüm algoritmaların temel performans metrikleri karşılaştırılmıştır.

| Metrik | FCFS | PSJF | NPSJF | RR (Q=4) | PP | NPP |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Ort. Bekleme Süresi (ms)** | 813.495 | **537.005** | 537.425 | 1091.700 | 833.630 | 824.770 |
| **Ort. Tamamlanma Süresi (ms)** | 823.995 | **547.505** | 547.925 | 1102.200 | 844.130 | 835.270 |
| **Throughput (T=200)** | 19 | **42** | **42** | 14 | 20 | 21 |
| **CPU Verimliliği (%)** | **99.94%** | **99.94%** | **99.94%** | 99.92% | **99.94%** | **99.94%** |
| **Toplam Bağlam Değiştirme** | 198 | 211 | 198 | **598** | 200 | 198 |

### 2.4. Yorum ve Değerlendirme (Case 1)

* **Yanıt Süresi ve SJF:** Preemptive SJF (PSJF) ve Non-Preemptive SJF (NPSJF), $537$ ms civarındaki ortalama bekleme süreleriyle en iyi performansı sağlamıştır. Bu, SJF'nin kısa işleri hemen bitirerek sistemdeki ortalama bekleme süresini etkin bir şekilde düşürmesiyle ilişkilidir. 
* **Verimlilik ve Non-Preemptive:** FCFS, NPSJF, NPP ve PSJF gibi düşük Bağlam Değiştirme (Context Switch) sayısına sahip algoritmalar, %99.94 ile en yüksek CPU Verimliliğine ulaşmıştır. Bu durum, Bağlam Değiştirme Yükünün (0.001 birim zaman) etkisinin minimum düzeyde kalmasından kaynaklanmaktadır.
* **Round Robin Yükü:** Round Robin (RR), 598 ile açık ara en yüksek Bağlam Değiştirme Sayısına sahiptir. Bu yüksek yük, RR'nin CPU Verimliliğini (%99.92) düşürmüş ve ortalama bekleme süresini ($1091$ ms) diğer algoritmalara göre en kötü seviyeye çekmiştir.

---

## 3. Case 2 Analizi (odev1\_case2.txt)

### 3.1. Süreç Yükü Özeti
Case 2, 100 adet süreçten oluşmaktadır. CPU Burst Time (BT) değerleri, Case 1'e göre daha uzun ve değişken (örneğin $4, 7, 10, 13, 16, 19, 2, 5, \dots$) bir desende artmaktadır. Bu yük, süreçlerin genel olarak daha fazla CPU süresi gerektirdiği bir durumu temsil eder.

### 3.2. Performans Metrikleri Karşılaştırması

Aşağıdaki tabloda, Case 2 için tüm algoritmaların temel performans metrikleri karşılaştırılmıştır.

| Metrik | FCFS | PSJF | NPSJF | RR (Q=4) | PP | NPP |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Ort. Bekleme Süresi (ms)** | 418.000 | **267.860** | 268.390 | 550.870 | 411.390 | 409.630 |
| **Ort. Tamamlanma Süresi (ms)** | 428.500 | **278.360** | 278.890 | 561.370 | 421.890 | 420.130 |
| **Throughput (T=200)** | 18 | **42** | **42** | 11 | 19 | 19 |
| **CPU Verimliliği (%)** | **99.99%** | 99.99% | 99.99% | 99.97% | 99.99% | **99.99%** |
| **Toplam Bağlam Değiştirme** | 99 | 110 | 99 | **299** | 100 | 99 |

### 3.3. Yorum ve Değerlendirme (Case 2)

* **En İyi Performans (Bekleme/Tamamlanma Süresi):** Case 2'de de en iyi ortalama bekleme ve tamamlanma süreleri (**267.860 ms**), **Preemptive SJF (PSJF)** tarafından elde edilmiştir. Non-Preemptive SJF (NPSJF) ise çok yakın bir ikinci sıradadır. Bu, SJF algoritmalarının, Burst Time deseninden bağımsız olarak, kuyruktaki en kısa kalan işi sürekli önceliklendirerek etkinliğini kanıtladığını gösterir.
* **Verimlilik ve Non-Preemptive:** FCFS, NPSJF ve Non-Preemptive Priority (NPP) algoritmaları, sadece 99 Context Switch Sayısı ile **%99.99** gibi mükemmel bir CPU Verimliliği sağlamıştır. Bu, uzun BT'li süreçlerin kesintisiz çalışmasının Overhead'i minimumda tuttuğunu gösterir.
* **Round Robin Yükü:** Round Robin (RR), Case 1'e benzer şekilde, 299 ile en yüksek Bağlam Değiştirme Sayısına sahiptir ve en kötü ortalama bekleme süresini (550.870 ms) vermiştir. Case 2'nin daha uzun BT'leri, $Q=4$ ile sürekli kesme yapılmasını gerektirdiği için Threading Overhead'i artırmıştır.
* **Açlık (Starvation):** Öncelik (Priority) algoritmaları incelendiğinde, süreçlerin düzenli dağılımı sayesinde Açlık riski yönetilmiştir. Ancak Non-Preemptive Priority (NPP) algoritmasında, uzun süreli düşük öncelikli bir işin başlaması ve kesilememesi, yeni gelen yüksek öncelikli işlerin beklemesine neden olarak verimlilik kaybına yol açabilir.

---

## 4. Bonus ve Sonuç

### 4.1. Çoklu İş Parçacığı (Threading) Uygulaması 
[cite_start]Proje, altı algoritmanın Case 1 ve Case 2 için toplamda 12 farklı testini Python'ın `threading` kütüphanesi ile eş zamanlı olarak yürütmüştür[cite: 28]. Bu yaklaşım, test süresini önemli ölçüde kısaltmış ve süreçler arasında tam bağımsızlık (deepcopy kullanılarak) sağlanmıştır.


### 4.2. Genel Sonuç

Genel olarak, **Preemptive SJF** algoritmasının ortalama bekleme ve tamamlanma süreleri açısından en iyi performansı gösterdiği, buna karşın **FCFS** ve **Non-Preemptive SJF**'nin en yüksek CPU verimliliğine sahip olduğu gözlemlenmiştir. Round Robin (Q=4) algoritması, yüksek kesme sayısı nedeniyle en kötü ortalama bekleme süresi performansını sergilemiştir. Özetle, en hızlı yanıt (düşük bekleme süresi) için **SJF**, en düşük sistem yükü (yüksek verimlilik) için ise **Non-Preemptive** yöntemler tercih edilmelidir.