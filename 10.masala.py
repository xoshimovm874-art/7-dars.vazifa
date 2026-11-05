jami = 0

fayl = open("xarajatlar.txt")
for qator in fayl:
    qismlar = qator.split()
    if len(qismlar) == 2:
        print(qismlar[0], qismlar[1])
        jami = jami + int(qismlar[1])
fayl.close()

print("Jami xarajat:", jami)