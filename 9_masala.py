with open("baholar.txt") as fayl:
    ballar = [float(qator) for qator in fayl if qator.strip()]

soni = len(ballar)
print("Ballar soni:", soni)
print("Eng katta ball:", max(ballar))
print("Eng kichik ball:", min(ballar))
print("O'rtacha ball:", sum(ballar) / soni)