try:
    with open('baholar.txt', 'r') as fayl:
        ballar = [int(qator.strip()) for qator in fayl.readlines() if qator.strip()]
    if ballar:
        print(f"Ballar soni: {len(ballar)}")
        print(f"Eng katta ball: {max(ballar)}")
        print(f"Eng kichik ball: {min(ballar)}")
        print(f"O'rtacha ball: {sum(ballar) / len(ballar):.2f}")
    else:
        print("Fayl bo'sh.")
except FileNotFoundError:
    print("baholar.txt fayli topilmadi.")