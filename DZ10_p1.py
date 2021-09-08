class Matrix:
    def __init__(self, input_inform):
        self.input = input_inform

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Проблема формы'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, summed_line)) + '\n'
        else:
            return 'Проблема формы'
        return answer


matrix_1 = Matrix([[6,11], [3, 7], [12, 9], [19, 8]])
matrix_2 = Matrix([[21, 45], [16, 81], [47, 2], [12, 55]])
print(matrix_1)
print()
print(matrix_1 + matrix_2)  # matrix_1.__add__(matrix_2)
