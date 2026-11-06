with open('mahsulotlar.txt', 'w', encoding='utf-8') as fayl:
    for i in range(5):
        mahsulot = input(f"{i+1}-mahsulot nomini kiriting: ")
        fayl.write(mahsulot + '\n')

with open('mahsulotlar.txt', 'r', encoding='utf-8') as fayl:
    print("\nBarcha mahsulotlar:")
    print(fayl.read())