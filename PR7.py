N = 4
board = [-1] * N

def safe(r, c):
    for i in range(r):
        if board[i] == c or abs(board[i] - c) == abs(i - r):
            return False
    return True

def solve(r):
    if r == N:
        return True

    for c in range(N):
        if safe(r, c):
            board[r] = c

            if solve(r + 1):
                return True

            board[r] = -1

    return False

solve(0)

for r in range(N):
    for c in range(N):
        if board[r] == c:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()
    
    