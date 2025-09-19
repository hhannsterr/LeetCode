class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells[cell] = 0

    def getValue(self, formula: str) -> int:
        def getCellValue(xy: str) -> int:
            if xy.isdigit():
                return int(xy)
            else:
                if xy in self.cells:
                    return self.cells[xy]
                else:
                    return 0
        

        x, y = formula[1:].split('+')
        x_val = getCellValue(x)
        y_val = getCellValue(y)
        return x_val + y_val


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)