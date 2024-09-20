nama_tactical_doll = input("Masukkan nama Tactical Doll: ")
firepower = int(input("Masukkan nilai Firepower: "))
rate_of_fire = int(input("Masukkan nilai Rate of Fire: "))
accuracy = int(input("Masukkan nilai Accuracy: "))
evasion = int(input("Masukkan nilai Evasion: "))

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

dps = hitung_dps(daya tembak, rate_of_fire)
CE = combat_effectiveness (Daya Tembak, rate_of_fire, Akurasi, Penghindaran)

print("\n===== Info Boneka Taktis =====")
print(f"Nama Tactical Doll: {nama_tactical_doll}")
print(f"Senjata: {daya tembak}")
print(f"Laju Tembakan: {rate_of_fire}")
print(f"Akurasi: {akurasi}")
print(f"Penghindaran: {penghindaran}")
print(f"Kerusakan per detik (DPS): {dps}")
print(f"Efektivitas tempur (CE): {ce}")
