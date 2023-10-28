rect_x1, rect_y1 = 1, 1
rect_x2, rect_y2 = 4, 4

point_x, point_y = 2, 3

if point_x >= rect_x1 and point_x <= rect_x2 and point_y >= rect_y1 and point_y <= rect_y2:
    print("The point is inside the rectangle.")
else:
    print("The point is outside the rectangle.")