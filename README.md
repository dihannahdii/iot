# Permainan Simon Says

Implementasi modern dari permainan memori klasik Simon Says dengan sistem high score berbasis ThingSpeak. Proyek ini menggunakan ESP8266 untuk membuat permainan memori yang menarik dengan lampu, suara, dan kemampuan untuk menyimpan dan menampilkan skor tertinggi melalui ThingSpeak.

## Fitur

- Permainan Simon Says klasik dengan 4 tombol dan LED berwarna
- Dua mode permainan:
  - Mode Memori: Mode pemain tunggal di mana Anda harus mengingat dan mengulang urutan
  - Mode Pertarungan: Mode dua pemain di mana pemain bergantian menambahkan ke urutan
- Easter Egg: Mode musik BeeGees tersembunyi
- Umpan balik LED dan suara interaktif
- Mendukung hingga 13 ronde permainan
- Sistem High Score berbasis ThingSpeak:
  - Penyimpanan skor otomatis ke ThingSpeak
  - Visualisasi data real-time
  - Akses skor dari mana saja
  - Grafik dan statistik permainan
  - Tampilan web yang responsif dan modern
  - Mode gelap/terang

## Kebutuhan Perangkat Keras

- ESP8266 (NodeMCU atau board ESP8266 lainnya)
- 4 LED:
  - 1x LED Merah
  - 1x LED Biru
  - 1x LED Hijau
  - 1x LED Kuning
- 4 Tombol Tekan
- 1 Buzzer Piezo
- 4x Resistor 220Ω (untuk LED)
- 4x Resistor 10kΩ (untuk tombol)
- Kabel Jumper
- Papan Breadboard

## Koneksi Pin

```
Koneksi LED:
- LED Merah: Pin D7 (GPIO13)
- LED Hijau: Pin D6 (GPIO12)
- LED Biru: Pin D5 (GPIO11)
- LED Kuning: Pin D4 (GPIO10)

Koneksi Tombol:
- Tombol Merah: Pin D3 (GPIO9)
- Tombol Hijau: Pin D2 (GPIO8)
- Tombol Biru: Pin D1 (GPIO7)
- Tombol Kuning: Pin D0 (GPIO6)

Koneksi Buzzer:
- Buzzer: Pin D5 (GPIO5)
```

## Pengaturan ThingSpeak

1. Buat akun di [ThingSpeak](https://thingspeak.com)
2. Buat channel baru:
   - Klik "New Channel"
   - Beri nama channel (misalnya "Simon Says High Scores")
   - Aktifkan Field 1 untuk menyimpan skor
   - Klik "Save Channel"
3. Dapatkan Channel ID dan API Key:
   - Channel ID ada di URL channel Anda
   - API Key ada di tab "API Keys"
4. Update kode di `Base.c`:
```cpp
#define CHANNEL_ID 2903790  // Channel ID untuk Simon Says High Scores
#define WRITE_API_KEY "4LZKTZ3KQR8GW4C5"  // Write API Key
#define READ_API_KEY "78TO0HZQAU4N7UXJ"   // Read API Key
```

## Pengaturan WiFi

1. Buka file `Base.c`
2. Ubah kredensial WiFi:
```cpp
const char* ssid = "NAMA_WIFI_ANDA";
const char* password = "PASSWORD_WIFI_ANDA";
```

## Fitur ThingSpeak

Setelah ESP8266 terhubung ke WiFi dan ThingSpeak:

1. Skor akan otomatis terkirim ke ThingSpeak setiap kali permainan selesai
2. Anda dapat melihat skor di dashboard ThingSpeak:
   - Grafik skor real-time
   - Statistik permainan
   - Riwayat skor
3. Akses data melalui:
   - Dashboard web ThingSpeak
   - API ThingSpeak
   - Website kustom dengan tampilan modern

## Website Kustom

Proyek ini menyertakan website kustom (`index.html`) untuk menampilkan high score dengan fitur:

1. Tampilan modern dan responsif
2. Grafik skor interaktif
3. Mode gelap/terang
4. Animasi smooth
5. Tombol refresh untuk memperbarui data

Untuk menggunakan website kustom:
1. Buka file `index.html`
2. Ganti `YOUR_CHANNEL_ID` dengan Channel ID ThingSpeak Anda
3. Host website di server web (GitHub Pages, Netlify, dll)
4. Akses website untuk melihat high score

## Petunjuk Pemasangan

1. Pemasangan LED:
   - Hubungkan anoda (kaki panjang) setiap LED melalui resistor 220Ω ke pin ESP8266 yang sesuai
   - Hubungkan semua katoda LED (kaki pendek) ke GND

2. Pemasangan Tombol:
   - Hubungkan satu sisi setiap tombol ke pin ESP8266 yang sesuai
   - Hubungkan sisi lain setiap tombol ke GND
   - Hubungkan resistor pull-up 10kΩ dari setiap pin tombol ke 3.3V

3. Pemasangan Buzzer:
   - Hubungkan kabel positif (merah) buzzer ke pin D5
   - Hubungkan kabel negatif (hitam) ke GND

## Pengaturan Perangkat Lunak

1. Install Arduino IDE dari [arduino.cc](https://www.arduino.cc/en/software)
2. Install library yang diperlukan:
   - ESP8266WiFi
   - ThingSpeak
3. Buka `Base.c` di Arduino IDE
4. Pilih board ESP8266 yang sesuai dari menu Tools > Board
5. Pilih port COM yang benar dari menu Tools > Port
6. Klik tombol Upload untuk memprogram ESP8266

## Mode Permainan

### Mode Memori (Default)
- Tekan tombol apa saja untuk memulai
- Perhatikan dan ingat urutan lampu
- Ulangi urutan dengan menekan tombol dalam urutan yang sama
- Setiap ronde yang berhasil menambahkan satu langkah ke urutan
- Menang dengan menyelesaikan 13 ronde
- Kalah jika membuat kesalahan atau terlalu lama
- Skor akan otomatis dikirim ke ThingSpeak

### Mode Pertarungan
- Tahan tombol hijau saat startup untuk memasuki mode pertarungan
- Pemain bergantian menambahkan satu langkah ke urutan
- Setiap pemain harus mengulang seluruh urutan sebelum menambahkan langkah mereka
- Pemain pertama yang membuat kesalahan kalah

### Mode Easter Egg
- Tahan tombol kuning saat startup untuk mengaktifkan mode BeeGees
- Perhatikan LED menyala berurutan sambil mendengarkan melodi BeeGees

## Pemecahan Masalah

1. LED tidak menyala:
   - Periksa polaritas LED (kaki panjang harus terhubung ke pin ESP8266 melalui resistor)
   - Verifikasi koneksi resistor
   - Coba pin yang berbeda

2. Tombol tidak merespons:
   - Verifikasi koneksi tombol
   - Periksa koneksi resistor pull-up
   - Uji kontinuitas tombol

3. Tidak ada suara:
   - Periksa polaritas buzzer
   - Coba pin yang berbeda
   - Verifikasi buzzer tidak rusak

4. Masalah Koneksi WiFi:
   - Periksa kredensial WiFi
   - Pastikan ESP8266 dalam jangkauan router
   - Restart ESP8266 jika tidak dapat terhubung

5. Masalah ThingSpeak:
   - Periksa Channel ID dan API Key
   - Pastikan ESP8266 terhubung ke internet
   - Periksa Serial Monitor untuk pesan error

## Kontribusi

Silakan kirim masalah dan permintaan peningkatan!

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file LICENSE untuk detailnya.

## Penghargaan

- Kode permainan Simon Says asli oleh SparkFun Electronics
- Dimodifikasi untuk ESP8266 dengan mode permainan yang ditingkatkan dan integrasi ThingSpeak 

## Integrasi dan Pengujian

### Tahap 1: Pengujian Hardware

#### 1.1 Pengujian Komponen Individual

##### Pengujian LED
1. Siapkan program blink sederhana:
```cpp
void setup() {
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
}

void loop() {
  // Test LED Merah
  digitalWrite(LED_RED, HIGH);
  delay(1000);
  digitalWrite(LED_RED, LOW);
  delay(1000);
  
  // Test LED Hijau
  digitalWrite(LED_GREEN, HIGH);
  delay(1000);
  digitalWrite(LED_GREEN, LOW);
  delay(1000);
  
  // Test LED Biru
  digitalWrite(LED_BLUE, HIGH);
  delay(1000);
  digitalWrite(LED_BLUE, LOW);
  delay(1000);
  
  // Test LED Kuning
  digitalWrite(LED_YELLOW, HIGH);
  delay(1000);
  digitalWrite(LED_YELLOW, LOW);
  delay(1000);
}
```

2. Langkah pengujian:
   - Upload program ke ESP8266
   - Pastikan setiap LED menyala dengan intensitas yang sama
   - Verifikasi tidak ada LED yang redup atau terlalu terang
   - Periksa polaritas LED (kaki panjang ke pin, kaki pendek ke GND)
   - Pastikan resistor 220Ω terpasang dengan benar

##### Pengujian Tombol
1. Siapkan program input sederhana:
```cpp
void setup() {
  Serial.begin(115200);
  pinMode(BUTTON_RED, INPUT_PULLUP);
  pinMode(BUTTON_GREEN, INPUT_PULLUP);
  pinMode(BUTTON_BLUE, INPUT_PULLUP);
  pinMode(BUTTON_YELLOW, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(BUTTON_RED) == LOW) Serial.println("Tombol Merah ditekan");
  if (digitalRead(BUTTON_GREEN) == LOW) Serial.println("Tombol Hijau ditekan");
  if (digitalRead(BUTTON_BLUE) == LOW) Serial.println("Tombol Biru ditekan");
  if (digitalRead(BUTTON_YELLOW) == LOW) Serial.println("Tombol Kuning ditekan");
  delay(100);
}
```

2. Langkah pengujian:
   - Upload program ke ESP8266
   - Buka Serial Monitor (115200 baud)
   - Tekan setiap tombol dan verifikasi pesan muncul
   - Periksa tidak ada false trigger
   - Pastikan resistor pull-up 10kΩ terpasang dengan benar
   - Verifikasi debouncing berfungsi

##### Pengujian Buzzer
1. Siapkan program tone sederhana:
```cpp
void setup() {
  pinMode(BUZZER, OUTPUT);
}

void loop() {
  // Test frekuensi berbeda
  tone(BUZZER, 440);  // A4
  delay(1000);
  noTone(BUZZER);
  delay(1000);
  
  tone(BUZZER, 880);  // A5
  delay(1000);
  noTone(BUZZER);
  delay(1000);
}
```

2. Langkah pengujian:
   - Upload program ke ESP8266
   - Verifikasi buzzer menghasilkan suara yang jelas
   - Test berbagai frekuensi untuk memastikan range suara
   - Periksa polaritas buzzer (kabel merah ke pin, hitam ke GND)
   - Pastikan volume suara konsisten

#### 1.2 Pengujian Koneksi

##### Pengujian dengan Multimeter
1. Siapkan multimeter digital
2. Langkah pengujian:
   - Ukur tegangan pada setiap pin LED (harus 3.3V saat HIGH)
   - Verifikasi tegangan GND (harus 0V)
   - Ukur resistansi resistor LED (220Ω ±5%)
   - Ukur resistansi pull-up resistor (10kΩ ±5%)
   - Periksa kontinuitas semua koneksi

##### Pengujian Short Circuit
1. Langkah pengujian:
   - Matikan power ESP8266
   - Ukur resistansi antara pin yang berdekatan
   - Verifikasi tidak ada koneksi yang tidak diinginkan
   - Periksa isolasi antar komponen
   - Pastikan tidak ada solder yang berlebih

### Tahap 2: Pengujian Game Logic

#### 2.1 Pengujian Mode Memori

##### Pengujian Urutan LED
1. Langkah pengujian:
   - Jalankan permainan dalam mode memori
   - Verifikasi urutan LED menyala dengan benar
   - Pastikan interval waktu antar LED konsisten
   - Periksa transisi LED smooth
   - Test dengan berbagai panjang urutan

##### Pengujian Input Tombol
1. Langkah pengujian:
   - Test respons tombol terhadap input
   - Verifikasi feedback suara untuk setiap tombol
   - Pastikan tidak ada false input
   - Test batas waktu input (3 detik)
   - Verifikasi debouncing berfungsi

##### Pengujian Skor
1. Langkah pengujian:
   - Mainkan beberapa ronde permainan
   - Verifikasi skor bertambah dengan benar
   - Test batas maksimum skor (13 ronde)
   - Pastikan skor reset saat game over
   - Verifikasi skor terkirim ke ThingSpeak

#### 2.2 Pengujian Mode Pertarungan

##### Pengujian Pergantian Pemain
1. Langkah pengujian:
   - Aktifkan mode pertarungan
   - Test pergantian pemain berjalan lancar
   - Verifikasi urutan bertambah dengan benar
   - Pastikan setiap pemain mendapat giliran
   - Test kondisi kemenangan/kekalahan

##### Pengujian Integrasi ThingSpeak
1. Langkah pengujian:
   - Mainkan mode pertarungan
   - Verifikasi skor terkirim ke ThingSpeak
   - Periksa format data yang dikirim
   - Test pengiriman data saat WiFi terputus
   - Verifikasi data tersimpan dengan benar

#### 2.3 Pengujian Mode Easter Egg

##### Pengujian Aktivasi
1. Langkah pengujian:
   - Tahan tombol kuning saat startup
   - Verifikasi mode BeeGees aktif
   - Test urutan LED dan musik
   - Pastikan kembali ke mode normal
   - Verifikasi tidak ada bug saat mode switch

### Tahap 3: Integrasi WiFi dan ThingSpeak

#### 3.1 Pengujian Koneksi WiFi

##### Pengujian Koneksi Awal
1. Langkah pengujian:
   - Setup kredensial WiFi
   - Verifikasi koneksi berhasil
   - Test reconnect otomatis
   - Monitor penggunaan memori
   - Verifikasi stabilitas koneksi

##### Pengujian Stabilitas
1. Langkah pengujian:
   - Test koneksi dalam jangka panjang
   - Verifikasi tidak ada memory leak
   - Test under load conditions
   - Monitor packet loss
   - Verifikasi QoS

#### 3.2 Pengujian ThingSpeak

##### Pengujian Pengiriman Data
1. Langkah pengujian:
   - Setup channel ThingSpeak
   - Verifikasi API key valid
   - Test pengiriman data
   - Monitor rate limit
   - Verifikasi format data

##### Pengujian Pembacaan Data
1. Langkah pengujian:
   - Test pembacaan data dari channel
   - Verifikasi timestamp
   - Test query data historis
   - Monitor latency
   - Verifikasi konsistensi data

#### 3.3 Pengujian Website Kustom

##### Pengujian UI/UX
1. Langkah pengujian:
   - Test di berbagai browser
   - Verifikasi responsivitas
   - Test mode gelap/terang
   - Verifikasi animasi smooth
   - Test loading state

##### Pengujian Data Real-time
1. Langkah pengujian:
   - Test pembaruan data otomatis
   - Verifikasi grafik update
   - Test filter data
   - Monitor performa
   - Verifikasi konsistensi

### Tahap 4: Pengujian Sistem Terintegrasi

#### 4.1 Pengujian End-to-End

##### Pengujian Alur Lengkap
1. Langkah pengujian:
   - Test alur permainan lengkap
   - Verifikasi skor tersimpan
   - Test pengiriman ke ThingSpeak
   - Verifikasi tampilan web
   - Test recovery dari error

##### Pengujian Performa
1. Langkah pengujian:
   - Monitor penggunaan memori
   - Test latency sistem
   - Verifikasi stabilitas
   - Test under load
   - Monitor resource usage

#### 4.2 Pengujian Keandalan

##### Pengujian Error Handling
1. Langkah pengujian:
   - Test WiFi terputus
   - Verifikasi penyimpanan lokal
   - Test reconnect
   - Monitor error log
   - Verifikasi recovery

##### Pengujian Batas Sistem
1. Langkah pengujian:
   - Test rate limit ThingSpeak
   - Verifikasi memory limit
   - Test concurrent connections
   - Monitor system stability
   - Verifikasi error handling

### Metrik Pengujian

#### 4.3 Metrik Performa
1. Hardware:
   - LED response time: < 50ms
   - Button response time: < 100ms
   - Sound latency: < 200ms
   - Power consumption: < 500mA

2. Software:
   - Boot time: < 5s
   - WiFi connection: < 10s
   - Data transmission: < 2s
   - UI update: < 1s

3. Reliability:
   - Uptime: > 99%
   - Data transmission rate: > 95%
   - Score accuracy: 100%
   - Recovery rate: > 90%

### 4.4 Dokumentasi Pengujian

#### Format Dokumentasi
1. Hasil Pengujian:
   - Tanggal dan waktu
   - Tester
   - Komponen yang diuji
   - Hasil pengujian
   - Status (Pass/Fail)

2. Bug Report:
   - ID Bug
   - Deskripsi
   - Steps to reproduce
   - Expected behavior
   - Actual behavior

3. Log Pengujian:
   - Timestamp
   - Event
   - Error message
   - System state
   - Action taken

4. Troubleshooting Guide:
   - Problem description
   - Possible causes
   - Solution steps
   - Prevention measures
   - Reference links 