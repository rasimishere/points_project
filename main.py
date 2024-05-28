class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

def main():
    num_points = int(input("how many points need to be created: "))

for i in range(num_points):
    print(f"Enter coordinates for point {i+1}:")
    x = float(input(" x: "))
    y = float(input(" y: "))
    points.append(Point(x, y))

print(\nThe points you entered are:)
for point in points:
    print(point)
    
if __name__ == "__main__":
    main()
