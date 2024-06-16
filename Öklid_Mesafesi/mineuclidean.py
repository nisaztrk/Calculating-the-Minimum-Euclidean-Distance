import math
# Minimum Öklid Mesafesinin Hesaplanması
"""
Noktaların Tanımlanması:

‘points’ adında bir liste oluşturun.
Bu liste, 2D uzaydaki noktaları temsil eden demetler (tuple) içermelidir. 
Örneğin, ‘(x, y)’ noktası bir demet ‘(x, y)’ olarak temsil edilecektir.
"""
points=[(1,2), (4,6), (-1,0), (5,4)]

"""
Öklid Mesafesi İçin Bir Fonksiyon Yazma:

‘euclideanDistance’ adında bir fonksiyon tanımlayın.
Bu fonksiyon, iki demet (her biri bir noktayı temsil eder) almalı 
ve bu iki nokta arasındaki Öklid mesafesini döndürmelidir.
"""
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)
# En başta import math yazmasaydık math.sqrt yerine içeriye yazdığımız fonksiyonun 0.5 üssünü (**0.5) alabilirdik.
# return ((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)**0.5 şeklinde

"""
Mesafelerin Hesaplanması:

Bir döngü kullanarak, ‘points’ listesindeki her nokta çifti arasındaki Öklid mesafesini hesaplayın.
Bu mesafeleri ‘distances’ adında başka bir listede saklayın.
""" 
distances=[]
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)

# Sonuçların yazdırılması
print(f"Noktalar arasındaki Öklid mesafeleri: {distances}")
print(f"Minimum Öklid mesafesi: {min_distance}")
