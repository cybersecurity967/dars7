try:
    with open('matn.txt', 'r', encoding='utf-8') as fayl:
        qatorlar = fayl.readlines()
        print(f"matn.txt faylida jami {len(qatorlar)} ta qator bor.")
except FileNotFoundError:
    print("matn.txt fayli topilmadi. Iltimos, bu faylni papkada yarating.")