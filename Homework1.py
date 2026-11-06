with open('ismlar.txt', 'w', encoding='utf-8') as fayl:
    for i in range(5):
        ism = input(f"{i+1}-ismni kiriting: ")
        fayl.write(ism + '\n')
print("Ismlar faylga yozildi.")