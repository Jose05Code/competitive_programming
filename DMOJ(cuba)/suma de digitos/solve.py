def solution():
    n = int(input())
    count = 0
    while n:
        count += bin(n).count('1')
        n -= 1

    print(count)
    
solution()
        