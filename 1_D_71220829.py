print("\(^O^) Selamat datang di Kalkulator Sederhana(^O^)/")
print("Ketik 1 untuk menghitung penjumlahan.")
print("Ketik 2 untuk menghitung pengurangan.")
print("Ketik 3 untuk menghitung perkalian.")
print("Ketik 4 untuk menghitung pembagian.")
print("Ketik 5 untuk menghitung sisa hasil bagi (modulus).")
print("Ketik 6 untuk menghitung pemangkatan.")
plh=int(input("Masukkan pilihan Anda:"))
bp1=int(input("Masukkan bilangan pertama:"))
bp2=int(input("Masukkan bilangan kedua:"))

rumus1=(int(bp1+bp2))
rumus2=(int(bp1-bp2))
rumus3=(int(bp1*bp2))
rumus4=(int(bp1/bp2))
rumus5=(int(bp1%bp2))
rumus6=(int(bp1**bp2))

if(plh=="1"):
    (print("hasil dari",bp1,"dijumlahkan dengan",bp2,"adalah",(rumus1)))
elif(plh=="2"):
    (print("hasil dari",bp1,"dijumlahkan dengan",bp2,"adalah",(rumus2)))
elif(plh=="3"):
    (print("hasil dari",bp1,"dijumlahkan dengan",bp2,"adalah",(rumus3)))
elif(plh=="4"):
    (print("hasil dari",bp1,"dijumlahkan dengan",bp2,"adalah",(rumus4)))
elif(plh=="5"):
    (print("hasil dari",bp1,"dijumlahkan dengan",bp2,"adalah",(rumus5)))
else:
    (print("hasil dari",bp1,"dijumlahkan dengan",bp2,"adalah",(rumus6)))