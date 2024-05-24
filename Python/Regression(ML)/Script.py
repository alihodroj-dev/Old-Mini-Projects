# Variables
lineXPoints = []
lineYPoints = []
points = [[1, 1], [1, 2], [3, 3], [5, 1], [3, 2], [2, 3], [1, 3], [2, 4], [3, 7], [6, 4]]
inputs = [[7, 8], [2, 3], [6, 1], [5, 4]]
firstPoint = points[0]
highestX = firstPoint[0]
highestY = firstPoint[1]
averageX = 0
averageY = 0

# Calculating average
for point1 in points:
    averageX += point1[0]
    averageY += point1[1]
averageX = int(averageX / len(points))
averageY = int(averageY / len(points))

# Deleting far points
for point2 in points:
    if point1[0] - averageX >= 4 or point2[1] - averageY >= 4:
        points.remove(point2)

# Getting highest X and Y
for point3 in points:
    if point3[0] > highestX:
        highestX = point3[0]
    if point3[1] > highestY:
        highestY = point3[1]

# Calculating line points
for x in range(0, highestX):
    lineXPoints.append(highestX - x)
    lineYPoints.append(x)

# Deciding for new point
def decide(newNumX, newNumY):
    decision = "Blue"
    for y in range(0, len(lineXPoints)):
        if newNumX > lineXPoints[y] and newNumY > lineYPoints[y]:
            decision = "Green"
            break
    return "Point " + str(newNumX) + "," + str(newNumY) + " is " + decision

# Outputing
for inp in inputs:
    print(decide(inp[0], inp[1]))