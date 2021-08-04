word = "процент"
word_1 = "а"
word_2 = "ов"
for x in range(1, 101):
    procent = x % 10
    if procent == 1 and not (11<= x <= 14):
        print (x, word)
    elif 2 <= procent <= 4 and not (11 <= x <= 14):
        print (x, word + word_1)
    elif 5 <= procent <= 9 or procent == 0 or (11 <= x <= 14):
        print(x, word + word_2)
