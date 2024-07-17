Ca, Ba, Pa, = map(int, input().split())
Cr, Br, Pr, = map(int, input().split())
Cs = Cr - Ca if Cr > Ca else 0
Bs = Br - Ba if Br > Ba else 0
Ps = Pr - Pa if Pr > Pa else 0

print(Cs + Bs + Ps)