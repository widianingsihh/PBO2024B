def hitung_dps(daya tembak, rate_of_fire):
    dps = (daya tembak * rate_of_fire) / 60
    Putaran Pengembalian (DPS, 2) 


def combat_effectiveness (daya tembak, rate_of_fire, akurasi, penghindaran):
    combat_effectiveness = (
        30 * daya tembak + 
        40 * (rate_of_fire**2 / 120) +
        15 * (akurasi + penghindaran)
    )
    kembalikan int(combat_effectiveness)


print("Masukkan informasi Tactical Doll milikmu:")
nama_tactical_doll = input("Masukkan nama Tactical Doll: ")
firepower = int(input("Masukkan nilai Firepower: "))
rate_of_fire = int(input("Masukkan nilai Rate of Fire: "))
accuracy = int(input("Masukkan nilai Accuracy: "))
evasion = int(input("Masukkan nilai Evasion: "))



print("\n Masukkaninformasi Tactical Doll musuh:")
nama_tactical_doll_musuh = input("Masukkan nama Tactical Doll: ")
firepower_musuh = int(input("Masukkan nilai Firepower: "))
rate_of_fire_musuh = int(input("Masukkan nilai Rate of Fire: "))
accuracy_musuh = int(input("Masukkan nilai Accuracy: "))
evasion_musuh = int(input("Masukkan nilai Evasion: "))


dps = hitung_dps(daya tembak, rate_of_fire)
CE = combat_effectiveness (Daya Tembak, rate_of_fire, Akurasi, Penghindaran)


dps_milikmu = hitung_dps (daya tembak, rate_of_fire)
ce_milikmu = combat_effectiveness (daya tembak, rate_of_fire, akurasi, penghindaran)


dps_musuh = hitung_dps(firepower_musuh, rate_of_fire_musuh)
ce_musuh = combat_effectiveness(firepower_musuh, rate_of_fire_musuh, accuracy_musuh, evasion_musuh)


jika ce_milikmu > ce_musuh:
    langkah = "MAJUU!!"
lainnya:
    langkah = "KABUR"🏃


nama_lengkap = input("\nMasukkan Nama Lengkap Anda: ")
nim = input("Masukkan NIM Anda: ")


print("\n===== Info Tantangan Boneka Taktis =====")
print(f"Nama Lengkap Anda: {nama_lengkap}")
print(f"NIM Anda: {nim}")

print("\n===== Boneka Taktis Milikmu =====")
print(f"Nama Tactical Doll: {nama_tactical_doll}")
print(f"Kerusakan per Detik (DPS): {dps_milikmu}")
print(f"Efektivitas Tempur (CE): {ce_milikmu}")

print("\n===== Boneka Taktis Musuh =====")
print(f"Nama Tactical Doll: {nama_tactical_doll_musuh}")
print(f"Kerusakan per Detik (DPS): {dps_musuh}")
print(f"Efektivitas Tempur (CE): {ce_musuh}")
print(f"\nLangkah yang harus diambil: {langkah}")
