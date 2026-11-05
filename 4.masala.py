fayl = open("mahsulotlar.txt", "w", encoding="utf-8")
for i in range(5):
    fayl.write(input("Mahsulot nomi: ") + "\n")
fayl.close()

fayl = open("mahsulotlar.txt", "r", encoding="utf-8")
print(fayl.read())
fayl.close()