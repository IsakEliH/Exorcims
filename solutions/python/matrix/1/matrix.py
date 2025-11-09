class Matrix:
    def __init__(self, matrix_string: str):
        matrix = matrix_string.split("\n")
        for index, string in enumerate(matrix):
            string = string.split()
            matrix[index] = [int(x) for x in string]

        self.matrix = matrix

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        column_list = []
        for x in self.matrix:
            column_list.append(x[index - 1])
        return column_list
