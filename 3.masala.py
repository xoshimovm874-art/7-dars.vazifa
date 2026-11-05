yangi = input("Yangi ism: ")

fayl = open("ismlar.txt", "a", encoding="utf-8")
fayl.write(yangi + "\n")
fayl.close()
