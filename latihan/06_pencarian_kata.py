# Input: Teks kalimat dan kata kunci pencarian
# Proses: Mengubah ke huruf kecil, memeriksa keberadaan kata, menghitung frekuensi, dan mencari posisi
# Output: Status kebenaran (True/False), jumlah kemunculan, dan indeks posisi

teks = "Python untuk data. Python untuk pendidikan." 
teks = teks.lower() 
kata = "python" 
print(kata in teks) 
print(teks.count(kata)) 
print(teks.find(kata))