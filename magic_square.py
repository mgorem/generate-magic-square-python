# Defining a fuction named magic square
def magic_square(matrix_ms):
    iSize = len(matrix_ms[0])
    sum_list = []

    # Vertical squares
    for col in range(iSize):
        sum_list.append(sum(row[col] for row in matrix_ms))

    # Horizontal squares
        sum_list.extend([sum (lines) for lines in matrix_ms])

        dlResult = 0
        for i in range(0,iSize):
            dlResult +=matrix_ms[i][i]
        sum_list.append(dlResult)
        drResult = 0
        for i in range(iSize-1,-1,-1):
            drResult +=matrix_ms[i][i]
        sum_list.append(drResult)
        if len(set(sum_list))>1:
            return False
        return True

        print(magic_square([[1,2,3], [4,5,6], [7,8,9]]))