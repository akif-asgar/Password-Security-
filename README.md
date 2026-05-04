git clone https://github.com/istifadəçi-adınız/cyber-security-lab.git
    cd cyber-security-lab
    ```

2.  **Lazımi kitabxanaları quraşdırın:**
    ```bash
    pip install django bcrypt
    ```

3.  **Verilənlər bazasını miqrasiya edin:**
    ```bash
    python manage.py migrate
    ```

4.  **Serveri başladın:**
    ```bash
    python manage.pyLayihən üçün peşəkar, texniki və vizual olaraq cəlbedici bir **README.md** faylı hazırladım. Bu sənəd həm layihənin məqsədini izah edir, həm də quraşdırılma qaydalarını göstərir.

---

# 🔬 CyberGuard Security Lab | Sınaq Paneli

**CyberGuard Security Lab**, müxtəlif kriptoqrafik heşləmə (hashing) metodlarının təhlükəsizlik səviyyəsini vizual olaraq simulyasiya edən interaktiv laboratoriya layihəsidir. Bu panel vasitəsilə istifadəçilər parolların brute-force hücumlarına qarşı dayanıqlığını və alqoritmlər arasındakı fərqləri öyrənə bilərlər.

## 🚀 Xüsusiyyətlər

*   **Çoxsaylı Alqoritmlər:** Plain Text, SHA-256, Salted SHA-256 və Bcrypt dəstəyi.
*   **Canlı Terminal Simulyasiyası:** Hücum prosesini izləmək üçün interaktiv terminal interfeysi.
*   **Vulnerability Score (Zəiflik Balı):** Parolun mürəkkəbliyi və seçilmiş metodun gücü əsasında dinamik uğur faizi hesablama.
*   **Müdafiə Tərəzisi:** Sistem tərəfindən təmin edilən qorunma səviyyəsinin vizual qrafiki.
*   **Real-time Hesablama:** Təxmini qırılma vaxtının (Time-to-crack) analizi.

## 🛠️ Texnologiya Steki

*   **Backend:** Python (Django)
*   **Frontend:** HTML5, Tailwind CSS, JavaScript
*   **Kriptoqrafiya:** `bcrypt`, `hashlib` kitabxanaları
*   **Dizayn:** Glassmorphism UI & Cyberpunk Aesthetics

## 📦 Quraşdırılma

Layihəni lokal maşınınızda işə salmaq üçün aşağıdakı addımları izləyin:

1.  **Repozitoriyanı klonlayın:**
    ```bash
    git clone [https://github.com/istifadəçi-adınız/cyber-security-lab.git](https://github.com/istifadəçi-adınız/cyber-security-lab.git)
    cd cyber-security-lab
    ```

2.  **Lazımi kitabxanaları quraşdırın:**
    ```bash
    pip install django bcrypt
    ```

3.  **Verilənlər bazasını miqrasiya edin:**
    ```bash
    python manage.py migrate
    ```

4.  **Serveri başladın:**
    ```bash
    python manage.py runserver
    ```

5.  **Brauzerdə açın:** `http://127.0.0.1:8000/lab/Layihən üçün peşəkar, texniki və vizual olaraq cəlbedici bir **README.md** faylı hazırladım. Bu sənəd həm layihənin məqsədini izah edir, həm də quraşdırılma qaydalarını göstərir.

---

# 🔬 CyberGuard Security Lab | Sınaq Paneli

**CyberGuard Security Lab**, müxtəlif kriptoqrafik heşləmə (hashing) metodlarının təhlükəsizlik səviyyəsini vizual olaraq simulyasiya edən interaktiv laboratoriya layihəsidir. Bu panel vasitəsilə istifadəçilər parolların brute-force hücumlarına qarşı dayanıqlığını və alqoritmlər arasındakı fərqləri öyrənə bilərlər.

## 🚀 Xüsusiyyətlər

*   **Çoxsaylı Alqoritmlər:** Plain Text, SHA-256, Salted SHA-256 və Bcrypt dəstəyi.
*   **Canlı Terminal Simulyasiyası:** Hücum prosesini izləmək üçün interaktiv terminal interfeysi.
*   **Vulnerability Score (Zəiflik Balı):** Parolun mürəkkəbliyi və seçilmiş metodun gücü əsasında dinamik uğur faizi hesablama.
*   **Müdafiə Tərəzisi:** Sistem tərəfindən təmin edilən qorunma səviyyəsinin vizual qrafiki.
*   **Real-time Hesablama:** Təxmini qırılma vaxtının (Time-to-crack) analizi.

## 🛠️ Texnologiya Steki

*   **Backend:** Python (Django)
*   **Frontend:** HTML5, Tailwind CSS, JavaScript
*   **Kriptoqrafiya:** `bcrypt`, `hashlib` kitabxanaları
*   **Dizayn:** Glassmorphism UI & Cyberpunk Aesthetics

## 📦 Quraşdırılma

Layihəni lokal maşınınızda işə salmaq üçün aşağıdakı addımları izləyin:

1.  **Repozitoriyanı klonlayın:**
    ```bash
    git clone [https://github.com/istifadəçi-adınız/cyber-security-lab.git](https://github.com/istifadəçi-adınız/cyber-security-lab.git)
    cd cyber-security-lab
    ```

2.  **Lazımi kitabxanaları quraşdırın:**
    ```bash
    pip install django bcrypt
    ```

3.  **Verilənlər bazasını miqrasiya edin:**
    ```bash
    python manage.py migrate
    ```

4.  **Serveri başladın:**
    ```bash
    python manage.py runserver
    ```

5.  **Brauzerdə açın:** `http://127.0.0.1:8000/lab/`

## 🖥️ İstifadə Qaydası

1.  **Hədəf Parol:** Yoxlamaq istədiyiniz parolu daxil edin.
2.  **Metod Seçimi:** Zəifdən (Plain) güclüyə (Bcrypt) doğru metodlardan birini seçin.
3.  **Simulyasiya:** "Launch Simulation" düyməsinə klikləyərək terminalı izləyin.
4.  **Analiz:** Sağ paneldə yaranan **Hücumun Uğur Şansı** və **Müdafiə Skoru** məlumatlarını təhlil edin.

## ⚠️ Təhlükəsizlik Xəbərdarlığı

Bu layihə yalnız **tədris və tədqiqat** məqsədləri üçün hazırlanmışdır. Real dünya tətbiqlərində həmişə **Bcrypt** və ya **Argon2** kimi müasir və yavaş heşləmə metodlarından istifadə etmək tövsiyə olunur.

---

### Müəllif
**Gemini Collaboration** - *Security Lab Project 2026*

---

> **Qeyd:** Bu `README.md` faylını GitHub-a yükləyərkən layihənizin skrinşotlarını əlavə etmək üçün `![Screen](link)` formatından istifadə edə bilərsiniz.