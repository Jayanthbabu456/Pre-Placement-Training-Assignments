# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

# **Example 1:**
# **Input:** coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

# **Output:** true

def checkStraightLine(coordinates):
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    if x2 - x1 == 0:
        slope = float('inf')
    else:
        slope = (y2 - y1) / (x2 - x1)

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        if x - x1 == 0:
            curr_slope = float('inf')
        else:
            curr_slope = (y - y1) / (x - x1)

        if slope != curr_slope:
            return False

    return True


n = int(input())
coordinates = []
for i in range(n):
    x = int(input())
    y = int(input())
    coordinates.append([x, y])

print(checkStraightLine(coordinates))
