from pygame import *


WINDOW_SIZE = (512, 512)
FPS = 60
window = display.set_mode(WINDOW_SIZE)
clock = time.Clock()
running = True


class Checker(sprite.Sprite):
    def __init__(self, pos_x, pos_y, color, img, img_scale, king=0):
        super().__init__()
        self.isking = king
        self.color = color
        self.image = transform.scale(image.load(img), (img_scale, img_scale))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

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
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if matrix[row][column] == 1:
            piece = Checker(column*64, row*64, 'white', 'white.png', 64)
            checker_group.add(piece)
        if matrix[row][column] == 2:
            piece = Checker(column*64, row*64, 'black', 'black.png', 64)
            checker_group.add(piece)


while running:
    for e in event.get():
        if e.type == QUIT:
            running = False  
    window.blit(image.load('board.png'), (0, 0))
    checker_group.draw(window)

    clock.tick()
    display.update()