# Input: Teks dengan spasi berlebih di awal, tengah, dan akhir
# Proses: Menghapus spasi luar dengan strip() dan merapikan spasi ganda menggunakan replace()
# Output: Teks bersih berformat capitalize

teks = " belajar python untuk pendidikan " 
teks = teks.strip() 
while " " in teks: 
    teks = teks.replace(" ", " ") 
print(teks.capitalize())