class Matrix:
    def __init__(self, elements):
        self.elements = elements

    def __str__(self):
        line = ''
        for el in self.elements:
            line += f'{el}\n'
        return line

    def __add__(self, other):
        result = Matrix()
        for row in len(self.elements):
            for col in len(row):
                result.elements[row][col] = self.elements[row][col] + other.elements[row][col]
        return result
