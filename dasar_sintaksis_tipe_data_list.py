my_hobby = ['Swimming', 'Travelling', 'Learning']
print(my_hobby)

print('\nMenampilkan dengan for in')
for hobby in my_hobby:
    print(hobby)

print('\nMenampilkan dengan for in')
for i in range(0, len(my_hobby)):
    print(my_hobby[i])

print('\nMenampilkan data dengan indeks tertentu')
print(my_hobby[0])
print(my_hobby[2])

print('\nMenambahkan data baru')
my_hobby.append('Coding')
for i in range(0, len(my_hobby)):
    print(my_hobby[i])

print('\nGanti tipe data')
my_hobby = [1, 2.3, 'Walking']
for i in range(0, len(my_hobby)):
    print(my_hobby[i])

print('\nClear List')
my_hobby.clear()
for i in range(0, len(my_hobby)):
    print(my_hobby[i])

print('\nGanti elemen pertama')
my_hobby = ['Swimming', 'Travelling', 'Learning']
my_hobby[0] = 'Sing'
for i in range(0, len(my_hobby)):
    print(my_hobby[i])

print('\nAmbil elemen ke-dua')
hobby = my_hobby.pop(1)
for i in range(0, len(my_hobby)):
    print(my_hobby[i])

print('\nBuku yang diambil')
print(hobby)

print('\nPop -2')
my_hobby = ['Swimming', 'Travelling', 'Learning']
my_hobby.pop(-2)
for i in range(0, len(my_hobby)):
    print(my_hobby[i])



