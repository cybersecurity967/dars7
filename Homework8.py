try:
    with open('sonlar.txt', 'r') as oqish_fayli, open('juft_sonlar.txt', 'w') as yozish_fayli:
        for qator in oqish_fayli:
            son = int(qator.strip())
            if son % 2 == 0:
                yozish_fayli.write(str(son) + '\n')
    print("Faylga muvaffaqiyatli yozildi.")
except FileNotFoundError:
    print("sonlar.txt fayli topilmadi.")
except ValueError:
    print("Faylda faqat sonlar kiritilganiga ishonch hosil qiling.")