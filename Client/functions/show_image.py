# import pygame module in this program
import pygame
from os.path import dirname, abspath
father_path = dirname(dirname(abspath(__file__))) # D:\MyDrive\CODING\School Server\Client
father_path = f'{father_path}/photos'  #D:\MyDrive\CODING\School Server\Client\resources
print(father_path)

def ShowImage(name):

    pygame.init()
    white = (255, 255, 255)

    # assigning values to X and Y variable
    X = 1920
    Y = 1080

    # create the display surface object
    # of specific dimension..e(X, Y).
    display_surface = pygame.display.set_mode((X, Y))

    # set the pygame window name
    pygame.display.set_caption('Image')

    # create a surface object, image is drawn on it.
    image = f'{father_path}/{name}.jpg'
    image = pygame.image.load(image)
    image = pygame.transform.scale(image, (1920, 1080))

    # infinite loop
    while True:

        # completely fill the surface object
        # with white colour
        display_surface.fill(white)

        # copying the image surface object
        # to the display surface object at
        # (0, 0) coordinate.
        display_surface.blit(image, (0, 0))

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()

                # quit the program.
                quit()

            # Draws the surface object to the screen.
            pygame.display.update()

