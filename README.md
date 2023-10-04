## Tautan Aplikasi = [hery-music-store-inventory](https://hery-music-store-inventory.adaptable.app/main/)

<details>
<summary><b><h1>Tugas 2</h1></b></summary>

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

</details>

<details>
<summary><b><h1>Tugas 3</h1></b></summary>

### 1. Apa perbedaan antara form POST dan form GET dalam Django?

Form POST digunakan ketika permintaan pada form akan merubah kondisi sistem server, POST dapat merubah database pada server secara langsung. implementasi form POST lebih aman dibandingkan form GET karena nilai variabel data tidak ditampilkan di URL. Sementara form GET membungkus data pada form dengan sistem 'key & value' lalu data tersebut dimasukkan kealam sebuah URL, sehingga implementasinya kurang aman dibandingkan form POST karena semua orang dapat mengakses URL tersebut. Form GET hanya mengembalikan suatu data namun tidak merubah kondisi sistem server dan tidak ada data yang masuk database.

### 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

HTML adalah pilar utama dalam pengembangan platform, HTML digunakan sebagai struktur suatu halaman pada web, sehingga pengiriman data juga tergabung dalam struktur tersebut. Sementara, JSON dan XML adalah representasi data yang digunakan dalam pertukaran data antaraplikasi. JSON mengrimkan data dengan sistem 'key & value', mudah di baca, dan cocok untuk data yang ringan. XML mengirimkan data dengan sistem terstruktur seperti *tree*, dimulai dari *root* dan masuk ke *branch*, cocok untuk data yang terstruktur dan *self-describing*. 

### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena memiliki format yang ringan dan efisien, mudah dipahami oleh manusia dan mesin, independen dari bahasa pemrograman, memiliki kompabilitas dengan JavaScript yang juga mempermudah penulisan dan pembacaan data, serta tidak memerlukan tag seperti pada format XML. 

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
### Screenshot dari hasil akses URL pada Postman

![messageImage_1695143950878](https://github.com/MahogaHeryasa/hery_music_strore_inventory/assets/124902537/622c16d3-01b2-4dae-bcef-7409b8c0b1a9)

![messageImage_1695143978588](https://github.com/MahogaHeryasa/hery_music_strore_inventory/assets/124902537/1b65f895-96b2-429d-b2f7-4bf606ba6a77)

![messageImage_1695144006197](https://github.com/MahogaHeryasa/hery_music_strore_inventory/assets/124902537/7351f0db-5987-4004-97c9-3d6f1f206fcc)

![messageImage_1695144098125](https://github.com/MahogaHeryasa/hery_music_strore_inventory/assets/124902537/67a10bf9-98bc-40a3-b39c-43572b4a8b6a)

![messageImage_1695144073686](https://github.com/MahogaHeryasa/hery_music_strore_inventory/assets/124902537/fd197266-eea5-4ddb-8680-2fb1f8617fb0)

</details>

<details>
<summary><b><h1>Tugas 4</h1></b></summary>

### 1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
`UserCreationForm` adalah modul *build-in* pada Django yang bertindak sebagai form untuk membuat akun user baru pada aplikasi kita. for ini memiliki tiga `fields`, username, password1, dan password2(Digunakan untuk mengkonfirmasi password). Beberapa kelebihan `UserCreationForm` diantaranya, mudah digunakan karena hanya perlu mengimpor dan mengimplementasikkannya pada method di views.py, validasi input sudah dibuat secara otomatis dari `UserCreationForm`, serta mudah diintegrasikan dengan model `user` bawaan Django. Namun, `UserCreationForm` juga memiliki kekurangan diantaranya, tampilan form yang sangat sederhana sehingga kurangnya sentuhan personalisasi dari segi design, sistem keamanan dan autentikasi bawaan `UserCreationForm` yang kurang, serta kurangnya fungsionalitas seperti verivikasi email yang memerlukan kustomisasi yang kompleks sehingga mematahkan fungsi awal `UserCreationForm` yang seharusnya memudahkan.

### 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
   - Autentikasi adalah proses verifikasi kesesuaian pengguna dan indetitas pengguna yang mereka klaim sebagai kebenaran identitas mereka.
   - Otorisasi adalah pembatasan terhadap hal yang boleh dan tidak boleh dilakukan di aplikasi oleh user yang telah ter-autentikasi.

Kedua hal ini penting karena dengan autentikasi dan otorisasi keamanan privasi data pengguna aplikasi kita terjaga dan  sistem aplikasi kita terjaga dengan aman dengan adanya batasan user. 

### 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookies adalah kumpulan data yang berisi rekam jejak dan aktivitas user ketika user menelusuri sebuah web. Cookies diterima komputer dari sebuah situs dan dikirimakan kembali ke situs yang dikunjungi sehingga *activity, preferences, login information* user dapat diingat sebuah web. Django menangani cookies secara otomatis. Ketika user menyimpan atau mengambil data dari suatu sesi web, Django akan menghasilkan cookie sesi yang sesuai dan mengirimkannya ke user.

### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Secara default, penggunaan cookies aman-aman saja jika cookies digunakan untuk menyimpan data user yang tidak rahasia, namun masih terdapat beberapa resiko potensial yang harus diwaspadai diantaranya, 
 - Session Hijacking: ketika cookies sesi dicuri oleh penyerang dan penyerang tersebut dapat dengan sah menjadi pengguna yang memiliki cookies sesi tersebut, penyerang dapat mengambil serta mengubah data pengguna didalam aplikasi.
 - Cookies Poisoning: ketika penyerang mencoba meracuni cookie pengguna dengan data yang tidak sah atau berbahaya.
 - Autauthentication bypass: user dapat menggunakan cookies untuk menembus otoritas aplikasi kita
 - Man-in-the-Middle (MITM) Attacks: serangan dari seorang penyerang yang berinteraksi diantara aplikasi dan user, penyerang bisa mengambil cookie saat berkomunikasi dengan server dan mengambil data privasi user.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.

   1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
      - Pertama, saya *import* beberapa method dan class untuk pembuatan form registerasi dan login serta fungsi logout
        ``` python
        from django.shortcuts import redirect
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib import messages
        from django.contrib.auth import authenticate, login, logout
        from django.contrib.auth.decorators import login_required  
        ```
      - Saya buat fungsi `register`, `login_user`, `logout_user` pada berkas `views.py`
         - fungsi `register` akan menerima user baru dengan menggunakan `UserCreationForm` dan menyimpannya pada database
          ``` python
          def register(request):
             form = UserCreationForm()

          if request.method == "POST":
              form = UserCreationForm(request.POST)
              if form.is_valid():
                  form.save()
                  messages.success(request, 'Your account has been successfully created!')
                  return redirect('main:login')
             context = {'form':form}
             return render(request, 'register.html', context)
          ```
          - fungsi `login_user` akan menerima input username dan password dan akan dicocokan dengan user pada data base dengan method `authenticate`
            ``` python
            def login_user(request):
                if request.method == 'POST':
                  username = request.POST.get('username')
                  password = request.POST.get('password')
                  user = authenticate(request, username=username, password=password)
                  if user is not None:
                     login(request, user)
                     return redirect('main:show_main')
                 else:
                     messages.info(request, 'Sorry, incorrect username or password. Please try again.')
                context = {}
                return render(request, 'login.html', context)
            ```
          - fungsi `logout_user` akan me-*logout* user yang berada pada server dan melakukan *redirect* ke halaman login kembali
            ``` python
            def logout_user(request):
                logout(request)
                return redirect('main:login')
            ```
      - Saya buat template html `register.html` dan `login.html` pada direktori `main\templates` sebagai tampilan form register dan login serta tombol `logout` pada `main.html`
      - Saya *import* fungsi-fungsi diatas pada `urls.py` untuk melakukan routing
        ``` python
        from main.views import ... register, login_user, logout_user
        ```
      - Saya tambahkan path url pada list `urlpatterns`
        ``` python
        ...
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        ...
        ```    
   2. Menghubungkan model `Item` dengan `User`.
      - Pertama, saya *import* class User untuk menyambungkan user pada models
        ``` python
        from django.contrib.auth.models import User
        ```
      -  Saya tambahkan atribut `user` pada model `Item` untuk menyimpan user pada database
         ``` python
         user = models.ForeignKey(User, on_delete=models.CASCADE)
         ```
      - Pada fungsi `create_item` saya tambahkan potongan kode berikut agar item yang dibuat sesuai dengan user yang login
        ``` python
        ...
        if form.is_valid() and request.method == "POST":
           item = form.save(commit=False)
           item.user = request.user
           item.save()
        ...
        ```
      - Saya lakukan migrasi aplikasi untuk atribut baru `user` pada model `Item` degan perintah `python manage.py makemigration` dan `python manage.py migrate`
        
   4. Membuat dua akun pengguna dengan masing-masing tiga *dummy data* menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

      - Pertama, regiter dua user pada form `registeration` aplikasi yang telah dibuat
        
        ![image](https://github.com/MahogaHeryasa/hery_music_strore_inventory/assets/124902537/e11417db-5b21-4ea0-be6c-6c095e388657)

        ![image](https://github.com/MahogaHeryasa/hery_music_strore_inventory/assets/124902537/9b00b9c8-7880-4f64-a8f3-c325608c6b46)

      - Login kedua user tersebut

        ![image](https://github.com/MahogaHeryasa/hery_music_strore_inventory/assets/124902537/47aa78be-87d1-458b-b77a-2943fc888924)

        ![image](https://github.com/MahogaHeryasa/hery_music_strore_inventory/assets/124902537/a61d74d9-4e34-4568-8fcb-dc79e2f00a14)

      - Tambahkan tiga item dengan mengisi form `create_item`

        ![image](https://github.com/MahogaHeryasa/hery_music_strore_inventory/assets/124902537/3ee83374-8077-4156-91c1-9890d4227470)

      - Berikut hasil kedua akun pengguna

        ![image](https://github.com/MahogaHeryasa/hery_music_strore_inventory/assets/124902537/081449ce-83ff-4e39-953e-83a9cdf2e569)

        ![image](https://github.com/MahogaHeryasa/hery_music_strore_inventory/assets/124902537/fdb6c195-3848-42ae-add7-a2cb6f96c756)

   6. Menampilkan detail informasi pengguna yang sedang `logged in` seperti username dan menerapkan `cookies` seperti last login pada halaman utama aplikasi.
      - Pada fungsi `show_main` saya tambahkan context `user_name` untuk memberikan nama user login pada template `main.html` 
        ``` python
        'user_name': request.user.username,
        ```
      - Pada `main.html` saya tambahkan
        ``` html
        ...
        <h3 style="color:#99764b;">User: {{ user_name }} </h3>
        ...
        ```
        untuk menampilkan user yang login pada web
      - Saya lakukan import `import datetime` untuk waktu login pada penerapan `cookies`
      - Pada fungsi `login_user` saya ubah blok kode bagian berikut
        ``` python
        ...
        if user is not None:
          login(request, user)
          response = HttpResponseRedirect(reverse("main:show_main")) 
          response.set_cookie('last_login', str(datetime.datetime.now()))
          return response
        ...
        ```
        agar set cookie waktu `'last_login'` pada user yang baru login,
        dan mengubah fungsi `logout_user`
        ``` python
        def logout_user(request):
          logout(request)
          response = HttpResponseRedirect(reverse('main:login'))
          response.delete_cookie('last_login')
          return response
        ```
        agar menghapus cookie saat user logout
      - Pada fungsi `show_main` saya tambahkan context `last_login` untuk memberikan waktu user terakhir login pada template `main.html` 
        ``` python
        'last_login': request.COOKIES['last_login'],
        ```
      - Pada `main.html` saya tambahkan
        ``` html
        ...
        <h5>{{user_name}}'s last login: {{ last_login }}</h5>
        ...
        ```
        untuk menampilkan waktu terakhir login user
            
</details>

<details>
<summary><b><h1>Tugas 5</h1></b></summary>

 ### 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
 Element selector CSS berguna untuk menyeleksi atau mengelompokkan elemen HTML yang akan mengaplikasikan *style* CSS yang sama.
  - Selektor Tag
    - Manfaat: digunakan untuk memilih semua elemen dengan tag HTML tertentu 
    - Waktu penggunaan: ketika ingin mengaplikasikan *style* CSS pada semua tag HTML yang sama
  - Selektor Class
    - Manfaat: digunakan untuk mengelompokkan elemen HTML berdasarkan class yang kita buat
    - Waktu penggunaan: ketika ingin mengaplikasikan *style* CSS pada elemen tertentu tanpa mempengaruhi elemen-elemen lain
  - Selektor Id
    - Manfaat: digunakan untuk memilih elemen HTML spseifik berdasarkan id yang unik dan hanya satu pada berkas HTML
    - Waktu penggunaan: ketika ingin mengaplikasikan *style* CSS pada satu elemen speifik
  - Selektor Class
    - Manfaat: digunakan untuk memilih elemen berdasarkan atribut HTML mereka
    - Waktu penggunaan: ketika ingin mengaplikasikan *style* CSS pada salah satu atribut elemen sperti elemen input yang memiliki atribut tipe
  - Selektor Universal
    - Manfaat: digunakan untuk memilih semua elemen pada berkas HTML
    - Waktu penggunaan: ketika ingin mengaplikasikan *style* CSS pada semua elemen
  - Selektor Class
    - Manfaat: digunakan untuk memilih elemen semu seperti state pada elemen, elemen before dan after, elemen ganjil, dan sebagainya.
    - Waktu penggunaan: ketika ingin mengaplikasikan *style* CSS pada elemen berdasarkan aksi atau kondisi tertentu.

 ### 2. Jelaskan HTML5 Tag yang kamu ketahui.
  - `<article>`: Mengidentifikasi konten artikel yang berdiri sendiri.
  - `<datalist>`: Kumpulan opsi default untuk elemen `<input>`
  - `<header>`: Representasi dari *header* pada suatu dokumen atau bagian tertentu.
  - `<footer>`: Representasi dari *footer* pada suatu dokumen atau bagian tertentu.
  - `<section>`: Untuk mendefinisikan *section* pada suatu dokumen seperti *header* dan *footer*

 ### 3. Jelaskan perbedaan antara margin dan padding.
 Margin dan padding digunakan untuk mengatur tata letak elemen pada berkas HTML. Margin diimplementasikan dengan membuat ruang kosong di luar elemen sehingga tidak mempengaruhi ukuran elemen namun mempengaruhi jarak antara elemen tersebut dengan yang lain serta mempengaruhi keseluruhan berkas. Sementara padding diimplementasikan dengan membuat ruang kosong didalam elemen sehingga tidak mempengaruhi jarak antara elemen lain namun mempengaruhi ukuran elemen itu sendiri.
 
 ### 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
 Tailwind diimplementasikan pada design html dengan menggabungkan kelas-kelas utilitas yang telah terdefinisikan sebelumnya, memiliki berkas CSS yang lebih ringan, memiliki flexsibilitas *customization* yang tinggi, namun lebih kompleks dikarenakan perlu menggabungkan kelas-kelas utilitas untuk mencapai tampilan yang diinginkan. Sementara bootstrap diimplementasikan pada design html secara langsung dengan komponen dan gaya yang telah didefinisikan oleh bootstrap, memiliki design repetetif dan minim *customization*, namun lebih mudah digunakan.

 Bootstrap sebaiknya digunakan daripada Tailwind ketika kita perlu membuat proyek yang tidak memakan waktu atau pemula yang baru mengenali pemengembangan web, implementasi design akan lebih mudah dengan komponen bawaan Bootstrap. Sebaliknya Tailwind digunakan ketika proyek kita memerlukan kontrol yang lebih besar terhadap tampilan, namun rela melakukan pekerjaan yang lebih banyak untuk mengatur hal tersebut.  

 ### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

  - Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma)
    1. Menambahkan Bootstrap pada aplikasi dengan menambahkan link bootstrap pada base.html 
      ``` html
      <head>
      ...
          {% block meta %}
          {% endblock meta %}
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
          <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
          <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
          <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
      </head>
      ...
      ```

    2. Kustomisasi `login.html`
      - mengimplementasikan template Bootstrap yang menggunakan card sebagai tempat menyimpan form login 
      ``` html
    {% extends 'base.html' %}

    {% block meta %}
        <title>Login</title>
    {% endblock meta %}

    {% block content %}

    <div class = "login">

        <section class="vh-100" style="background-color: #5a0000;">
            <div class="container py-5 h-100">
              <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col col-xl-10">
                  <div class="card" style="border-radius: 1rem;">
                    <div class="row g-0">
                      <div class="col-md-6 col-lg-5 d-none d-md-block">
                        <img src="https://i.pinimg.com/564x/65/fb/e8/65fbe8ca3f041e799c434c15509e71e2.jpg"
                          alt="login form" class="img-fluid" style="border-radius: 1rem 0 0 1rem;" />
                      </div>
                      <div class="col-md-6 col-lg-7 d-flex align-items-center">
                        <div class="card-body p-4 p-lg-5 text-black">
          
                          <form method="POST" action="">
                            {% csrf_token %}
                            <div class="d-flex align-items-center mb-3 pb-1">
                              <img src="https://clipartcraft.com/images/guitar-logo-8.png" alt="Logo" width="50" height="50" style="margin-right: 10px;">
                              <span class="h2 fw-bold mb-0">Hery Music Store Inventory</span>
                            </div>
                            <br/> <br/> 
                            <h5 class="fw-normal mb-3 pb-3" style="letter-spacing: 1px;">Login</h5>
          
                            <div class="form-outline mb-4">
                              <input type="text" name="username" id="Username" class="form-control form-control-lg" placeholder="Username"/>
                              <!-- <label for="Username">Username</label> -->
                            </div>
          
                            <div class="form-outline mb-4">
                              <input type="password" name="password" id="pwpw" class="form-control form-control-lg" placeholder="Password"/>
                              <!-- <label class="form-label" for="pwpw">Password</label> -->
                            </div>
          
                            <div class="pt-1 mb-4">
                              <button class="btn btn-dark btn-lg btn-block" type="submit" value="Login">Login</button>
                            </div>
                            
                            {% if messages %}
                            <ul>
                                {% for message in messages %}
                                    <li>{{ message }}</li>
                                {% endfor %}
                            </ul>
                            {% endif %}   
          
                            <p class="mb-5 pb-lg-2" style="color: #393f81;">Don't have an account? <a href="{% url 'main:register' %}"
                                style="color: #393f81;">Register here</a></p>
                          </form>
          
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
          
    </div>

    {% endblock content %}
      ```

    3. Kustomisasi `register.html`
      - mengimplementasikan template Bootstrap yang menggunakan card sebagai tempat menyimpan form register
      ``` html
      {% extends 'base.html' %}

      {% block meta %}
          <title>Register</title>
      {% endblock meta %}

      {% block content %}  

      <div class = "login">
          
          <section class="vh-100" style="background-color: #5a0000;">
              <div class="container py-5 h-100">
                <div class="row d-flex justify-content-center align-items-center h-100">
                  <div class="col-12 col-md-8 col-lg-6 col-xl-5">
                    <div class="card shadow-2-strong" style="border-radius: 1rem;">
                      <div class="card-body p-5 text-left">
            
                        <h3 class="mb-5">Sign in</h3>
                        
                        <form method="POST">
                          {% csrf_token %} 
                          <div class="form-outline mb-4">
                            <input type="text" id="id_username"  class="form-control form-control-lg" name="{{ form.username.name }}" placeholder="Username"/>
                          </div>
              
                          <div class="form-outline mb-4">
                            <input type="password" id="id_password1" class="form-control form-control-lg" name="{{ form.password1.name }}" placeholder="Password"/>
                          </div>
              
                          <div class="form-outline mb-4">
                            <input type="password" id="id_password2" class="form-control form-control-lg" name="{{ form.password2.name }}" placeholder="Re-type Password"/>
                          </div>
                          <hr class="my-4">
                          <button class="btn btn-primary btn-dark btn-block" type="submit" name="submit" value="Daftar">Register</button>
                        </form>
                        {% if messages %}  
                        <ul>   
                            {% for message in messages %}  
                                <li>{{ message }}</li>  
                                {% endfor %}  
                        </ul>   
                        {% endif %} 
                      </div>
                    </div>
                  </div>
                </div>
              </div>
          </section>  
      </div>  

      {% endblock content %}
      ```
    4. Kustomisasi `create_item.html`
      - mengimplementasikan template Bootstrap yang menggunakan card sebagai tempat menyimpan form create item
      ``` html
    ...
    {% block content %}
    <section class="intro">
        <div class="bg-image-vertical h-100" style="background-color: #f2f2f2;
                background-image: url(https://guitar.com/wp-content/uploads/2021/04/guitar-shop@1400x1050.jpg);
              ">
          <div class="mask d-flex align-items-center">
            <div class="container" style="margin-top: 6rem; margin-bottom: 6rem;">
              <div class="row justify-content-center">
                <div class="col-12 col-lg-10">
                  <div class="card" style="border-radius: 1rem;">
                    <div class="card-body p-5" >
      
                      <h1 class="mb-5 text-center">Item Atribute</h1>
                      <br/>
                      <form method="POST">
                        {% csrf_token %}
                        <div class="form-outline mb-4">
                            <input type="text" id="form6Example3" class="form-control" placeholder="Name" name="name"/>
                        </div>
                        <div class="form-outline mb-4">
                          <input type="number" id="form6Example4" class="form-control" placeholder="Price" name="price"/>
                        </div>
                        <div class="form-outline mb-4">
                          <input type="number" id="form6Example5" class="form-control" placeholder="Amount" name="amount"/>
                        </div>
                        <div class="form-outline mb-4">
                          <textarea class="form-control" id="form6Example7" rows="4" placeholder="Description" name="description"></textarea>
                        </div>

                        <button type="submit" class="btn btn-dark btn-rounded btn-block" value="Add Product">Place Item in Inventory</button>
                      </form>
      
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

    {% endblock %}
      ```
      - Menambahkan *internal style sheet* pada berkas `create_item.html` untuk memodifikasi ketentuan *background image*
      ``` html
      {% extends 'base.html' %} 
      <style>
          .intro {
              height: 100%;
          }

          .bg-image-vertical {
              position: relative;
              background-repeat: repeat;
              background-position: right center;
              background-size: auto 100%;
          }
      </style>
      ...
      ```
    5. Kustomisasi `main.html`
      - Mengimplementasikan komponen Bootstrap navbar pada tampilan daftar inventori dan menempatkan komponen *Add Item*, *Logout*, dan *last login User* didalamnya
      ``` html
      ...
      {% block content %}
      <nav class="navbar navbar-dark shadow fixed-top">
          <div class="container-fluid">
          <a class="navbar-brand" style="color: #f2f2f2;">
              <img src="https://clipartcraft.com/images/guitar-logo-8.png" alt="logo" width="50" height="50">   Hery Music Store Inventory
          </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNavDropdown">
              <ul class="navbar-nav">
              <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false" style="color: #f2f2f2;">
                      Option
                  </a>
                  <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="{% url 'main:logout' %}">Logout</a></li>
                  <li><a class="dropdown-item" href="{% url 'main:create_item' %}">Add Item</a></li>
                  </ul>
              <li class="nav-item dropdown">
                      <a class="nav-link" href="#">last login: {{last_login}}.</a>
              </li>
              </li>
              </ul>
          </div>
          </div>
      </nav>
      ...
      ```

      - Mengimplementasikan komponen Bootstrap jumbotoron untuk menampilkan nama user serta tombol *Add Item*
      ``` html
      ...
      <div style="background: url(https://guitar.com/wp-content/uploads/2021/04/guitar-shop@1400x1050.jpg); font-family:Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif" class="jumbotron bg-cover text-white">
          <div class="container py-5 text-center">
              <br/> <br/> <br/><br/><br/><br/>
              <h1 class="display-4 font-weight-bold text-with-stroke">Welcome {{user_name}}, to Your Inventory</h1>
              <br/>
              <br/> <br/> <br/> <br/>
              <a href= "{% url 'main:create_item' %}" class="btn btn-light px-5">Add Item</a>
          </div>
      </div>
      ...
      ``` 
      - Mengimplementasikan komponen Bootstrap container yang menyimpan table dan komponen Bootstrap card untuk menampilkan produk
      ``` html
        ...
        <section class="py-5">
          <br/>
          <div class="container">
              <h1 style="color:#5a0000; text-align: center;">Total Items Stored in Inventory: {{counter}}</h1>
              <br/> <br/>
              <h5 style="color:#5a0000;"> List Item </h5> 
              <table>
                  <tr>
                      <th style="border: 1px solid #000000;">No</th>
                      <th style="border: 1px solid #000000;">Item</th>
                  </tr>
                  {% for item in items %}
                      <tr>
                          <td style="border: 1px solid #000000;">{{forloop.counter}}</td>
                          <td style="border: 1px solid #000000;">{{item.name}}</td>
                      </tr>
                  {% endfor %}
              </table>
              <br/> <br/> <br/>
              <h5 style="color:#5a0000;"> Catalog </h5>
              <div class="row">
                  {% for item in items %}
                      <div class="col-md-3 mb-5">
                          <div class="card" style="width: 18rem;">
                              <img class="card-img-top" src="https://clipartcraft.com/images/guitar-logo-8.png" alt="item">
                              <div class="card-body">
                                  <h5 class="card-title" style="color:#f2f2f2; white-space: wrap; ">{{item.name}}</h5>
                                  <p></p>
                                  <p class="card-text">Description: {{item.description}}</p>
                                  <p class="card-text">Price: {{item.price}}</p>
                                  <p class="card-text">Amount: {{item.amount}}</p>
                                  <a href="{% url 'main:increase' item.pk %}" class="btn btn-light">+</a>
                                  <a href="{% url 'main:decrease' item.pk %}" class="btn btn-light">-</a>
                                  <a href="{% url 'main:delete' item.pk %}" class="btn btn-light">DEL</a>
                              </div>
                              <div class="card-footer" style="background-color: #ffffff;">
                                  <small class="text-muted">Date Added: {{item.date_added}}</small>
                              </div>
                          </div>
                      </div>
                  <br/>    
                  {% endfor %}
              </div>
          </div>
      </section>
      ...
      ```
      - Mengimplementasikan komponen footer untuk menampilkan nama dan kelas
      ``` html
      ...
      </br>
        <footer id="sticky-footer" class="flex-shrink-0 py-4">
            <div class="container text-center">
              <small style="color: #f2f2f2;">Copyright &copy; {{ my_name }} of Class: {{ class }}</small>
            </div>
        </footer>
    {% endblock content %} 
      ```

</details>