import math

a = 7
areaCube = math.floor(6 * math.pow(a,2))
volumeCube = math.floor(math.pow(a,3))

r = 9
areaSphere = math.floor(4 * math.pi * math.pow(r,2))
volumeSphere = math.floor(4/3  * math.pi * math.pow(r,3))

print(f"Area of Cube: {areaCube}")
print(f"Volume of Cube: {volumeCube}")

print(f"Area of Sphere: {areaSphere}")
print(f"Volume of Sphere: {volumeSphere}")

