import pygame
import time

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Joystick Tester")

pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No joystick found!")
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Testing: {joystick.get_name()}")
    print("Keep the Pygame window focused and press buttons!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                if abs(event.value) > 0.2:
                    print(f"Axis {event.axis}: {event.value:.2f}")
            elif event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")
            elif event.type == pygame.JOYHATMOTION:
                print(f"Hat {event.hat}: {event.value}")
        time.sleep(0.01)
