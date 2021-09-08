class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) \
               + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return 'Сложение' + str(self.nums + other.nums)


    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'Вычитание'

    def __mul__(self, other):
        return 'Умножение' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'Деление' + str(round(self.nums / other.nums))
