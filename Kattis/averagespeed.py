import sys as sys
dist_time={}
speed=0.0
time_beg=0.0
dist=0.0
for i in sys.stdin:
    i = str(i).strip()

    details=[f for f in i.split(" ")]
    r_details = [float(g) for g in details[0].split(":")]
    time=1*r_details[0]+r_details[1]/60+r_details[2]/3600
    a=float((time-time_beg)*speed+dist)
    d=format(a,'.2f')
    dist_time[details[0]]=d
    dist=a
    time_beg=time
    if len(details)==2:
        speed=float(details[1])
    else:
        print(details[0],dist_time[details[0]],"km")
