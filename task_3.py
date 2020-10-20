class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        new_cell = self.quantity + other.quantity
        return Cell(new_cell)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __sub__(self, other):
        return Cell((self.quantity - other.quantity) if (self.quantity - other.quantity) > 0 else "the " \
                                                                                                  "result" \
                                                                                                  "is < 0!")

    def __truediv__(self, other):
        try:
            return Cell(self.quantity // other.quantity)
        except ValueError:
            return Cell('Division to 0!')

    def __str__(self):
        return f'{self.quantity}'

    def make_order(self, row_quantity):
        y = ['*' * row_quantity for _ in range(self.quantity // row_quantity)]
        y.append('*' * (self.quantity % row_quantity)) if self.quantity % row_quantity != 0 else ''
        print("\n".join(y))


cell_1 = Cell(10)
cell_2 = Cell(12)
cell_3 = Cell(18)
print(cell_1 + cell_2)
print(cell_3 - cell_2)
print(cell_1 * cell_2)
print(cell_2 / cell_1)
cell_1.make_order(4)
