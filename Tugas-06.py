from datetime import datetime

print("Halo Selamat Datang")
print("Hari ini kamu mau melakukan apa?")
print("sarapan")
print("pergi kerja")

aktivitas = input ("Masukkan aktivitas yang mau kamu pilih!")

if aktivitas.lower() == ("sarapan"):

    print("Berikut menu sarapan yang tersedia:")
    print("telur")
    print("ikan")
    print("nugget")

    menu = input ("Mau sarapan apa hari ini?")

    if menu.lower() == "telur" or menu.lower () == "ikan" or menu.lower() == "nugget":
        print (f"baik, {menu} terseedia. Jangan lupa untuk dimasak!")
    else:
        print(f"Mohon maaf, bahan tidak tersedia. Silahkan membeli bahannya terlebih dahulu")

elif aktivitas.lower()== "pergi kerja":
    waktu = datetime.now()
    print("Jadwal pergi kerja pada pukul 08.00 WIB")
    print(f"Saat ini pukul {waktu}")

    if waktu.hour < 08.00: 
        print("Keren! anda masih memiliki waktu untuk sampai tepat waktu")
    elif waktu.hour == 08.00:
        print("Hati-hati dijalan! Ini sudah pukul 08.00, selanjutnya anda persiapkan lebih awal")
    else: 
        print("Aduh, anda sudah telat. Jangan sampai terulang ya")