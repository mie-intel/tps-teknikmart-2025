## **Simulasi Antrean pada Teknik Mart**

## Struktur Folder

```
📁
 - cashier.py
 - color.py
 - config.py
 - Game.py
 - main.py
 - map.py
 - observation_data.json
 - person.py
 - state.py
 - utils.py
```

- `cashier.py` : berisi implementasi untuk mengatur kasir dan antrian pada kasir
- `color.py` : berisi definisi dari konstan warna - warna tertentu
- `config.py` : berisi variabel - variabel untuk mengatur jalannya simulasi
- `Game.py` : berisi fungsi - fungsi utama untuk mengatur siklus berjalannya simulasi
- `main.py` : merupakan file utama yang dijalankan program. file ini nantinya akan memanggil fungsi - fungsi dari Game.py
- `map.py` : berisi implementasi peta dari simulasi
- `observation_data.json` : berisi data hasil pengamatan yang nantinya akan digunakan selama berjalannya simulasi
- `person.py` : berisi implementasi perilaku dari setiap _agent_ pelanggan
- `state.py` : berisi variabel - variabel global yang menentukan kondisi simulasi saat dijalankan
- `utils.py` : berisi fungsi - fungsi pembantu berjalannya simulasi

## Requirement

```
pygame
numpy
datetime
```

## How to run?

1. Install terlebih dahulu beberapa dependencies dengan

   ```
   pip install -r requirements.txt
   ```

2. Gunakan perintah berikut

   ```
   python main.py
   ```

## Reports

Hasil simulasi data akan disimpan di dalam folder `/results`

Baca artikel selengkapnya [di sini](https://www.notion.so/ARTIKEL-Project-Teknik-Pemodelan-dan-Simulasi-201884ed4c9580968b31c699c3199ec6)
