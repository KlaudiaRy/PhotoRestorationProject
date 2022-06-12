import pygame
import pygame.locals
import pygame_gui
from display import Display
import os
import files_functions
import image_functions
import image_prediction

class PhotoRestoration(object):

    def __init__(self):
        pygame.init()
        self.display = Display()
        self.fps_clock = pygame.time.Clock()
        self.display.saveButton.disable()
        self.display.improveButton.disable()
        self.display.fixButton.disable()


    def handle_events(self):

        time_delta = self.fps_clock.tick(1000)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

                    if event.ui_element == self. display.loadButton:
                        self.__init__()
                        self.display.neutral_picture=files_functions.pick_photo()
                        self.display.modified_picture = None
                        self.display.draw()
                        f = open("tmp/neutral_path.txt", "w")
                        f.write(self.display.neutral_picture)
                        f.close()
                        self.display.fixButton.enable()
                        self.display.saveButton.enable()


                    if event.ui_element == self. display.saveButton:
                        files_functions.save_photo()

                    if event.ui_element == self. display.infoButton:
                        files_functions.display_info()

                    if event.ui_element == self. display.improveButton:
                        self.__init__()
                        f = open('tmp/neutral_path.txt', "r")
                        if (os.stat('tmp/neutral_path.txt').st_size != 0):
                            name = f.read()
                            self.display.modified_picture = image_functions.improve_picture()
                            f2 = open('tmp/modified_path.txt', "w")
                            f2.write(self.display.modified_picture)
                            self.display.neutral_picture = name
                            f2.close()
                        self.display.draw()
                        f.close()
                        self.display.saveButton.enable()

                    if event.ui_element == self. display.fixButton:
                        self.__init__()
                        f = open('tmp/neutral_path.txt', "r")
                        if (os.stat('tmp/neutral_path.txt').st_size != 0):
                            name = f.read()
                            self.display.modified_picture = image_prediction.generate_images()
                            f2 = open('tmp/modified_path.txt', "w")
                            f2.write(self.display.modified_picture)
                            self.display.neutral_picture = name
                            f2.close()
                        self.display.draw()
                        f.close()
                        self.display.improveButton.enable()
                        self.display.saveButton.enable()




            self. display.manager.process_events(event)

        self. display.manager.update(time_delta)
        self. display.manager.draw_ui(self. display.surface)
        pygame.display.update()

        return False

    def run(self):
        self.display.draw()
        while not self.handle_events():
            pass

if __name__ == '__main__':
    app = PhotoRestoration()
    app.run()