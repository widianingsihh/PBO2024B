import math

print ("--- TACTICAL DOLL CROSSFIRE ---")
weapon = input("Nama Tactical Doll: ")
firepower = int(input("Masukkan FirePower: "))
rate_of_fire = int(input("Masukkan Rate of fire: "))
accuracy = int(input("Masukkan Accuracy: "))
evasion = int(input("Masukkan Evasion: "))

DPS = firepower * rate_of_fire / 62
combat_effectiveness = 30 * firepower + 40 * rate_of_fire/120 + 15 * (accuracy + evasion)

print ("--- SUCCESS ---")
print("Tactical Doll: " + weapon)
print(f"FirePower: {firepower}")
print(f"Rate Of Fire: {rate_of_fire}")
print(f"Accuracy: {accuracy}")
print(f"Evasion: {evasion}")
print(f"Damage Per Second: {DPS:.2f}")
print(f"Combat Effectiveness: {math.floor(combat_effectiveness)}")

# Important!
# Floor for membulatkan angka bilangan ke bilangan terdekat.
# f (format string) for memasukkan Nilai atau angka bilangan yang menggunakan kurung kurawal{}.

