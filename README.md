# 📚 Analisis Algoritma – Searching & Sorting

Repository ini berisi implementasi beberapa algoritma dasar dalam **analisis algoritma** menggunakan Python.

Algoritma yang dibahas dalam tugas ini:

🔎 Modified Binary Search  
🔁 Bubble Sort dengan Analisis Langkah  
⚡ Hybrid Sort  
🔗 Merge Tiga Sorted Lists  
📊 Inversions Counter  

Setiap soal berisi:
- 📝 Penjelasan
- 💻 Kode Program
- 📥 Contoh Input
- 📤 Contoh Output

---

# 🔎 Soal 1 – Modified Binary Search

## 📝 Penjelasan

Binary Search adalah algoritma pencarian yang digunakan pada **array yang sudah terurut**.

Cara kerjanya:

1. Menentukan elemen tengah array
2. Membandingkan elemen tengah dengan target
3. Jika target lebih kecil → cari di **bagian kiri**
4. Jika target lebih besar → cari di **bagian kanan**
5. Proses diulang sampai elemen ditemukan

Kompleksitas waktu:

```
O(log n)
```

Binary Search jauh lebih cepat dibanding **Linear Search (O(n))**.

---

## 💻 Kode

```python
def modified_binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1
```

---

## 📥 Contoh Input

```
Array  : [1, 3, 5, 7, 9]
Target : 7
```

## 📤 Output

```
3
```

Artinya **angka 7 ditemukan pada indeks ke-3**.

---

# 🔁 Soal 2 – Bubble Sort dengan Analisis Langkah

## 📝 Penjelasan

Bubble Sort adalah algoritma sorting sederhana yang bekerja dengan cara:

1️⃣ Membandingkan dua elemen bersebelahan  
2️⃣ Jika urutan salah → tukar posisi  
3️⃣ Proses diulang sampai seluruh array terurut  

Kompleksitas waktu:

```
O(n²)
```

Pada program ini juga dihitung:

- 🔎 jumlah **comparisons**
- 🔁 jumlah **swaps**

untuk mengetahui banyaknya langkah algoritma.

---

## 💻 Kode

```python
def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                
    return comparisons, swaps
```

---

## 📥 Contoh Input

```
[5, 1, 4, 2, 8]
```

## 📤 Output

```
Sorted array : [1, 2, 4, 5, 8]
Comparisons  : 10
Swaps        : 4
```

---

# ⚡ Soal 3 – Hybrid Sort

## 📝 Penjelasan

Hybrid Sort adalah algoritma yang **menggabungkan dua metode sorting** untuk meningkatkan efisiensi.

Pada program ini digunakan:

🔹 **Insertion Sort** → untuk dataset kecil  
🔹 **Selection Sort** → untuk dataset besar  

Alasannya:

- Insertion Sort sangat cepat untuk **data kecil**
- Selection Sort lebih stabil untuk **data besar**

Program juga membandingkan jumlah operasi dari:

- Hybrid Sort
- Insertion Sort
- Selection Sort

---

## 💻 Kode

```python
import random

def insertion_sort(arr):
    comparisons = 0
    swaps = 0
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j+1] = arr[j]
            swaps += 1
            j -= 1
            
        arr[j+1] = key
        
    return comparisons + swaps


def selection_sort(arr):
    comparisons = 0
    swaps = 0
    
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps += 1
        
    return comparisons + swaps


def hybrid_sort(arr, threshold=10):
    if len(arr) <= threshold:
        return insertion_sort(arr)
    else:
        return selection_sort(arr)
```

---

## 📥 Contoh Input

```
[8, 3, 5, 1, 9]
```

## 📤 Output Sorting

```
[1, 3, 5, 8, 9]
```

---

# 🔗 Soal 4 – Merge Tiga Sorted Lists

## 📝 Penjelasan

Masalah ini meminta kita untuk **menggabungkan tiga list yang sudah terurut** menjadi satu list yang tetap terurut.

Cara kerja algoritma:

1️⃣ Bandingkan elemen pertama dari tiga list  
2️⃣ Ambil nilai paling kecil  
3️⃣ Masukkan ke list hasil  
4️⃣ Geser indeks list tersebut  
5️⃣ Ulangi sampai semua elemen habis  

Kompleksitas waktu:

```
O(n)
```

---

## 💻 Kode

```python
def merge_three_lists(a, b, c):
    result = []
    i = j = k = 0
    
    while i < len(a) and j < len(b) and k < len(c):
        smallest = min(a[i], b[j], c[k])
        result.append(smallest)
        
        if smallest == a[i]:
            i += 1
        elif smallest == b[j]:
            j += 1
        else:
            k += 1
            
    result.extend(a[i:])
    result.extend(b[j:])
    result.extend(c[k:])
    
    return result
```

---

## 📥 Contoh Input

```
A = [1,4,7]
B = [2,5,8]
C = [3,6,9]
```

## 📤 Output

```
[1,2,3,4,5,6,7,8,9]
```

---

# 📊 Soal 5 – Inversions Counter

## 📝 Penjelasan

Inversion adalah pasangan indeks `(i, j)` dimana:

```
i < j dan arr[i] > arr[j]
```

Artinya posisi elemen **tidak sesuai dengan urutan yang benar**.

Program ini menggunakan dua metode:

### 1️⃣ Naive Method

Membandingkan semua pasangan elemen.

Kompleksitas:

```
O(n²)
```

### 2️⃣ Merge Sort Method

Menggunakan teknik **merge sort** untuk menghitung inversions saat proses penggabungan array.

Kompleksitas:

```
O(n log n)
```

Metode ini jauh lebih efisien untuk data besar.

---

## 💻 Kode

```python
def countInversionsNaive(arr):
    n = len(arr)
    inv = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                inv += 1
                
    return inv
```

---

## 📥 Contoh Input

```
[2,4,1,3,5]
```

## 📤 Output

```
Jumlah inversions = 3
```

Pasangan inversions:

```
(2,1)
(4,1)
(4,3)
```

---

# ✅ Kesimpulan
Dari implementasi algoritma di atas dapat disimpulkan bahwa:
✔ **Binary Search** sangat efisien untuk pencarian data terurut  
✔ **Bubble Sort** mudah dipahami tetapi kurang efisien untuk data besar  
✔ **Hybrid Sort** dapat meningkatkan performa dengan menggabungkan dua algoritma  
✔ **Merge Sorted Lists** memungkinkan penggabungan data secara efisien  
✔ **Merge Sort Inversion Counter** jauh lebih cepat dibanding metode naive

---

## 🚀 Cara Menjalankan
### 1. Clone Repository
```bash
git clone https://github.com/KaivalAmamiya/Tugas-Struktur-Data-Minggu-ke-5.git
cd Tugas-Struktur-Data-Minggu-ke-5
