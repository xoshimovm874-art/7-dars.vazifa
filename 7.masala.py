fayl = open("matn.txt", "r", encoding="utf-8")
sozlar = fayl.read().split()
fayl.close()
eng_uzun = ""
for soz in sozlar:
    if len(soz) > len(eng_uzun):
        eng_uzun = soz
print("Eng uzun so'z:", eng_uzun)