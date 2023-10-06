from pygame import *


WINDOW_SIZE = (512, 512)
FPS = 60
window = display.set_mode(WINDOW_SIZE)
clock = time.Clock()
running = True


class Checker(sprite.Sprite):
    def __init__(self, pos_x, pos_y, color, img, image_scale, king=0):
        super().__init__()
        self.isking = king
        self.color = color
        """        self.image = transform.scale(image.load(img), (img_scale))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y """

    def move(self):
        pass

matrix = [[0, 1, 0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [2, 0, 2, 0, 2, 0, 2, 0],
          [0, 2, 0, 2, 0, 2, 0, 2],
          [2, 0, 2, 0, 2, 0, 2, 0]]

checker_group = sprite.Group()
for row in matrix:
    for column in row:
        if column == 1:
            peice = Checker(matrix[column], matrix[row], 'white', '', 64)
        if column == 2:
            peice = Checker(matrix[column], matrix[row], 'black', '', 64)
    checker_group.add(peice)

print(checker_group)
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False  
    window.fill((0, 0, 0))


    clock.tick()
    display.update()