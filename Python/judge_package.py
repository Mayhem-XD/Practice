import calcpkg.operation as op
import calcpkg.geometry as geo
num = int(input())
sqrt = op.squareroot(num)
area = geo.circle_area(num)
print(sqrt)
print(area)