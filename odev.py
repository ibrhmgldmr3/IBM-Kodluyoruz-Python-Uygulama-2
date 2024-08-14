import math

# Noktaların Tanımlanması
points = [(1, 2), (3, 4), (6, 8), (10, 12)]


# Öklid Mesafesi İçin Bir Fonksiyon 
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Mesafelerin Hesaplanması İçin Döngü
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunması
min_distance = min(distances)
 
 
# Sonuçların Yazdırılması
print("Hesaplanan Mesafeler: ", distances)
print("Minimum Mesafe: ", min_distance)
