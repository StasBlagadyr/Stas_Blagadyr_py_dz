prices = [3.50, 24, 53, 27.50, 260, 1450, 31000, 735.99, 85.60, 99.99, 950.30]
for price in prices:
    grn = int(price)
    kop = (price - int(price)) * 100
    print(f'{grn} грн {kop:02.0f} коп')




#Вывести цены по возрастанию!
prices = [3.50, 24, 53, 27.50, 260, 1450, 31000, 735.99, 85.60, 99.99, 950.30]
print(id(prices))
prices.sort()
print(id(prices))
for price in prices:
    grn = int(price)
    kop = (price - int(price)) * 100
    print(f'{grn} грн {kop:02.0f} коп')



#Вывести цены по убыванию
prices = [3.50, 24, 53, 27.50, 260, 1450, 31000, 735.99, 85.60, 99.99, 950.30]
for price in sorted(prices) [::-1] [:11]:
    grn = int(price)
    kop = (price - int(price)) * 100
    print(f'{grn} грн {kop:02.0f} коп')







