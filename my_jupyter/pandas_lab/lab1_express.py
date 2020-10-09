#python expression test

xy_list = [x*y for x in range(10) for y in range(x, x+10)]

print(xy_list[:])