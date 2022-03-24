class Solution:

    def _get_board_dimensions(self, board):
        """
            (n, m)
        """
        return (len(board) , len(board[0]))

    def _put_single_square(self, board, row, col, marker_value) -> bool:
        (n,m) = self._get_board_dimensions(board)
        # the figure cannot fit in the matrix
        if row < 0 or col < 0 or row >= n or col > m:
            return False

        if board[row][col] != 0:
            return False
        else:
            board[row][col] = marker_value
            return True

    def _put_horizontal_line(self, board, row, col, marker_value) -> bool:
        (n,m) = self._get_board_dimensions(board)

        # the figure cannot fit in the matrix
        if row < 0 or col < 0 or row >= n or col + 2 >= m:
            return False

        if board[row][col] != 0 or board[row][col + 1] != 0 or board[row][col + 2] != 0:
            return False
        else:
            board[row][col] = board[row][col + 1] = board[row][col + 2] = marker_value
            return True


    def _put_double_square(self, board, row, col, marker_value) -> bool:
        (n,m) = self._get_board_dimensions(board)

        # the figure cannot fit in the matrix
        if row < 0 or col < 0 or row + 1 >= n or col + 1 >= m:
            return False

        if board[row][col] != 0 or board[row][col + 1] != 0 or board[row + 1][col] != 0 or board[row + 1][col + 1] != 0:
            return False
        else:
            board[row][col] = board[row][col + 1] =  board[row + 1][col] = board[row + 1][col + 1] = marker_value
            return True

    def _put_right_triangle(self, board, row, col, marker_value) -> bool:
        (n,m) = self._get_board_dimensions(board)

        # the figure cannot fit in the matrix
        if row < 0 or col < 0 or row + 2 >= n or col + 1 >= m:
            return False

        if board[row][col] != 0 or board[row + 1][col] != 0 or board[row + 2][col] != 0 or board[row + 1][col + 1] != 0:
            return False
        else:
            board[row][col] = board[row + 1][col] = board[row + 2][col] = board[row + 1][col + 1] = marker_value
            return True

    def _put_upper_triangle(self, board, row, col, marker_value) -> bool:
        (n,m) = self._get_board_dimensions(board)

        # the figure cannot fit in the matrix
        if row - 1 < 0 or col < 0 or row >= n or col + 2 >= m:
            return False

        if board[row][col] != 0 or board[row][col + 1] != 0 or board[row][col + 2] != 0 or board[row - 1][col + 1] != 0:
            return False
        else:
            board[row][col] = board[row][col + 1] = board[row][col + 2] = board[row - 1][col + 1] = marker_value
            return True

    def _put_figure_on_board(self, board, figure_type, row, col, marker_value) -> bool:
        if figure_type == 1:
            return self._put_single_square(board, row, col, marker_value)
        elif figure_type == 2:
            return self._put_horizontal_line(board, row, col, marker_value)
        elif figure_type == 3:
            return self._put_double_square(board, row, col, marker_value)
        elif figure_type == 4:
            return self._put_right_triangle(board, row, col, marker_value)
        elif figure_type == 5:
            return self._put_upper_triangle(board, row, col, marker_value)

    def _init_board(self, cols, rows):
        return [[0 for i in range(cols)] for j in range(rows)]

    def _print_board(self, board):
        for row in board:
            print(row)
        print('------------------------------')

    def _place_all(self, board, figures, curr_row, curr_col) -> bool:
        (n,m) = self._get_board_dimensions(board)
        fig_index = 0

        for figure in figures:
            fig_index += 1
            start = curr_col + curr_row * m
            for index in range(start, m * n):
                row = index // m
                col = index % m
                # break if the field is empty and we have succeeded in putting the figure
                if board[row][col] == 0 and self._put_figure_on_board(board, figure, row, col, fig_index):
                    break

    def almostTetris(self, n: int, m: int, figures):
        board = self._init_board(n, m)

        self._place_all(board, figures, 0, 0)

        self._print_board(board)

# ------------------------------------------------------------------------------------------
# solution in leetcode.com

def almostTetris(n, m, figures):
    grid = [[0] * m for _ in range(n)]

    shapes = {
        1: [(0,0)],
        2: [(0,0),(0,1),(0,2)],
        3: [(0,0),(0,1),(1,0),(1,1)],
        4: [(0,0),(1,0),(1,1),(2,0)],
        5: [(0,0),(0,1),(-1,1),(0,2)],
    }

    def checkShapeFit(x,y,shape_no, number):
        for (i,j) in shapes[shape_no]:
            if(x+i)>=n or (y+j)>=m or (x+i)<0 or (y+j)<0 or grid[x+i][y+j]!=0:
                return False

        for i,j in shapes[shape_no]:
            grid[x+i][y+j] = number

        return True

    def getAvailable():
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 0:
                    if checkShapeFit(row,col,f, i+1):
                        return

    for i, f in enumerate(figures):
        getAvailable()

    return grid
# -------------------------------------------------------------------------------

def print_board(board):
    for row in board:
        print(row)
    print('------------------------------')

if __name__ == '__main__':
    figures = [4, 2, 1, 3]
    print(f'Figures: {figures}')
    s = Solution()
    s.almostTetris(4, 4, figures)

    board = almostTetris(4, 4, figures)
    print_board(board)
