# This code was written by Aryan Kanak

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import math

# initiate pygame
pygame.init()
# create window and clock
window_width = 1000
window_height = 600
gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Driving Simulator")
clock = pygame.time.Clock()


# car class
class Car:
    speed = 0.0
    angle = math.pi / 2.0

    def __init__(self, img_filepath, x_pos, y_pos):
        self.x_pos = float(x_pos)  # x_pos and y_pos are coordinates of the top centre of the car
        self.y_pos = float(y_pos)
        self.sprite = pygame.image.load(img_filepath).convert_alpha() # filepath for sprite of car

    # change velocity of car
    def accelerate(self, acc, turn):
        self.speed += acc
        self.angle += math.radians(turn)

    # update car position
    def move(self):
        self.x_pos += self.speed * math.cos(self.angle)
        self.y_pos += self.speed * math.sin(self.angle)

    # display car
    def display(self):
        points = [
            (self.x_pos - 10 * math.sin(self.angle), self.y_pos + 10 * math.cos(self.angle)),
            (self.x_pos + 10 * math.sin(self.angle), self.y_pos - 10 * math.cos(self.angle)),
            (self.x_pos + 10 * math.sin(self.angle) + 30 * math.cos(self.angle), self.y_pos - 10 * math.cos(self.angle) + 30 * math.sin(self.angle)),
            (self.x_pos - 10 * math.sin(self.angle) + 30 * math.cos(self.angle), self.y_pos + 10 * math.cos(self.angle) + 30 * math.sin(self.angle))
        ]
        polygon = pygame.draw.polygon(gameDisplay, (0, 0, 0), points)
        gameDisplay.blit(pygame.transform.rotate(self.sprite, -1 * math.degrees(self.angle) + 90), polygon)


# simulation loop
car = Car("car_sprite.png", 500, 300)
end = False
while not end:
    # poll for events
    for event in pygame.event.get():
        # close window
        if event.type == pygame.QUIT:
            end = True

    # get keys pressed
    keys_pressed = pygame.key.get_pressed()
    # turn car
    if car.speed != 0.0:
        if keys_pressed[pygame.K_LEFT]:
            car.accelerate(0.0, 5.0 * math.copysign(1.0, car.speed))
        elif keys_pressed[pygame.K_RIGHT]:
            car.accelerate(0.0, -5.0 * math.copysign(1.0, car.speed))
    # accelerate car
    if keys_pressed[pygame.K_UP]:
        car.accelerate(-0.5, 0.0)
    elif keys_pressed[pygame.K_DOWN]:
        car.accelerate(0.5, 0.0)
    # update car position
    car.move()

    # prevent car from exiting window
    if car.angle % (2 * math.pi) <= math.pi / 2.0:
        if car.x_pos < 10 * math.sin(car.angle):
            car.x_pos = 10 * math.sin(car.angle)
            car.speed = 0.0
        elif car.x_pos > window_width - 10 * math.sin(car.angle) - 30 * math.cos(car.angle):
            car.x_pos = window_width - 10 * math.sin(car.angle) - 30 * math.cos(car.angle)
            car.speed = 0.0
        if car.y_pos < 10 * math.cos(car.angle):
            car.y_pos = 10 * math.cos(car.angle)
            car.speed = 0.0
        elif car.y_pos > window_height - 30 * math.sin(car.angle) - 10 * math.cos(car.angle):
            car.y_pos = window_height - 30 * math.sin(car.angle) - 10 * math.cos(car.angle)
            car.speed = 0.0
    elif car.angle % (2 * math.pi) <= math.pi:
        if car.x_pos < -30 * math.cos(car.angle) + 10 * math.sin(car.angle):
            car.x_pos = -30 * math.cos(car.angle) + 10 * math.sin(car.angle)
            car.speed = 0.0
        elif car.x_pos > window_width - 10 * math.sin(car.angle):
            car.x_pos = window_width - 10 * math.sin(car.angle)
            car.speed = 0.0
        if car.y_pos < -10 * math.cos(car.angle):
            car.y_pos = -10 * math.cos(car.angle)
            car.speed = 0.0
        elif car.y_pos > window_height + 10 * math.cos(car.angle) - 30 * math.sin(car.angle):
            car.y_pos = window_height + 10 * math.cos(car.angle) - 30 * math.sin(car.angle)
            car.speed = 0.0
    elif car.angle % (2 * math.pi) <= 3.0 / 2.0 * math.pi:
        if car.x_pos < -10 * math.sin(car.angle) - 30 * math.cos(car.angle):
            car.x_pos = -10 * math.sin(car.angle) - 30 * math.cos(car.angle)
            car.speed = 0.0
        elif car.x_pos > window_width + 10 * math.sin(car.angle):
            car.x_pos = window_width + 10 * math.sin(car.angle)
            car.speed = 0.0
        if car.y_pos < -30 * math.sin(car.angle) - 10 * math.cos(car.angle):
            car.y_pos = -30 * math.sin(car.angle) - 10 * math.cos(car.angle)
            car.speed = 0.0
        elif car.y_pos > window_height + 10 * math.cos(car.angle):
            car.y_pos = window_height + 10 * math.cos(car.angle)
            car.speed = 0.0
    else:
        if car.x_pos < -10 * math.sin(car.angle):
            car.x_pos = -10 * math.sin(car.angle)
            car.speed = 0.0
        elif car.x_pos > window_width - 30 * math.cos(car.angle) + 10 * math.sin(car.angle):
            car.x_pos = window_width - 30 * math.cos(car.angle) + 10 * math.sin(car.angle)
            car.speed = 0.0
        if car.y_pos < 10 * math.cos(car.angle) - 30 * math.sin(car.angle):
            car.y_pos = 10 * math.cos(car.angle) - 30 * math.sin(car.angle)
            car.speed = 0.0
        elif car.y_pos > window_height - 10 * math.cos(car.angle):
            car.y_pos = window_height - 10 * math.cos(car.angle)
            car.speed = 0.0

    # draw car
    gameDisplay.fill((0, 0, 0))
    car.display()
    pygame.display.update()
    # tick clock
    clock.tick(30)
