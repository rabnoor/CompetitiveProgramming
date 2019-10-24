import math as k
pi=k.pi
dimension=[float(c) for c in input().split(" ")]
len_wire=dimension[1]
area=dimension[0]
max_area= (len_wire**2)/(4*pi)
if max_area>=area:
    print("Diablo is happy!")
else:
    print("Need more materials!")
