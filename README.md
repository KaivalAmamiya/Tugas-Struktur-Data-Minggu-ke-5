# 📚 Python Algorithms Collection

Repository ini berisi beberapa implementasi algoritma dasar menggunakan Python yang berkaitan dengan **Searching**, **Sorting**, dan **Array Analysis**.  
Setiap program dibuat untuk membantu memahami cara kerja algoritma serta melihat performanya melalui jumlah operasi dan waktu eksekusi.

---

# 📂 Daftar Program

Repository ini terdiri dari lima program utama:

- Modified Binary Search
- Bubble Sort dengan Analisis Proses
- Hybrid Sort
- Merge Three Sorted Lists
- Inversions Counter

---

# 1️⃣ Modified Binary Search

## Deskripsi
Program ini menggunakan **Binary Search yang dimodifikasi** untuk menghitung jumlah kemunculan suatu nilai dalam list yang sudah terurut.

Algoritma bekerja dengan cara:

- mencari **posisi pertama** kemunculan nilai
- mencari **posisi terakhir** kemunculan nilai
- menghitung jumlah kemunculan menggunakan rumus berikut:

```
count = last_index - first_index + 1
```

Pendekatan ini lebih efisien dibandingkan pencarian linear karena ruang pencarian selalu dibagi menjadi dua bagian.

## Kompleksitas

**Time Complexity**

```
O(log n)
```

**Space Complexity**

```
O(1)
```

Binary Search sangat efisien karena setiap langkah mengurangi setengah ruang pencarian.

---

# 2️⃣ Bubble Sort dengan Analisis Proses

## Deskripsi
Program ini mengimplementasikan algoritma **Bubble Sort** dan sekaligus melakukan analisis terhadap proses pengurutan data.

Selama proses sorting, program akan menghitung:

- jumlah **perbandingan**
- jumlah **pertukaran elemen**
- jumlah **iterasi (pass)**

Setiap iterasi juga akan menampilkan kondisi array setelah proses pertukaran dilakukan.

## Kompleksitas

**Worst Case**

```
O(n²)
```

**Best Case (data sudah terurut)**

```
O(n)
```

Algoritma juga menggunakan optimasi dengan menghentikan proses lebih awal apabila dalam satu iterasi tidak terjadi pertukaran.

---

# 3️⃣ Hybrid Sort

## Deskripsi
Hybrid Sort merupakan kombinasi dari dua algoritma pengurutan:

- **Insertion Sort** untuk data berukuran kecil
- **Selection Sort** untuk data berukuran lebih besar

Program akan menentukan algoritma yang digunakan berdasarkan ukuran array menggunakan parameter **threshold**.

Selain itu program juga membandingkan performa antara:

- Hybrid Sort
- Insertion Sort
- Selection Sort

Perbandingan dilakukan dengan menghitung total operasi seperti **comparisons** dan **swaps**.

## Kompleksitas

**Insertion Sort**

Best Case  
```
O(n)
```

Worst Case  
```
O(n²)
```

**Selection Sort**

```
O(n²)
```

Hybrid Sort mencoba memilih metode yang lebih sesuai dengan ukuran data.

---

# 4️⃣ Merge Three Sorted Lists

## Deskripsi
Program ini digunakan untuk **menggabungkan tiga list yang sudah terurut** menjadi satu list yang tetap terurut.

### Contoh

Input

```
A = [1,5,9]
B = [2,6,10]
C = [3,4,7]
```

Output

```
[1,2,3,4,5,6,7,9,10]
```

Algoritma menggunakan **tiga pointer** untuk membandingkan elemen dari masing-masing list dan memilih nilai terkecil pada setiap iterasi.

## Kompleksitas

**Time Complexity**

```
O(n)
```

**Space Complexity**

```
O(n)
```

Setiap elemen hanya diproses satu kali selama proses penggabungan.

---

# 5️⃣ Inversions Counter

## Deskripsi
Program ini digunakan untuk menghitung jumlah **inversion** dalam sebuah array.

Inversion adalah pasangan indeks `(i, j)` yang memenuhi kondisi berikut:

```
i < j
arr[i] > arr[j]
```

### Contoh

Array

```
[3,1,2]
```

Inversion yang terjadi

```
(3,1)
(3,2)
```

Total inversion = **2**

Program ini menggunakan dua pendekatan berbeda.

### 1. Naive Method

Metode sederhana dengan membandingkan semua pasangan elemen dalam array.

Kompleksitas

```
O(n²)
```

### 2. Merge Sort Based Method

Pendekatan yang lebih efisien dengan memanfaatkan konsep **Merge Sort**.

Kompleksitas

```
O(n log n)
```
Program juga dapat membandingkan waktu eksekusi kedua metode tersebut.
---
# ▶️ Cara Menjalankan Program
Pastikan Python sudah terinstall di komputer.

### Clone repository
```
git clone https://github.com/KaivalAmamiya/Tugas-Struktur-Data-Minggu-ke-3.git
```
Masuk ke folder project
```
cd Tugas-Struktur-Data-Minggu-ke-3
```
Jalankan program
```
filename.py
```

---

# 🎯 Tujuan Repository
Repository ini dibuat untuk:
- memahami konsep algoritma dasar
- mempelajari analisis kompleksitas algoritma
- membandingkan performa berbagai metode sorting dan searching
- melatih implementasi algoritma menggunakan Python

---
