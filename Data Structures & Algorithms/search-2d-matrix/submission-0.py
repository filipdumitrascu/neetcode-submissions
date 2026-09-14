class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """Linear Search

        Un approach brute force este sa nu tinem cont de faptul ca liniile sunt
        sortate intre ele si ele in sine si sa facem o scanare liniara prin
        toata matricia cu care sa gasim elementul.

        T = O(m * n), S = O(1)
        """
        # for row in range(len(matrix)):
        #     for column in range(len(matrix[0])):
        #         if matrix[row][column] == target:
        #             return True
        # return False



        """Binary Search

        Pentru ca matricea are liniile ordonate si sortate, intreaga matrice
        se poate comporta ca un array mare. Ordinea elementelor intr un array 
        neschimbandu-se, acesta ramane sortat si se poate aplica cautare binara
        pentru a gasi targetul in timp logaritmic. Se cauta de la index 0 la
        ROWS * COLS - 1. Pnetru fiecare mid index m, putem mapa elementul inapoi
        in matrice astfel:

        row = m // COLS
        col = m % COLS
        Asa putem accesa corect elementul fara sa facem efectiv transformarea
        in array.

        T = O(log(m * n)), S = O(1)
        """
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols

        while left < right:
            mid = left + (right - left) // 2

            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True

            if target > matrix[row][col]:
                left = mid + 1
            else:
                right = mid

        return False
