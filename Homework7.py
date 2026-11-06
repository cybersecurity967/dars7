try:
    with open('matn.txt', 'r', encoding='utf-8') as fayl:
        matn = fayl.read()
        sozlar = matn.split() 
        if sozlar:
            eng_uzun = max(sozlar, key=len)
            print(f"Fayldagi eng uzun so'z: {eng_uzun}")
        else:
            print("Fayl bo'sh.")
except FileNotFoundError:
    print("matn.txt fayli topilmadi.")