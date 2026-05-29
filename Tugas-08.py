user = input ("Siapa namamu?")

print(f"\n♟️1.Papan Catur Masukkan kegiatan {user}♟️")

for baris in range (8):
    for kolom in range (8):
        if (baris+kolom) % 2 == 0:
            print ("⬛", end=" ")
        else:
            print("⬜", end=" ")
    print()

print(f"\n ♟️ 2. Daftar Kegiatan {user}♟️")

Daftar_kegiatan = []
Jumlah_kegiatan = int(input("Berapa banyak kegiatan yang ingin dimasukkan?"))

for i in range(Jumlah_kegiatan):
    print()
    print(f"\n♟️Kegiatan ke-{i+1}♟️")

    Nama_kegiatan = input("Nama_kegiatan: ")
    Waktu_kegiatan = input("Waktu_kegiatan: ")
    Durasi_kegiatan = input("Durasi_kegiatan: ")
    Tempat_kegiatan = input("Tempat_kegiatan: ")

    Kegiatan= {
        "Kegiatan": Nama_kegiatan,
        "Waktu": Waktu_kegiatan,
        "Durasi": Durasi_kegiatan,
        "Tempat": Tempat_kegiatan
    }
    Daftar_kegiatan.append(Kegiatan)
print()

print(f"\n♟️Daftar kegiatan yang sudah {user} masukkan♟️")

for i in range(len(Daftar_kegiatan)):
    print(f"Kegiatan {i + 1}")
    print(f"Nama kegiatan: {Daftar_kegiatan[i]['Kegiatan']}")
    print(f"Waktu kegiatan: {Daftar_kegiatan[i]['Waktu']}")
    print(f"Durasi kegiatan: {Daftar_kegiatan[i]['Durasi']}")
    print(f"Tempat kegiatan: {Daftar_kegiatan[i]['Tempat']}")
    print()