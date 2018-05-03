tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(colWidths)):
        colWidths[i] = max(map(len, tableData[i]))
    colWidth = max(colWidths)
    index = 0
    while index < len(tableData[0]):
        for i in range(len(tableData)):
            print(tableData[i][index].rjust(colWidth), end='')
        index += 1
        print()

print_table(tableData)
