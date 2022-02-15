#import pygame
import subprocess
from os.path import dirname, abspath
from distutils.dir_util import copy_tree
from os import startfile

father_path = dirname(dirname(abspath(__file__))) # /home/kristina/desire-directory

father_path = f'{father_path}/resources/'
data = [
    ['thanos','Thanos-snap.mp4.mp4']
]
def start(name_of_video):
    for x in data:
        if x[0] == name_of_video:
            print(name_of_video)
            path_for_video = f'{father_path}/{x[1]}'
            startfile(path_for_video)

            """video = cv2.VideoCapture(f'{father_path}/{x[1]}')
            success, video_image = video.read()
            fps = video.get(cv2.CAP_PROP_FPS)
            print('hf')

            window = pygame.display.set_mode(video_image.shape[1::-1])
            clock = pygame.time.Clock()
            DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

            run = success
            while run:
                clock.tick(fps)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                success, video_image = video.read()
                if success:
                    video_surf = pygame.image.frombuffer(
                        video_image.tobytes(), video_image.shape[1::-1], "BGR")
                else:
                    run = False
                window.blit(video_surf, (100, 100))
                pygame.display.flip()

            pygame.quit()
            exit()"""


