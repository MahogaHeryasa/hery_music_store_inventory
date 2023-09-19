# Tugas 2

## Tautan Aplikasi = [hery-music-store-inventory](https://hery-music-store-inventory.adaptable.app/main/)

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
![Bagan](https://github.com/MahogaHeryasa/hery_music_strore_inventory/assets/124902537/1a5949be-60ac-4669-8f0f-2d8f80af8d41)

### 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment digunakan untuk menggisolasi ketergantungan dan kebutuhan library suatu proyek. Virtual environment memungkinkan suatu proyek menggunakan suatu versi Django dan suatu proyek lain menggunakan versi Django yang lain. Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun semua proyek yang ada hanya akan menggunakan versi Django tertinggi sehingga tidak terdapat isolasi untuk masing-masing proyek.    

### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

- MVC: Arsitektur yang menggunakan `Model` sebagai penggelola data dan pengghubung dengan database, `View` menampilkan response berdasarkan input pengguna, `Controller` sebagai penerima input dan komunikator antara view dan model
- MVT: Arsitektur yang menggunakan `Model` sebagai penggelola data dan pengghubung dengan database, `View` yang menampilkan response berdasarkan data pada database dan ditampilkan melalui template html, `Template` Template HTML yang berfungsi sebagai tampilan untuk user
- MVVM: Arsitektur yang menggunakan `Model` sebagai penggelola data dan pengghubung dengan database, `View` yang menampilkan response, `ViewModel` sebagai penggubung langsung antara model dan view. ViewModel terdiri dair Model yang diubah menjadi View

Perbasarkan penjelasan diatas, perbedaan antara ketiganya adalah MVC berfokus pada pengendalian alur kerja aplikasi, MVT memiliki view yang berperan lebih sebagai pengendali tampilan, sementara logika bisnisnya diatur di Model dan Template, dan MVVM memiliki sistem yang mengikat data dengan tampilan secara langsung. 

# Tugas 3

### 1. Apa perbedaan antara form POST dan form GET dalam Django?

Form POST digunakan ketika permintaan pada form akan merubah kondisi sistem server, POST dapat merubah database pada server secara langsung. implementasi form POST lebih aman dibandingkan form GET karena nilai variabel data tidak ditampilkan di URL. Sementara form GET membungkus data pada form dengan sistem 'key & value' lalu data tersebut dimasukkan kealam sebuah URL, sehingga implementasinya kurang aman dibandingkan form POST karena semua orang dapat mengakses URL tersebut. Form GET hanya mengembalikan suatu data namun tidak merubah kondisi sistem server dan tidak ada data yang masuk database.

### 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

   1. Membuat input `form` untuk menambahkan objek model pada app sebelumnya.
      - Pertama saya buat file `forms.py` pada direktori `main` sebagai struktur form
      - Pada `forms.py` saya buat class `ItemForm`  
        ``` python
         class ItemForm(ModelForm):
             class Meta:
                 model = Item
                 fields = ["name", "price", "description", "amount"]
        ```
        class ini digunakan sebagai struktur yang menyambungkan model dan field model yang akan digunakan untuk menyimpan data dari form
      - Saya buat berkas `create_item.html` pada direktori `main/templates` sebagai template html yang menunjukkan form
      - Pada `views.py` saya tambahkan fungsi `create_item`
        ``` python
        def create_item(request):
             form = ItemForm(request.POST or None)
   
             if form.is_valid() and request.method == "POST":
                 form.save()
                 return HttpResponseRedirect(reverse('main:show_main'))
   
             context = {'form': form}
             return render(request, "create_item.html", context)
        ```
        fungsi ini digunakan untuk membuat form yang ditunjukkan ke client melalui `create_item.html` dan menyimpan data dari form tersebut
      - pada fungsi `show main` saya tambahkan `items` pada `context` dimana `items = Item.objects.all()`, untuk menunjukkan items di database yang telah di add di form
      - pada `main.html` saya tambahkan tabel yang menunjukkan seluruh item di database
        
   2. Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
      - fungsi HTML pada `views.py` adalah fungsi `show_main` yang sudah dibuat sebelumnya
      - fungsi XML pada `views.py` adalah fungsi `show_xml` yang saya tambahkan
        ``` python
        def show_xml(request):
          data = Item.objects.all()
          return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        ```
        fungsi ini mengambil seluruh item dan mengembalikannya dalam format xml
      - fungsi JSON pada `views.py` adalah fungsi `show_json` yang saya tambahkan
        ``` python
         def show_json(request):
             data = Item.objects.all()
             return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        ```
        fungsi ini mengambil seluruh item dan mengembalikannya dalam format json
      - fungsi XML by ID pada `views.py` adalah fungsi `show_xml_by_id` yang saya tambahkan
        ``` python
         def show_xml_by_id(request, id):
             data = Item.objects.filter(pk=id)
             return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        ```
        fungsi ini mengambil salah satu item berdasarkan id nya dan mengembalikannya dalam format xml
      - fungsi JSON by ID pada `views.py` adalah fungsi `show_json_by_id` yang saya tambahkan
        ``` python
         def show_json_by_id(request, id):
             data = Item.objects.filter(pk=id)
             return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        ```
        fungsi ini mengambil salah satu item berdasarkan id nya dan mengembalikannya dalam format json
        
   3. Membuat routing URL untuk masing-masing `views` yang telah ditambahkan.
      - pada `urls.py` yang berada di direktori `main` saya import semua jenis `views` yang telah dibuat
        ``` python
        from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
        ```
      - saya tambahkan path url pada list `urlpatterns` dari semua `views` (kecuali show_main yang telah ditambahkan sebelumnya)
        ``` python
        ...
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'), 
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
        ...
        ```

        
         
