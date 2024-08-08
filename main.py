def solve(N: int, A: list[int]) -> int:
    ans = 0
    for i in range(N):
        ans += A[i]
    print(ans)

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    solve(N, A)
