N = int(input())
rating = 0.0
for _ in range(N):
	S, A, T, M = map(float, input().split())
	A, T, M = map(int, (A, T, M, ))
	rating += (S * (1 + 1 / A) * (1 + M / T)) / 4

P = int(input())
ratings = list()
for _ in range(P):
	ratings.append(float(input()))
ratings.sort(reverse=True)

print("The total score of", 
	"Younghoon" if ratings[int((P + 1) * 0.15) - 1] > rating else "Younghoon \"The God\"",
	f"is {rating:.2f}."
	)
