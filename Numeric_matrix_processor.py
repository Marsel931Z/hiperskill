class Menu():
    
    def __init__(self):
        print('1. Add matrices')
        print('2. Multiply matrix by a constant')
        print('3. Multiply matrices')
        print('4. Transpose matrix')
        print('5. Calculate a determinant')
        print('0. Exit')
        self.choise = int(input('Your choice: '))
        if self.choise == 1:
            AddMatrices()
        elif self.choise == 2:
            MultiplyConstant()
        elif self.choise == 3:
            MultiplyMatrices()
        elif self.choise == 4:
            TransposeMatrix()
        elif self.choise == 5:
            CalculateDeterminant()
        elif self.choise == 6:
            InverseMatrix()
        elif self.choise == 0:
            exit(1)
        else:
            Menu()

class AddMatrices():
    
    def __init__(self):
        self.size1 = input('Enter size of first matrix: ')
        self.splitsize1 = self.size1.split()
        self.first_matrix = []
        print('Enter first matrix: ')
        for j in range(0, int(self.splitsize1[0])):
            j = input()
            self.first_matrix.append(j.split())
        self.size2 = input('Enter size of second matrix: ')
        self.splitsize2 = self.size2.split()
        self.second_matrix = []
        print('Enter second matrix: ')
        for i in range(0, int(self.splitsize2[0])):
            i = input()
            self.second_matrix.append(i.split())
        self.sum_matrix = []
        if len(self.first_matrix) == len(self.second_matrix):
            if len(self.first_matrix[0]) == len(self.second_matrix[0]):
                for k in range(0, len(self.first_matrix)):
                    self.sum_matrix.append([])
                    for t in range(0, len(self.first_matrix[k])):
                        self.sum_matrix[k].append(str(float(self.first_matrix[k][t]) + float(self.second_matrix[k][t])))
                print('The result is: ')
                for l in range (0, len(self.first_matrix)):
                    print(' '.join(self.sum_matrix[l])) 
            else:
                print("The operation cannot be performed.")
        else:
            print("The operation cannot be performed.")
        Menu()
        
class MultiplyConstant():
    
    def __init__(self):
        self.size = input('Enter size of matrix: ')  
        self.splitsize = self.size.split()
        self.matrix = []
        print('Enter matrix: ')
        for i in range(0, int(self.splitsize[0])):
            i = input()
            self.matrix.append(i.split())
        self.const = float(input('Enter constant: '))
        print('The result is: ')
        for q in range(0, len(self.matrix)):
            for w in range(0, len(self.matrix[q])):
                self.matrix[q][w] = str(float(self.matrix[q][w]) * self.const)
            print(' '.join(self.matrix[q]))
        Menu()

class MultiplyMatrices():
    
    def __init__(self):
        self.size1 = input('Enter size of first matrix: ')
        self.splitsize1 = self.size1.split()
        self.first_matrix = []
        print('Enter first matrix: ')
        for j in range(0, int(self.splitsize1[0])):
            j = input()
            self.first_matrix.append(j.split())
        self.size2 = input('Enter size of second matrix: ')
        self.splitsize2 = self.size2.split()
        self.second_matrix = []
        print('Enter second matrix: ')
        for i in range(0, int(self.splitsize2[0])):
            i = input()
            self.second_matrix.append(i.split())  
        self.mult_matrix = []
        if self.splitsize1[1] == self.splitsize2[0]:
            self.second_matrix = [[self.second_matrix[j][i] for j in range(len(self.second_matrix))] for i in range(len(self.second_matrix[0]))]
            for j in range(0, len(self.first_matrix)):
                self.mult_matrix.append([])
                for a in range (0, len(self.second_matrix)):
                    suma = 0
                    for k in range(0, len(self.first_matrix[j])):
                        q = float(self.first_matrix[j][k]) * float(self.second_matrix[a][k])
                        suma += q
                    self.mult_matrix[j].append(round(suma, 2))
            print('The result is: ')
            for q in range(0, len(self.mult_matrix)):
                for w in range (0, len(self.mult_matrix[q])):
                    self.mult_matrix[q][w] = str(self.mult_matrix[q][w])
                print(' '.join(self.mult_matrix[q]))  
        else:
            print('The operation cannot be performed.')
        Menu()    

class TransposeMatrix():
    
    def __init__(self):
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        self.choise1 = int(input('Your choice: '))
        if self.choise1 == 1:
            TransposeMatrix.maindiag()
        elif self.choise1 == 2:
            TransposeMatrix.sidediag()
        elif self.choise1 == 3:
            TransposeMatrix.vert()
        elif self.choise1 == 4:
            TransposeMatrix.horiz()
        else:
            Menu()
            
    def maindiag():
        size = input('Enter size of matrix: ')  
        splitsize = size.split()
        matrix = []
        print('Enter matrix: ')
        for i in range(0, int(splitsize[0])):
            i = input()
            matrix.append(i.split())
        matrix = [[matrix[j][i] for j in range(0, len(matrix))] for i in range(0, len(matrix[0]))]
        for q in range(0, len(matrix)):
            print(' '.join(matrix[q]))
        Menu()
    
    def sidediag():
        size = input('Enter size of matrix: ')  
        splitsize = size.split()
        matrix = []
        print('Enter matrix: ')
        for i in range(0, int(splitsize[0])):
            i = input()
            matrix.append(i.split())
        matrix = [[matrix[j][i] for j in range(len(matrix) - 1, -1, -1)] for i in range(len(matrix[0]) - 1, -1, -1)]
        for q in range(0, len(matrix)):
            print(' '.join(matrix[q]))
        Menu()
        
    def horiz():
        size = input('Enter size of matrix: ')  
        splitsize = size.split()
        matrix = []
        print('Enter matrix: ')
        for i in range(0, int(splitsize[0])):
            i = input()
            matrix.append(i.split())
        matrix = [[matrix[i][j] for j in range(0, len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]
        for q in range(0, len(matrix)):
            print(' '.join(matrix[q]))
        Menu()
        
    def vert():
        size = input('Enter size of matrix: ')  
        splitsize = size.split()
        matrix = []
        print('Enter matrix: ')
        for i in range(0, int(splitsize[0])):
            i = input()
            matrix.append(i.split())
        matrix = [[matrix[i][j] for j in range(len(matrix) - 1, -1, -1)] for i in range(0, len(matrix[0]))]
        for q in range(0, len(matrix)):
            print(' '.join(matrix[q]))
        Menu()
        
class CalculateDeterminant():
    
    def __init__(self):
        self.size = input('Enter size of matrix: ')  
        self.splitsize = self.size.split()
        if self.splitsize[0] != self.splitsize[1]:
            print('The operation cannot be performed.')
        else:
            self.matrix = []
            print('Enter matrix: ')
            for i in range(0, int(self.splitsize[0])):
                i = input()
                self.matrix.append(i.split())
            print('The result is:')
            print(CalculateDeterminant.determinant(self.matrix, 1))
        print()
        Menu()
        
    def determinant(matrix, minor):
        width = len(matrix)
        if width == 1:
            return float(minor) * float(matrix[0][0])
        else:
            sign = -1
            sum = 0
            for i in range(width):
                mat_new = []
                for j in range(1, width):
                    mat_list = []
                    for k in range(width):
                        if k != i:
                            mat_list.append(matrix[j][k])
                    mat_new.append(mat_list)
                sign *= -1
                sum += float(minor) * float(CalculateDeterminant.determinant(mat_new, sign * float(matrix[0][i])))
            return sum

class InverseMatrix():
    
    def __init__(self):
        self.size = input('Enter size of matrix: ')  
        self.splitsize = self.size.split()
        if self.splitsize[0] != self.splitsize[1]:
            print('The operation cannot be performed.')
        else:
            self.matrix = []
            print('Enter matrix: ')
            for i in range(0, int(self.splitsize[0])):
                i = input()
                self.matrix.append(i.split())
            print('The result is:')
            if InverseMatrix.getMatrixDeternminant(self.matrix) != 0:
                for q in range(0, len(InverseMatrix.getMatrixInverse(self.matrix))):
                    print(' '.join(InverseMatrix.getMatrixInverse(self.matrix)[q]))
            else:
                print("This matrix doesn't have an inverse.")
            Menu()
            
    def transposeMatrix(m):
        return [[m[j][i] for j in range(0, len(m))] for i in range(0, len(m[0]))]

    def getMatrixMinor(m,i,j):
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

    def getMatrixDeternminant(m):
        if len(m) == 2:
            return float(m[0][0])*float(m[1][1])-float(m[0][1])*float(m[1][0])
        determinant = 0
        for c in range(len(m)):
            determinant += ((-1)**c)*float(m[0][c])*InverseMatrix.getMatrixDeternminant(InverseMatrix.getMatrixMinor(m,0,c))
        return determinant

    def getMatrixInverse(m):
        determinant = InverseMatrix.getMatrixDeternminant(m)
        if len(m) == 2:
            return [[float(m[1][1])/determinant, -1*float(m[0][1])/determinant],
                    [-1*float(m[1][0])/determinant, float(m[0][0])/determinant]]
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = InverseMatrix.getMatrixMinor(m,r,c)
                cofactorRow.append(((-1)**(r+c)) * InverseMatrix.getMatrixDeternminant(minor))
            cofactors.append(cofactorRow)
        cofactors = InverseMatrix.transposeMatrix(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = str(round(float(cofactors[r][c])/determinant, 3))
        return cofactors

Menu()
