#редставлен список чисел. Определить элементы списка, не имеющие повторений.
#Сформировать из этих элементов список с сохранением порядка их следования


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

num = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print(x for x in num if num.count(x) == 1)
