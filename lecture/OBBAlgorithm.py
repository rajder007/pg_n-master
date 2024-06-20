import pygame
import numpy as np
# w przypadki gdy nie ma biblioteki skimage: pip install scikit-image
import skimage, os
import matplotlib.pyplot as plt

class DetectObject:
    def __init__(self, path, scale) -> None:
        self.img = skimage.io.imread(path)
        height, width, _ = self.img.shape
        self.img = skimage.transform.resize(self.img,( height / scale, width / scale) )
        # rgb = skimage.color.rgba2rgb(self.img)
        # gray = skimage.color.rgb2gray(rgb)
        # gray = skimage.filters.gaussian(gray, sigma=0.1)
        # corners = skimage.feature.corner_harris(gray)
        # points = skimage.feature.corner_peaks(skimage.feature.corner_harris(corners), min_distance=1,threshold_abs=0.001,threshold_rel=0.01)
        # print('{} corners were found in the image.'.format(len(points)))
        # #Let's mark these detected corners on the image with red marker:
        # plt.imshow(gray, cmap='gray')
        # plt.plot(points[:,1], points[:,0], '+r', markersize=15)
        # plt.axis('off')
        # plt.show()
        # print(points)

    def get_corners(self):
        rgb = skimage.color.rgba2rgb(self.img)
        gray = skimage.color.rgb2gray(rgb)
        gray = skimage.filters.gaussian(gray, sigma=0.1)
        corners = skimage.feature.corner_harris(gray)
        points = skimage.feature.corner_peaks(skimage.feature.corner_harris(corners), min_distance=1,threshold_abs=0.001,threshold_rel=0.01)
        return points

# detect_object = DetectObject(os.path.join( "assets", "ship.png"), 2)
# rectangle_points = detect_object.get_corners()




pygame.init()

# # Ustawienie wielkości ekranu
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Oriented Bounding Box Example")

# # Kolory
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# # Funkcja do obliczania OBB
def calculate_obb(points):
#     # Obliczamy centroid
    centroid = np.mean(points, axis=0)
    
#     # Obliczamy macierz kowariancji i wartości własne
    covariance_matrix = np.cov(points.T)
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    
#     # Obrót na podstawie głównej osi
    rotation_matrix = eigenvectors.T
    rotated_points = np.dot(points - centroid, rotation_matrix)
    
#     # Obliczamy min i max dla każdego wymiaru
    obb_min = np.min(rotated_points, axis=0)
    obb_max = np.max(rotated_points, axis=0)
    
#     # Obliczamy rozmiar OBB
    obb_size = obb_max - obb_min
    
    return centroid, rotation_matrix, obb_size

# # Rysowanie OBB
def draw_obb(centroid, rotation_matrix, obb_size):
    # Wierzchołki OBB
    half_size = obb_size / 2.0
    vertices = np.array([
        [-half_size[0], -half_size[1]],
        [half_size[0], -half_size[1]],
        [half_size[0], half_size[1]],
        [-half_size[0], half_size[1]]
    ])
    
#     # Obrót wierzchołków
    rotated_vertices = np.dot(vertices, rotation_matrix) + centroid
    
#     # Rysowanie linii OBB
    pygame.draw.polygon(screen, RED, rotated_vertices, 2)

# # Początkowe punkty prostokąta
rectangle_points = np.array([
    [200, 200],
    [300, 200],
    [300, 300],
    [200, 300]
])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(WHITE)
    
    # Obliczanie i rysowanie OBB
    centroid, rotation_matrix, obb_size = calculate_obb(rectangle_points)
    draw_obb(centroid, rotation_matrix, obb_size)
    
    # # Rysowanie prostokąta
    pygame.draw.polygon(screen, (0, 0, 0), rectangle_points, 2)
    
    pygame.display.flip()

# Zakończenie programu
pygame.quit()