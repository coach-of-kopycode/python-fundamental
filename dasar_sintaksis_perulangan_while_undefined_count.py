"""
Program perulangan membaca buku dengan while baca buku sampai paham
"""

book_count = 10
read_count = 0

print('Ibu berkata, "Baca buku sampai paham')

understood_count = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {understood_count}')

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f'Buku ke {understood_count + 1} belum paham')
    else:
        understood_count = understood_count + 1
        print(f'Buku ke {understood_count} sudah dibaca dan dipahami')

print(f'Jumlah buku yang dibaca dan dipahami {understood_count}')
if understood_count == book_count:
    print('Semua buku sudah dipahami')
else:
    print(f'Bu tidak semua buku bisa dipahami. '
          f'Budi hanya bisa memahami {understood_count} buku')
