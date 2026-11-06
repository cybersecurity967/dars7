qidirilayotgan_ism = input("Qidirmoqchi bo'lgan ismni kiriting: ").strip()

try:
    with open('ismlar.txt', 'r', encoding='utf-8') as fayl:
        ismlar = [qator.strip() for qator in fayl.readlines()]
        
    if qidirilayotgan_ism in ismlar:
        print("Ism topildi")
    else:
        print("Ism topilmadi")
except FileNotFoundError:
    print("ismlar.txt fayli yo'q.")