N = 8
board = [-1] * N

def solve(row):
    if row == N:
        for r in range(N):
            print(" ".join(
                "Q" if board[r] == c else "."
                for c in range(N)
            ))
        return True

    for col in range(N):
        if all(
            board[r] != col and
            abs(board[r] - col) != abs(r - row)
            for r in range(row)
        ):
            board[row] = col
            if solve(row + 1):
                return True
    return False

solve(0)
