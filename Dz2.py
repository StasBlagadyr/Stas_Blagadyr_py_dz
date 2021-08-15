#Создать список, состоящий из кубов нечетных чисел от 1 до 1000 (куб х - третья степень числа х):
# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делиться нацело на 7.
# b. К каждому элементу добавить 17 и вычислить заново.
def sum_of_digits(x):
    summa = 0
    while x:
        summa += x % 10
        x //= 10
    return summa
mass_of_cubes = [x ** 3 for x in range(1, 1001, 2)]
answer_summa_1 = 0
answer_summa_2 = 0
for number in mass_of_cubes:
    new_number = number + 17
    if sum_of_digits(number) % 7 == 0:
        answer_summa_1 += number
    if sum_of_digits(new_number) % 7 == 0:
        answer_summa_2 += new_number
print("a", answer_summa_1)
print("b", answer_summa_2)