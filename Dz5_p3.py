#Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen = ((tutor, klas) for tutor, klas in zip(tutors,klasses))
print(next(gen))
print(next(gen))
print(next(gen))

from itertools import zip_longest
gen = ((tutor, klas) for tutor, klas in zip(tutors,klasses))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

