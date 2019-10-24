import math as m

test_cases = int(input())
for i in range(test_cases):
    c = [float(x) for x in input().split(" ")]
    center = [x for x in c[0:3]]
    radius = c[3]
    velocity_vector = [x for x in c[4:]]
    # print(velocity_vector)
    c1 = [float(x) for x in input().split(" ")]
    center1 = [x for x in c1[0:3]]
    radius1 = c1[3]
    velocity_vector1 = [x for x in c1[4:]]
    # print(velocity_vector1)
    del_x = center1[0] - center[0]
    del_y = center1[1] - center[1]
    del_z = center1[2] - center[2]
    c=(del_x**2)+(del_y**2)+(del_z**2)-((radius1+radius)**2)
    del_vx= velocity_vector[0]-velocity_vector1[0]
    del_vy = velocity_vector[1] - velocity_vector1[1]
    del_vz = velocity_vector[2] - velocity_vector1[2]
    a= del_vx**2+del_vy**2+del_vz**2
    b=2*((del_x*del_vx)+(del_y*del_vy)+(del_z*del_vz))
    timea=0
    if ((b**2)-4*a*c)>=0 and a!=0:

            timea+= ((-1*b)+m.sqrt((b**2)-4*a*c))/(-2*a)

    if timea>0:
        print(timea)
    else:
        print("No collision")
