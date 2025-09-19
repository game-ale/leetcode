
class Spreadsheet:
    def __init__(self, rows: int):
        self.cells = {}  # map cell_string -> int

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.cells:
            del self.cells[cell]

    def getValue(self, formula: str) -> int:
        # formula like "=A1+B2" or "=5+A1" or "=10+20"
        # Remove leading '='
        expr = formula[1:]
        left, right = expr.split('+')
        return self._getToken(left) + self._getToken(right)

    def _getToken(self, token: str) -> int:
        if token[0].isdigit():
            return int(token)
        else:
            return self.cells.get(token, 0)

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)