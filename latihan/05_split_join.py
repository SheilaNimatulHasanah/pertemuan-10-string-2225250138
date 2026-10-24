# Input: Kalimat string
# Proses: Memecah kalimat menjadi list kata dengan split() dan menggabungkannya kembali dengan join()
# Output: List kata dan string tergabung dengan tanda hubung (-)

kalimat = "data teks perlu dibersihkan" 
kata = kalimat.split() 
print(kata) 
print("-".join(kata))