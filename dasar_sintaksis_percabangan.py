"""
Dasar sintaksis dasar python
1. Sekuensial : langkah berurutan
2. Percabangan : langkah melompat jiika kondisi terpenuhi
3. Perulangan : mengunlang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('Ibu berkata, "Pergi ketoko"')
print('Budi menjawab, "apa yang harus saya lakukan ditoko?"')
print('Ibu menjawab, "beli satu botol susu"')
print('Budi berangkat ketoko untuk berbelanja')
print('===========================================')
# Percabangan
jumlah_botol_susu = 125
jumlah_butir_telur = 3455

print(f'Jumlah susu {jumlah_botol_susu} botol')
print(f'Jumlah telur {jumlah_butir_telur} butir')

if jumlah_botol_susu > 0:
    print('budi membeli satu botol susu')
    if jumlah_butir_telur < 1:
        print('budi membayar satu botol susu')
        print('budi pulang kerumah dengan satu botol susu')
    else:
        print('budi membeli enam butir telur')
        print('budi pulang kerumah membawa satu botol susu dan enam butir telur')
else:
    print('barang yang ingin dibeli budi tidak ada')
    print('budi pulang kerumah')
    print('budi menyampaikan ke ibu')

