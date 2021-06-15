import moistweight
import math

IF = math.radians(3)
SA = math.atan(0.1)
cs = 2.5

wg = moistweight.Weight(50)

γw = wg[0]
γt = wg[1]
γs = wg[2]

print(wg)

D = 3
d = 0.06
x = (math.cos(SA))**2

N1 = (cs - (γw*d*x*(math.tan(IF))))
z1 = (γt*(D-d))+(γs*d)
z2 = (math.cos(SA))*(math.sin(SA))
D1 = z1*z2

N2 = math.tan(IF)
D2 = math.tan(SA)

SF = (N1/D1) + (N2/D2)
SF = round(SF,5)
print(SF)