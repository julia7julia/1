width=float(input())
length=float(input())
spend=float(input())
volume=int(input())
reserve=int(input())
paint_sq=round(width*length,2)
print(paint_sq)
paint_vol=round(paint_sq/spend+paint_sq/spend*reserve/100,2)
print(paint_vol)
can=int(paint_vol/volume+1)
print(can)
leftover=round(can*volume-paint_vol,2)
print(leftover)