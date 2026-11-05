ism = input("ism kiritng: ")

with open("ismlar.txt", "r") as f:
    data = f.read().split()
    if ism in data:
        print("ism topildi")
    else:
        print("topilmadi")     
        