# Nama  : Raihan Fauzi Rakhman
# NIM   : 2403872
# Kelas : RPL 1C

student_info = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Mathematics"},
    "Charlie": {"age": 19, "major": "Physics"}
}

# Menyimpan beberapa info dari siswa ke dalam variabel
student_name = input("Inputkan nama siswa : ")
student_age = student_info[student_name]["age"]
student_major = student_info[student_name]["major"]
print(f'Umur {student_name} adalah {student_age} dan Prodi nya adalah {student_major}')