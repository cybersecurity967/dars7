try:
    umumiy_summa = 0
    print("--- Xarajatlar Hisoboti ---")
    
    with open('xarajatlar.txt', 'r', encoding='utf-8') as fayl:
        for qator in fayl:
            qator = qator.strip()
            if qator:
                qismlar = qator.rsplit(' ', 1)
                if len(qismlar) == 2 and qismlar[1].isdigit():
                    nomi = qismlar[0]
                    summa = int(qismlar[1])
                    print(f"{nomi}: {summa} so'm")
                    umumiy_summa += summa
                    
    print("-" * 27)
    print(f"Umumiy summa: {umumiy_summa} so'm")
except FileNotFoundError:
    print("xarajatlar.txt fayli topilmadi.")