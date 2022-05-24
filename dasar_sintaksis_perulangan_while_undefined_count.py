"""
Program perulangan membaca buku dengan while baca buku sampai paham
"""

jumlah_buku = 10
jumlah_baca = 0

print('Ibu berkata, "Baca buku sampai paham')

jumlah_paham = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_paham}')

while jumlah_baca < jumlah_buku * 2:
    jumlah_baca = jumlah_baca + 1
    if jumlah_paham == 9:
        print(f'Buku ke {jumlah_paham + 1} belum paham')
    else:
        jumlah_paham = jumlah_paham + 1
        print(f'Buku ke {jumlah_paham} sudah dibaca dan dipahami')

print(f'Jumlah buku yang dibaca dan dipahami {jumlah_paham}')
if jumlah_paham == jumlah_buku:
    print('Semua buku sudah dipahami')
else:
    print(f'Bu tidak semua buku bisa dipahami. '
          f'Budi hanya bisa memahami {jumlah_paham} buku')
