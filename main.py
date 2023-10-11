from pygame import *


WINDOW_SIZE = (512, 512)
FPS = 60
window = display.set_mode(WINDOW_SIZE)
clock = time.Clock()
running = True


class Checker(sprite.Sprite):
    selected_checker = None

    def __init__(self, pos_x, pos_y, color, img, img_scale, king=0, selected=False):
        super().__init__()
        self.isking = king
        self.color = color
        self.img_scale = img_scale
        self.image = transform.scale(image.load(img), (img_scale, img_scale))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.selected = selected

    def update(self, x, y):
        if self.rect.x == x and self.rect.y == y:
            if Checker.selected_checker is not None:
                Checker.selected_checker.selected = False
                Checker.selected_checker.update_image()
            self.selected = True
            Checker.selected_checker = self
            self.update_image()

    def update_image(self):
        if self.selected:
            self.image = transform.scale(image.load('selected.png'), (self.img_scale, self.img_scale))
        else:
            if self.color == 'white':
                self.image = transform.scale(image.load('white.png'), (self.img_scale, self.img_scale))
            else:
                self.image = transform.scale(image.load('black.png'), (self.img_scale, self.img_scale))



matrix = [[0, 2, 0, 2, 0, 2, 0, 2],
        [2, 0, 2, 0, 2, 0, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0]]

checker_group = sprite.Group()
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if matrix[row][column] == 1:
            piece = Checker(column*64, row*64, 'white', 'white.png', 64)
            checker_group.add(piece)
        if matrix[row][column] == 2:
            piece = Checker(column*64, row*64, 'black', 'black.png', 64)
            checker_group.add(piece)

white = 12
black = 12

finished = False
while running:

    if finished == False:
        if black == 0:
            finished = True
            print('white won')
        if white == 0:
            finished = True
            print('black won')

        window.blit(image.load('board.png'), (0, 0))
        checker_group.draw(window)

        for e in event.get(): 
            if e.type == QUIT:
                running = False
            if e.type == MOUSEBUTTONDOWN: # all game logic is in here btw
                for checker in checker_group:
                    if checker.rect.collidepoint(mouse.get_pos()[0], mouse.get_pos()[1]):
                        checker.update(mouse.get_pos()[0]//64*64, mouse.get_pos()[1]//64*64)

                    if checker.selected and not any(checker.rect.collidepoint(mouse.get_pos()[0], mouse.get_pos()[1]) for checker in checker_group):
                        checker.selected = False
                        Checker.selected_checker.selected = False
                        checker.update_image()

                        dx = mouse.get_pos()[0]//64*64 - checker.rect.x
                        dy = mouse.get_pos()[1]//64*64 - checker.rect.y
                        if abs(dx) == abs(dy) and dx != 0 and dy != 0:  # Check if movement is diagonal and not horizontal or vertical
                            if abs(dx) == 64:  # Moved by 1 tile
                                checker.rect.x = mouse.get_pos()[0] // 64 * 64
                                checker.rect.y = mouse.get_pos()[1] // 64 * 64
                            elif abs(dx) == 128:  # Moved by 2 tiles
                                enemy_x = checker.rect.x + dx // 2 # Half the way from the destination point
                                enemy_y = checker.rect.y + dy // 2
                                for enemy_checker in checker_group:
                                    if enemy_checker.rect.x == enemy_x and enemy_checker.rect.y == enemy_y:
                                        if enemy_checker.color != checker.color:  # Check if the enemy tile is of a different color than ours
                                            enemy_checker.kill()  # pow
                                            if enemy_checker.color == 'black':
                                                black -= 1
                                            else: # if white
                                                white -= 1
                                            checker.rect.x = mouse.get_pos()[0] //64*64
                                            checker.rect.y = mouse.get_pos()[1] //64*64
                                        break
    else:
        for e in event.get(): 
            if e.type == QUIT:
                running = False # So you can close it after the game ends.
    clock.tick()
    display.update()
