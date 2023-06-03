class QueenPlaces:
    def __init__(self, size):
        self.size = size
        self.resheno = []

    def solve(self):
        rows = [""] * self.size
        self.find_ferz(rows, 0)

    def find_ferz(self, rows, kolonna_index):

        if kolonna_index == self.size:
            self.resheno.append(rows.copy())
            self.show(rows)
            return True
        for colonna in range(self.size):
            if self.check_position(rows, kolonna_index, colonna):
                rows[kolonna_index] = colonna
                self.find_ferz(rows, kolonna_index + 1)

    def check_position(self, rows, kolonna_index, column) -> bool:

        for i in range(kolonna_index):
            if rows[i] == column or rows[i] - i == column - kolonna_index or rows[i] + i == column + kolonna_index:
                return False
        return True

    def show(self, rows: list):
        rows2d = [["Q" if column == rows[row] else "" for column in range(self.size)] for row in range(self.size)]
        print(f"Решение {len(self.resheno)}:")
        for row in rows2d:
            print(row)
        print("\n", "-" * 50, "\n")

if __name__ == '__main__':
    size = 8
    qp = QueenPlaces(size)
    qp.solve()
