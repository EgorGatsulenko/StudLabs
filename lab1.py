import numpy as np
import matplotlib.pyplot as plt

x = float(input("x ="))
y = float(input("y ="))
z = float(input("z ="))
if - 1 <= z <= 1:
    s = np.sqrt(10  * (np.cbrt(x) + x ** (y + 2))) * ((np.asin(z) ** 2) - np.fabs(x))
    print("s =", s)
else:
    print("Ошибка")
