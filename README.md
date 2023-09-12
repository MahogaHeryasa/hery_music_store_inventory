# Tautan Aplikasi = [hery-music-store-inventory](https://hery-music-store-inventory.adaptable.app/main/)

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.

   1. Membuat sebuah proyek Django baru.
      - Pertama buat virtual environment pada direktori lokal untuk proyek Django
        ```
        python -m venv env
        ```
      - Aktifkan virtual environment dengan perintah
        ```
        env\Scripts\activate.bat
        ```
      - Saya buat berkas `requirements.txt` pada direktori yang sama dan Saya tambahkan beberapa dependencies
      - Saya Pasang dependencies untuk proyek dengan perintah
        ```
        pip install -r requirements.txt
        ```
      - Saya buat proyek Django saya dengan perintah
        ```
        django-admin startproject hery_music_store_inventory .
        ```
      - Untuk keperluan deployment, saya tambahkan  `"*"` untuk `ALLOWED_HOSTS` di `settings.py`
      - Terakhir, saya tambahkan berkas `.gitignore` agar beberapa hal dapat diabaikan GitHub
        
  2. Membuat aplikasi dengan nama `main` pada proyek tersebut.
     - Pada virtual environment, saya jalankan perintah `python manage.py startapp main` untuk membuat aplikasi main pada proyek
     - Saya tambahkan `'main'` pada variabel `INSTALLED_APPS` di `settings.py` yang berada pada direktori proyek
     - Lalu saya tambahkan folder `templates` pada direktori `main`, dan di dalamnya saya buat berkas `main.html` sebagai template html
       
  3. Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`.
     - Pada berkas `urls.py` pada direktori proyek, saya tambahkan `path('main/', include('main.urls')),` pada variabel `urlpatterns`
       
  4. Membuat model pada aplikasi `main` dengan nama `Item`
     - Pada `models.py`, saya tambahkan class `Item` dengan atribut:
       - name
       - date_added
       - price
       - description
       - amount
         
  5. Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
     - Pada `views.py` saya tambahkan fungsi dengan nama `show_main` dengan context `'application_name'`, `name`, dan `class`. lalu saya render context ke `main.html`
     - Pada `main.html` saya buat parameter bebas dengan sintaks `{{  }}` dimana nilai dari konteks akan di oper kedalam parameter bebas tersebut

  6. Membuat sebuah routing pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
     - pada direktori `main`, saya tambahkan berkasa baru `urls.py`, didalamnya saya tambahkan variabel `app_name = 'main'` dan variabel `urlpatterns` yang didalamnya saya tambahkan `path('', show_main, name='show_main'),`

   7. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat.
      - Sebelum melakukan deployment, saya lakukan `add`, `commit`, `push` pada repositori GitHub bernama hery_music_store_inventory
      - Setelah itu saya deploy aplikasi saya ke Adaptable dengan ketentuan template deployment `Python App Template` dan tipe basis data `PostgreSQL`
     
### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
<img src = "C:\Users\mahog\Documents\UI\PBP esai\Bagan.jpg" >
