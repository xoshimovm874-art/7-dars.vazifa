with open("sonlar.txt") as kirish, open("juft_sonlar.txt", "w") as chiqish:
    for qator in kirish:
        if int(qator) % 2 == 0:
            chiqish.write(qator)