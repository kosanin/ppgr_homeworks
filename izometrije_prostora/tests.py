from main import *

print()
print("eulerA2(-math.atan(1/4), -math.asin(8/9), math.atan(4)")
A = eulerA2(-math.atan(1 / 4), -math.asin(8 / 9), math.atan(4))
print(A)
print("---------------------------------------------------------")

p, phi = axisAngle(A)
print("axisAngle(A)")
print(p, phi)
print("---------------------------------------------------------")

R = rodrigez(p, phi)
print("rodrigez(p, phi)")
print(R)
print("---------------------------------------------------------")

phi1, theta, psi = A2Euler(R.tolist())
print("A2Euler(R)")
print(phi1, theta, psi)
print("---------------------------------------------------------")

q = axisAngle2Q(p, phi)
print("axisAngle2Q(p, phi)")
print(q)
print("---------------------------------------------------------")

p1, phi2 = Q2AxisAngle(q)
print("Q2AxisAngle(q)")
print(p1, phi2)