N = int(input())

grades = [int(n) for n in input().split()]

avg = sum(grades) / N
print(avg / (max(grades) / 100))