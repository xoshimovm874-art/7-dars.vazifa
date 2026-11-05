fayl = open("matn.txt", "r", encoding="utf-8")
qatorlar = fayl.readlines()
fayl.close()

print("Qatorlar soni:", len(qatorlar))