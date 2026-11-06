try:
    with open('ismlar.txt', 'r', encoding='utf-8') as fayl:
        ismlar = fayl.read()
        print("Fayldagi ismlar:\n" + ismlar)
except FileNotFoundError:
    print("ismlar.txt fayli topilmadi. Avval 1-masalani bajaring.")