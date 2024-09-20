import math
Nama = "Nama Bayu Gunawan"
Nim = "2355201032"

print ("--- TACTICAL DOLL CROSSFIRE ---")
weapon = input("Nama Tactical Doll: ")
firepower = int(input("Masukkan FirePower: "))
rate_of_fire = int(input("Masukkan Rate of fire: "))
accuracy = int(input("Masukkan Accuracy: "))
evasion = int(input("Masukkan Evasion: "))

print ("--- ENEMY TACTICAL DOLL CROSSFIRE ---")
weapon2 = input("Nama Tactical Doll: ")
firepower2 = int(input("Masukkan FirePower: "))
rate_of_fire2 = int(input("Masukkan Rate of fire: "))
accuracy2 = int(input("Masukkan Accuracy: "))
evasion2 = int(input("Masukkan Evasion: "))

DPS = firepower * rate_of_fire / 62
combat_effectiveness = 30 * firepower + 40 * rate_of_fire/120 + 15 * (accuracy + evasion)

DPS2 = firepower2 * rate_of_fire2 / 62
combat_effectiveness2 = 30 * firepower + 40 * rate_of_fire/120 + 15 * (accuracy + evasion)

print ("--- RESULT ---")
print(weapon)
# print(f"FirePower: {firepower}")
# print(f"Rate Of Fire: {rate_of_fire}")
# print(f"Accuracy: {accuracy}")
# print(f"Evasion: {evasion}")
print(f"Damage Per Second: {DPS:.2f}")
print(f"Combat Effectiveness: {math.floor(combat_effectiveness)}")

print(weapon2)
print(f"Damage Per Second: {DPS2:.2f}")
print(f"Combat Effectiveness: {math.floor(combat_effectiveness2)}")

if weapon > weapon2:
    print ("Gas Jangan Kasih Kabur")
elif weapon2 > weapon:
    print("Nuh Im Out")

print ("Data Diri")
print ("Nama Lengkap", Nama)
print ("Nim", Nim)

# Important!
# Floor for membulatkan angka bilangan ke bilangan terdekat.
# f (format string) for memasukkan Nilai atau angka bilangan yang menggunakan kurung kurawal{}.

