yangi_ism = input("Yangi ism kiriting: ")
with open('ismlar.txt', 'a', encoding='utf-8') as fayl:
    fayl.write(yangi_ism + '\n')
print("Yangi ism faylga qo'shildi.")