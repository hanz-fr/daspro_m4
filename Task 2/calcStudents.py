# Nama  : Raihan Fauzi Rakhman
# NIM   : 2403872
# Kelas : RPL 1C

from collections import Counter

students = {
    "Alice": "Computer Science",
    "Bob": "Mathematics",
    "Charlie": "Physics",
    "David": "Computer Science",
    "Eva": "Mathematics",
}

# hitung jurusan yang sama menggunakan Counter()
count = Counter(students.values())
print(f'Prodi computer science sebanyak {count['Computer Science']}')
print(f'Prodi mathematics sebanyak {count['Mathematics']}')
print(f'Prodi physics sebanyak {count['Physics']}')