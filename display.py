import pygame
import pygame.locals
import pygame_gui
from constants import *

class Display(object):
    def __init__(self):
        self.surface = pygame.display.set_mode(RESOLUTION, 0, 32)
        pygame.display.set_caption('IMAGE RESTORATION')
        self.background = pygame.Surface(RESOLUTION)

        self.manager = pygame_gui.UIManager(RESOLUTION)

        self.loadButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_LOADBUTTON, SIZE_LOADBUTTON),
            text='SELECT IMAGE',
            manager=self.manager)

        self.fixButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_FIXBUTTON, SIZE_FIXBUTTON),
            text='REPAIR',
            manager=self.manager)

        self.improveButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_IMPBUTTON, SIZE_IMPBUTTON),
            text='IMPROVE',
            manager=self.manager)

        self.saveButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_SAVEBUTTON, SIZE_SAVEBUTTON),
            text='SAVE IMAGE',
            manager=self.manager)


        self.infoButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_INFOBUTTON, SIZE_INFOBUTTON),
            text='INFO',
            manager=self.manager)

        self.neutral_picture = None
        self.modified_picture = None

    def draw(self):

        if self.neutral_picture:
            img = pygame.image.load(self.neutral_picture)
            img = pygame.transform.scale(img, SIZE_PICTURES)
            self.surface.blit(img, POSITION_NEUTRALPICTURE)

        if self.modified_picture:
            img = pygame.image.load(self.modified_picture)
            img = pygame.transform.scale(img, SIZE_PICTURES)
            self.surface.blit(img, POSITION_MODIFIEDPICTURE)

        pygame.font.init()

        myfont = pygame.font.SysFont('Arial', 24)
        textsurface = myfont.render('Old photo restoration project', False,
                                    FONT_COLOR)

        self.surface.blit(textsurface, POSITION_TASK)

        myfont_info = pygame.font.SysFont('Arial', 12)
        textsurface_info = myfont_info.render(TEXT_INFO, False,
                                              FONT_COLOR)
        self.surface.blit(textsurface_info, POSITION_INFO)

        pygame.display.update()