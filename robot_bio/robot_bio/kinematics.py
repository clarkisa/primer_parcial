import math

def calcular_angulos(x, y, z):
    L = 1.5

    r = math.sqrt(x**2 + y**2)
    z_p = z - 2*L

    theta1 = math.atan2(y, x)

    D = (r**2 + z_p**2 - L**2 - L**2) / (2*L*L)

    # evitar error numérico
    if D > 1: D = 1
    if D < -1: D = -1

    theta3 = math.acos(D)

    theta2 = math.atan2(z_p, r) - math.atan2(L*math.sin(theta3), L + L*math.cos(theta3))

    return theta1, theta2, theta3