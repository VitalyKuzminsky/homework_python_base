class ComplexNumber:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2
        complex_number = complex(self.number_1, self.number_2)
        print(complex_number)

    def __add__(self, other):
        return ComplexNumber(self.number_1 + other.number_1, self.number_2 + other.number_2)

    def __mul__(self, other):
        return ComplexNumber(self.number_1 * other.number_1 + self.number_2 * other.number_2 * -1,
                             self.number_1 * other.number_2 + self.number_2 * other.number_1)


cn_1 = ComplexNumber(2, 3)
cn_2 = ComplexNumber(5, 4)
print('Операции с комплексными числами:')
sum_cn = cn_1 + cn_2
mul_cn = cn_1 * cn_2
