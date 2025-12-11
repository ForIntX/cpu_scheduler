# KULLANICI KILAVUZU: İşlemci Zamanlama Projesi (EBLM341 Ödev 1)

## 1. Giriş

Bu kılavuz, İşletim Sistemleri dersi için hazırlanan CPU Zamanlama Algoritmaları Karşılaştırma Projesi'nin kurulumunu ve çalıştırılmasını adım adım açıklamaktadır. Proje, 6 farklı zamanlama algoritmasını iki farklı süreç yükü (Case 1 ve Case 2) üzerinde eş zamanlı olarak test etmek üzere tasarlanmıştır.

## 2. Sistem Gereksinimleri

* **İşletim Sistemi:** Windows, macOS veya Linux.
* **Programlama Dili:** Python 3.6 veya üzeri.
* **Gerekli Kütüphaneler:** Standart Python kütüphaneleri (os, threading, copy, sys). Ek bir kurulum gerektirmez.

## 3. Kurulum ve Proje Yapısı

1.  **Klonlama/İndirme:** Projenin GitHub deposunu yerel makinenize indirin.
2.  **Dizin Kontrolü:** Proje kök dizininizin aşağıdaki yapıya sahip olduğundan emin olun:

    ```
    /Isletim_Sistemleri_Odev1
    ├── /src
    │   ├── main_scheduler.py
    │   ├── algorithms.py
    │   ├── process.py
    │   └── utils.py
    ├── /data
    │   ├── odev1_case1.txt
    │   └── odev1_case2.txt
    ├── /output  (Program tarafından oluşturulacaktır)
    └── /docs
    ```
3.  **Veri Girişi:** `data` klasörünün içine, projede verilen `odev1_case1.txt` ve `odev1_case2.txt` dosyalarının doğru bir şekilde yerleştirildiğini kontrol edin. Program, parametre olarak uygun herhangi bir CSV formatındaki süreç dosyasını bu dizinde okuyabilir.

## 4. Çalıştırma Talimatları

1.  Terminal veya Komut İstemi'ni açın.
2.  Projenin ana kök dizinine (yani `/odev` klasörüne) gidin.
3.  Aşağıdaki komutu kullanarak ana çalıştırıcı dosyayı başlatın:

    ```bash
    python src/main_scheduler.py
    ```

## 5. Çıktı ve Sonuçlar

Program, çalıştığı süre boyunca konsola ilerleme durumunu (hangi thread'in başladığını ve bittiğini) yazdıracaktır.

* **Çıktı Konumu:** Tüm algoritmaların sonuçları, otomatik olarak **output** klasörünün altına kaydedilecektir:
    * `/output/case1/`
    * `/output/case2/`
* **Çıktı Formatı:** Her algoritma için ayrı bir `.txt` dosyası oluşturulur ve bu dosyalar ödevde istenen 6 metrik bilgisini (Gantt Chart, WT, TT, Throughput, Utilization, Context Switch Count) içerir.

Bu adımlar tamamlandığında, analiz için gereken tüm verileriniz hazır olacaktır.