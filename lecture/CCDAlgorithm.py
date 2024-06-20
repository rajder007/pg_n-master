class Rectangle:
    def __init__(self, x, y, width, height, velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity

    def move(self, dt):
        self.x += self.velocity[0] * dt
        self.y += self.velocity[1] * dt

def CCD(rect1, rect2):
    # Interpolacja pomiędzy pozycjami początkową i końcową obiektów
    start_rect1 = (rect1.x, rect1.y)
    end_rect1 = (rect1.x + rect1.velocity[0], rect1.y + rect1.velocity[1])

    start_rect2 = (rect2.x, rect2.y)
    end_rect2 = (rect2.x + rect2.velocity[0], rect2.y + rect2.velocity[1])

    # Interpolacja czasowa
    dt = 0.01  
    
    # Sprawdzenie kolizji dla każdej klatki czasowej pomiędzy pozycjami początkową i końcową
    t = 0
    while t <= 1:
        x_rect1 = start_rect1[0] + (end_rect1[0] - start_rect1[0]) * t
        y_rect1 = start_rect1[1] + (end_rect1[1] - start_rect1[1]) * t

        x_rect2 = start_rect2[0] + (end_rect2[0] - start_rect2[0]) * t
        y_rect2 = start_rect2[1] + (end_rect2[1] - start_rect2[1]) * t

        # Sprawdzenie, czy prostokąty nachodzą na siebie
        if (abs(x_rect1 - x_rect2) * 2 < (rect1.width + rect2.width)) and \
           (abs(y_rect1 - y_rect2) * 2 < (rect1.height + rect2.height)):
            return True  # Kolizja została wykryta

        t += dt

    return False  # Nie wykryto kolizji

# Przykładowe użycie
# Utworzenie dwóch prostokątów z pozycjami, wymiarami i prędkościami
rect1 = Rectangle(0, 0, 10, 10, (5, 0))
rect2 = Rectangle(20, 0, 10, 10, (-5, 0))

# Wywołanie CCD
collision = CCD(rect1, rect2)
print("Czy wystąpiła kolizja?", collision)