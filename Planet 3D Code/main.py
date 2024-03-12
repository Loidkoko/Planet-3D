import pygame
import os
import random

width = 1200 #x
hidth = 1200 #y

fps = 20

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 127, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
l_blue = (50, 50, 255)
blue = (0, 0, 255)
purple = (255, 0, 255)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

pygame.display.set_icon(pygame.image.load(os.path.join(img_folder, 'icon0.png')))

class ControlPoint(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sonce1
        self.image.set_colorkey(white)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.cordx = hidth / 2
        self.cordy = width / 2
        self.rect.x = hidth / 2
        self.rect.y = width / 2
        self.rect.center = (width / 2, hidth / 2)
        self.m = 150
silagravia = 10
class Planet(pygame.sprite.Sprite):
    def __init__(self, wwodx, wwody, wwodz, wwodspedx, wwodspedy, wwodspedz, m):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(skyobjimg)
        self.imagen = self.image
        self.m = m
        self.speedx = wwodspedx
        self.speedy = wwodspedy
        self.speedz = wwodspedz
        self.cordz = wwodz
        self.cordx = wwodx
        self.rect = self.image.get_rect()
        self.cordy = wwody
        self.rect.x = wwodx
        self.image.set_colorkey(white)
        self.image = pygame.transform.scale(self.image, (wwodz/10 + self.m, wwodz/10 + self.m))
        self.rect.center = (wwodx, wwody)

    def update(self):
        global silagravia

        for i in skyobj:
            if i != self:
                if (self.cordx - i.obncordx) != 0:
                    self.speedx = self.speedx-((i.m / self.m)*((self.cordx - i.obncordx)/10))
                if (self.cordy - i.obncordy) != 0:
                    self.speedy = self.speedy-((i.m / self.m)*((self.cordy - i.obncordy)/10))
                if (self.cordz - i.obncordz) != 0:
                    self.speedz = self.speedz-((i.m / self.m)*((self.cordz - i.obncordz)/10))

        self.cordx = self.cordx + self.speedx
        self.cordy = self.cordy + self.speedy
        self.cordz = self.cordz + self.speedz
        self.image = pygame.transform.scale(self.imagen, (self.cordz / 10 + self.m, self.cordz / 10 + self.m))
        self.rect.center = (self.cordx, self.cordy)
        self.rect.x = self.cordx
        self.rect.y = self.cordy



class okna_nastoi(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        global okon_planet
        self.okons = okon_planet
        self.MaSs = okna_mass()
        okna_dop.add(self.MaSs)
        self.Xx = okna_x()
        okna_dop.add(self.Xx)
        self.Yy = okna_y()
        okna_dop.add(self.Yy)
        self.Zz = okna_z()
        okna_dop.add(self.Zz)
        self.sXx = okna_sx()
        okna_dop.add(self.sXx)
        self.sYy = okna_sy()
        okna_dop.add(self.sYy)
        self.sZz = okna_sz()
        okna_dop.add(self.sZz)
        okon_planet = okon_planet + 1
        self.image = OKNAA_img
        self.image = pygame.transform.scale(self.image, (600, 300))
        self.rect = self.image.get_rect()
        self.rect.y = 100 + scroll + (self.okons * 330)
        self.rect.x = 600
        self.rect.center = (600, 100 + scroll + (self.okons * 330))
        self.name = "oknA_nastroi"
    def update(self):
        global scroll
        self.rect.y = 100 + scroll + (self.okons * 330)
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            clock.tick(fps)


class plus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Plus
        self.rect = self.image.get_rect()
        self.rect.center = (1100, 100)
        self.name = "pluS"
    def update(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            clock.tick(fps)
            okNo = okna_nastoi()
            opat_okna.add(okNo)

class conti(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cont
        self.rect = self.image.get_rect()
        self.rect.y = 1100
        self.rect.x = 1100
        self.rect.center = (1100, 1100)
        self.name = "conTi"
    def update(self):
        global continu
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            clock.tick(fps)
            continu = False

class Fps(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Massss
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (1095, 300)
        self.natpis = "20"
        self.printon = False
        self.name = "fpS"

    def update(self):
        if pygame.mouse.get_pressed()[0]:
            self.printon = False
            clock.tick(fps)
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.printon = True
            clock.tick(fps)
        if self.printon == True:
            if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                if self.natpis != "":
                    self.natpis = self.natpis[:-1]
            if pygame.key.get_pressed()[pygame.K_0] or pygame.key.get_pressed()[pygame.K_KP_0]:
                if self.natpis != "":
                    self.natpis = self.natpis + "0"
            if pygame.key.get_pressed()[pygame.K_1] or pygame.key.get_pressed()[pygame.K_KP_1]: self.natpis = self.natpis + "1"
            if pygame.key.get_pressed()[pygame.K_2] or pygame.key.get_pressed()[pygame.K_KP_2]: self.natpis = self.natpis + "2"
            if pygame.key.get_pressed()[pygame.K_3] or pygame.key.get_pressed()[pygame.K_KP_3]: self.natpis = self.natpis + "3"
            if pygame.key.get_pressed()[pygame.K_4] or pygame.key.get_pressed()[pygame.K_KP_4]: self.natpis = self.natpis + "4"
            if pygame.key.get_pressed()[pygame.K_5] or pygame.key.get_pressed()[pygame.K_KP_5]: self.natpis = self.natpis + "5"
            if pygame.key.get_pressed()[pygame.K_6] or pygame.key.get_pressed()[pygame.K_KP_6]: self.natpis = self.natpis + "6"
            if pygame.key.get_pressed()[pygame.K_7] or pygame.key.get_pressed()[pygame.K_KP_7]: self.natpis = self.natpis + "7"
            if pygame.key.get_pressed()[pygame.K_8] or pygame.key.get_pressed()[pygame.K_KP_8]: self.natpis = self.natpis + "8"
            if pygame.key.get_pressed()[pygame.K_9] or pygame.key.get_pressed()[pygame.K_KP_9]: self.natpis = self.natpis + "9"
            clock.tick(fps)
        screen.blit(font.render((self.natpis), True, black), (self.rect.x + 10, self.rect.y + 10))

class Fps_name(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = fps_Name
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (1095, 250)
        self.name = "fps_nam"

class okna_mass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        global okon_planet
        self.okons = okon_planet
        self.image = Massss
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.y = 250 + scroll + (self.okons * 330)
        self.rect.x = 600
        self.rect.center = (600, 100 + scroll + (self.okons * 330))
        self.name = "oknA_mass"
        self.natpis = "100"
        self.printon = False
    def update(self):
        global scroll
        self.rect.x = 700
        self.rect.y = 250 + scroll + (self.okons * 330)
        if pygame.mouse.get_pressed()[0]:
            self.printon = False
            clock.tick(fps)
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.printon = True
            clock.tick(fps)
        if self.printon == True:
            if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                if self.natpis != "":
                    self.natpis = self.natpis[:-1]
            if pygame.key.get_pressed()[pygame.K_0] or pygame.key.get_pressed()[pygame.K_KP_0]: self.natpis = self.natpis + "0"
            if pygame.key.get_pressed()[pygame.K_1] or pygame.key.get_pressed()[pygame.K_KP_1]: self.natpis = self.natpis + "1"
            if pygame.key.get_pressed()[pygame.K_2] or pygame.key.get_pressed()[pygame.K_KP_2]: self.natpis = self.natpis + "2"
            if pygame.key.get_pressed()[pygame.K_3] or pygame.key.get_pressed()[pygame.K_KP_3]: self.natpis = self.natpis + "3"
            if pygame.key.get_pressed()[pygame.K_4] or pygame.key.get_pressed()[pygame.K_KP_4]: self.natpis = self.natpis + "4"
            if pygame.key.get_pressed()[pygame.K_5] or pygame.key.get_pressed()[pygame.K_KP_5]: self.natpis = self.natpis + "5"
            if pygame.key.get_pressed()[pygame.K_6] or pygame.key.get_pressed()[pygame.K_KP_6]: self.natpis = self.natpis + "6"
            if pygame.key.get_pressed()[pygame.K_7] or pygame.key.get_pressed()[pygame.K_KP_7]: self.natpis = self.natpis + "7"
            if pygame.key.get_pressed()[pygame.K_8] or pygame.key.get_pressed()[pygame.K_KP_8]: self.natpis = self.natpis + "8"
            if pygame.key.get_pressed()[pygame.K_9] or pygame.key.get_pressed()[pygame.K_KP_9]: self.natpis = self.natpis + "9"
            clock.tick(fps)
        screen.blit(font.render((self.natpis), True, black), (self.rect.x + 10, self.rect.y + 10))



class okna_x(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        global okon_planet
        self.okons = okon_planet
        self.image = Massss
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.y = 220 + scroll + (self.okons * 330)
        self.rect.x = 450
        self.rect.center = (450, 220 + scroll + (self.okons * 330))
        self.name = "oknA_x"
        self.natpis = "0"
        self.printon = False
    def update(self):
        global scroll
        self.rect.x = 450
        self.rect.y = 220 + scroll + (self.okons * 330)
        if pygame.mouse.get_pressed()[0]:
            self.printon = False
            clock.tick(fps)
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.printon = True
            clock.tick(fps)
        if self.printon == True:
            if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                if self.natpis != "":
                    self.natpis = self.natpis[:-1]
            if pygame.key.get_pressed()[pygame.K_0] or pygame.key.get_pressed()[pygame.K_KP_0]: self.natpis = self.natpis + "0"
            if pygame.key.get_pressed()[pygame.K_1] or pygame.key.get_pressed()[pygame.K_KP_1]: self.natpis = self.natpis + "1"
            if pygame.key.get_pressed()[pygame.K_2] or pygame.key.get_pressed()[pygame.K_KP_2]: self.natpis = self.natpis + "2"
            if pygame.key.get_pressed()[pygame.K_3] or pygame.key.get_pressed()[pygame.K_KP_3]: self.natpis = self.natpis + "3"
            if pygame.key.get_pressed()[pygame.K_4] or pygame.key.get_pressed()[pygame.K_KP_4]: self.natpis = self.natpis + "4"
            if pygame.key.get_pressed()[pygame.K_5] or pygame.key.get_pressed()[pygame.K_KP_5]: self.natpis = self.natpis + "5"
            if pygame.key.get_pressed()[pygame.K_6] or pygame.key.get_pressed()[pygame.K_KP_6]: self.natpis = self.natpis + "6"
            if pygame.key.get_pressed()[pygame.K_7] or pygame.key.get_pressed()[pygame.K_KP_7]: self.natpis = self.natpis + "7"
            if pygame.key.get_pressed()[pygame.K_8] or pygame.key.get_pressed()[pygame.K_KP_8]: self.natpis = self.natpis + "8"
            if pygame.key.get_pressed()[pygame.K_9] or pygame.key.get_pressed()[pygame.K_KP_9]: self.natpis = self.natpis + "9"
            clock.tick(fps)
        screen.blit(font.render((self.natpis), True, black), (self.rect.x + 10, self.rect.y + 10))

class okna_y(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        global okon_planet
        self.okons = okon_planet
        self.image = Massss
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.y = 280 + scroll + (self.okons * 330)
        self.rect.x = 450
        self.rect.center = (450, 280 + scroll + (self.okons * 330))
        self.name = "oknA_y"
        self.natpis = "0"
        self.printon = False
    def update(self):
        global scroll
        self.rect.x = 450
        self.rect.y = 280 + scroll + (self.okons * 330)
        if pygame.mouse.get_pressed()[0]:
            self.printon = False
            clock.tick(fps)
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.printon = True
            clock.tick(fps)
        if self.printon == True:
            if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                if self.natpis != "":
                    self.natpis = self.natpis[:-1]
            if pygame.key.get_pressed()[pygame.K_0] or pygame.key.get_pressed()[pygame.K_KP_0]: self.natpis = self.natpis + "0"
            if pygame.key.get_pressed()[pygame.K_1] or pygame.key.get_pressed()[pygame.K_KP_1]: self.natpis = self.natpis + "1"
            if pygame.key.get_pressed()[pygame.K_2] or pygame.key.get_pressed()[pygame.K_KP_2]: self.natpis = self.natpis + "2"
            if pygame.key.get_pressed()[pygame.K_3] or pygame.key.get_pressed()[pygame.K_KP_3]: self.natpis = self.natpis + "3"
            if pygame.key.get_pressed()[pygame.K_4] or pygame.key.get_pressed()[pygame.K_KP_4]: self.natpis = self.natpis + "4"
            if pygame.key.get_pressed()[pygame.K_5] or pygame.key.get_pressed()[pygame.K_KP_5]: self.natpis = self.natpis + "5"
            if pygame.key.get_pressed()[pygame.K_6] or pygame.key.get_pressed()[pygame.K_KP_6]: self.natpis = self.natpis + "6"
            if pygame.key.get_pressed()[pygame.K_7] or pygame.key.get_pressed()[pygame.K_KP_7]: self.natpis = self.natpis + "7"
            if pygame.key.get_pressed()[pygame.K_8] or pygame.key.get_pressed()[pygame.K_KP_8]: self.natpis = self.natpis + "8"
            if pygame.key.get_pressed()[pygame.K_9] or pygame.key.get_pressed()[pygame.K_KP_9]: self.natpis = self.natpis + "9"
            clock.tick(fps)
        screen.blit(font.render((self.natpis), True, black), (self.rect.x + 10, self.rect.y + 10))

class okna_z(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        global okon_planet
        self.okons = okon_planet
        self.image = Massss
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.y = 340 + scroll + (self.okons * 330)
        self.rect.x = 450
        self.rect.center = (450, 340 + scroll + (self.okons * 330))
        self.name = "oknA_z"
        self.natpis = "0"
        self.printon = False
    def update(self):
        global scroll
        self.rect.x = 450
        self.rect.y = 340 + scroll + (self.okons * 330)
        if pygame.mouse.get_pressed()[0]:
            self.printon = False
            clock.tick(fps)
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.printon = True
            clock.tick(fps)
        if self.printon == True:
            if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                if self.natpis != "":
                    self.natpis = self.natpis[:-1]
            if pygame.key.get_pressed()[pygame.K_0] or pygame.key.get_pressed()[pygame.K_KP_0]: self.natpis = self.natpis + "0"
            if pygame.key.get_pressed()[pygame.K_1] or pygame.key.get_pressed()[pygame.K_KP_1]: self.natpis = self.natpis + "1"
            if pygame.key.get_pressed()[pygame.K_2] or pygame.key.get_pressed()[pygame.K_KP_2]: self.natpis = self.natpis + "2"
            if pygame.key.get_pressed()[pygame.K_3] or pygame.key.get_pressed()[pygame.K_KP_3]: self.natpis = self.natpis + "3"
            if pygame.key.get_pressed()[pygame.K_4] or pygame.key.get_pressed()[pygame.K_KP_4]: self.natpis = self.natpis + "4"
            if pygame.key.get_pressed()[pygame.K_5] or pygame.key.get_pressed()[pygame.K_KP_5]: self.natpis = self.natpis + "5"
            if pygame.key.get_pressed()[pygame.K_6] or pygame.key.get_pressed()[pygame.K_KP_6]: self.natpis = self.natpis + "6"
            if pygame.key.get_pressed()[pygame.K_7] or pygame.key.get_pressed()[pygame.K_KP_7]: self.natpis = self.natpis + "7"
            if pygame.key.get_pressed()[pygame.K_8] or pygame.key.get_pressed()[pygame.K_KP_8]: self.natpis = self.natpis + "8"
            if pygame.key.get_pressed()[pygame.K_9] or pygame.key.get_pressed()[pygame.K_KP_9]: self.natpis = self.natpis + "9"
            clock.tick(fps)
        screen.blit(font.render((self.natpis), True, black), (self.rect.x + 10, self.rect.y + 10))


class okna_sx(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        global okon_planet, width, hidth
        self.okons = okon_planet
        self.image = Massss
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.y = 220 + scroll + (self.okons * 330)
        self.rect.x = 580
        self.rect.center = (580, 220 + scroll + (self.okons * 330))
        self.name = "oknA_sx"
        self.natpis = "0"
        self.printon = False
        self.min = False
    def update(self):
        global scroll
        self.rect.x = 580
        self.rect.y = 220 + scroll + (self.okons * 330)
        if pygame.mouse.get_pressed()[0]:
            self.printon = False
            clock.tick(fps)
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.printon = True
            clock.tick(fps)
        if self.printon == True:
            if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                if self.natpis != "":
                    self.natpis = self.natpis[:-1]
            if pygame.key.get_pressed()[pygame.K_0] or pygame.key.get_pressed()[pygame.K_KP_0]: self.natpis = self.natpis + "0"
            if pygame.key.get_pressed()[pygame.K_1] or pygame.key.get_pressed()[pygame.K_KP_1]: self.natpis = self.natpis + "1"
            if pygame.key.get_pressed()[pygame.K_2] or pygame.key.get_pressed()[pygame.K_KP_2]: self.natpis = self.natpis + "2"
            if pygame.key.get_pressed()[pygame.K_3] or pygame.key.get_pressed()[pygame.K_KP_3]: self.natpis = self.natpis + "3"
            if pygame.key.get_pressed()[pygame.K_4] or pygame.key.get_pressed()[pygame.K_KP_4]: self.natpis = self.natpis + "4"
            if pygame.key.get_pressed()[pygame.K_5] or pygame.key.get_pressed()[pygame.K_KP_5]: self.natpis = self.natpis + "5"
            if pygame.key.get_pressed()[pygame.K_6] or pygame.key.get_pressed()[pygame.K_KP_6]: self.natpis = self.natpis + "6"
            if pygame.key.get_pressed()[pygame.K_7] or pygame.key.get_pressed()[pygame.K_KP_7]: self.natpis = self.natpis + "7"
            if pygame.key.get_pressed()[pygame.K_8] or pygame.key.get_pressed()[pygame.K_KP_8]: self.natpis = self.natpis + "8"
            if pygame.key.get_pressed()[pygame.K_9] or pygame.key.get_pressed()[pygame.K_KP_9]: self.natpis = self.natpis + "9"
            if pygame.key.get_pressed()[pygame.K_KP_MINUS] or pygame.key.get_pressed()[pygame.K_MINUS]:
                if self.min == False:
                    self.min = True
                    self.natpis = "-" + self.natpis
                else:
                    self.min = False
                    self.natpis = self.natpis[-1:]
            clock.tick(fps)
        screen.blit(font.render((self.natpis), True, black), (self.rect.x + 10, self.rect.y + 10))


class okna_sy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        global okon_planet
        self.okons = okon_planet
        self.image = Massss
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.y = 280 + scroll + (self.okons * 330)
        self.rect.x = 580
        self.rect.center = (580, 280 + scroll + (self.okons * 330))
        self.name = "oknA_sy"
        self.natpis = "0"
        self.printon = False
        self.min = False
    def update(self):
        global scroll
        self.rect.x = 580
        self.rect.y = 280 + scroll + (self.okons * 330)
        if pygame.mouse.get_pressed()[0]:
            self.printon = False
            clock.tick(fps)
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.printon = True
            clock.tick(fps)
        if self.printon == True:
            if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                if self.natpis != "":
                    self.natpis = self.natpis[:-1]
            if pygame.key.get_pressed()[pygame.K_0] or pygame.key.get_pressed()[pygame.K_KP_0]: self.natpis = self.natpis + "0"
            if pygame.key.get_pressed()[pygame.K_1] or pygame.key.get_pressed()[pygame.K_KP_1]: self.natpis = self.natpis + "1"
            if pygame.key.get_pressed()[pygame.K_2] or pygame.key.get_pressed()[pygame.K_KP_2]: self.natpis = self.natpis + "2"
            if pygame.key.get_pressed()[pygame.K_3] or pygame.key.get_pressed()[pygame.K_KP_3]: self.natpis = self.natpis + "3"
            if pygame.key.get_pressed()[pygame.K_4] or pygame.key.get_pressed()[pygame.K_KP_4]: self.natpis = self.natpis + "4"
            if pygame.key.get_pressed()[pygame.K_5] or pygame.key.get_pressed()[pygame.K_KP_5]: self.natpis = self.natpis + "5"
            if pygame.key.get_pressed()[pygame.K_6] or pygame.key.get_pressed()[pygame.K_KP_6]: self.natpis = self.natpis + "6"
            if pygame.key.get_pressed()[pygame.K_7] or pygame.key.get_pressed()[pygame.K_KP_7]: self.natpis = self.natpis + "7"
            if pygame.key.get_pressed()[pygame.K_8] or pygame.key.get_pressed()[pygame.K_KP_8]: self.natpis = self.natpis + "8"
            if pygame.key.get_pressed()[pygame.K_9] or pygame.key.get_pressed()[pygame.K_KP_9]: self.natpis = self.natpis + "9"
            if pygame.key.get_pressed()[pygame.K_KP_MINUS] or pygame.key.get_pressed()[pygame.K_MINUS]:
                if self.min == False:
                    self.min = True
                    self.natpis = "-" + self.natpis
                else:
                    self.min = False
                    self.natpis = self.natpis[-1:]
            clock.tick(fps)
        screen.blit(font.render((self.natpis), True, black), (self.rect.x + 10, self.rect.y + 10))


class okna_sz(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        global okon_planet
        self.okons = okon_planet
        self.image = Massss
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.y = 340 + scroll + (self.okons * 330)
        self.rect.x = 580
        self.rect.center = (580, 340 + scroll + (self.okons * 330))
        self.name = "oknA_sz"
        self.natpis = "0"
        self.printon = False
        self.min = False
    def update(self):
        global scroll
        self.rect.x = 580
        self.rect.y = 340 + scroll + (self.okons * 330)
        if pygame.mouse.get_pressed()[0]:
            self.printon = False
            clock.tick(fps)
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.printon = True
            clock.tick(fps)
        if self.printon == True:
            if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                if self.natpis != "":
                    self.natpis = self.natpis[:-1]
            if pygame.key.get_pressed()[pygame.K_0] or pygame.key.get_pressed()[pygame.K_KP_0]: self.natpis = self.natpis + "0"
            if pygame.key.get_pressed()[pygame.K_1] or pygame.key.get_pressed()[pygame.K_KP_1]: self.natpis = self.natpis + "1"
            if pygame.key.get_pressed()[pygame.K_2] or pygame.key.get_pressed()[pygame.K_KP_2]: self.natpis = self.natpis + "2"
            if pygame.key.get_pressed()[pygame.K_3] or pygame.key.get_pressed()[pygame.K_KP_3]: self.natpis = self.natpis + "3"
            if pygame.key.get_pressed()[pygame.K_4] or pygame.key.get_pressed()[pygame.K_KP_4]: self.natpis = self.natpis + "4"
            if pygame.key.get_pressed()[pygame.K_5] or pygame.key.get_pressed()[pygame.K_KP_5]: self.natpis = self.natpis + "5"
            if pygame.key.get_pressed()[pygame.K_6] or pygame.key.get_pressed()[pygame.K_KP_6]: self.natpis = self.natpis + "6"
            if pygame.key.get_pressed()[pygame.K_7] or pygame.key.get_pressed()[pygame.K_KP_7]: self.natpis = self.natpis + "7"
            if pygame.key.get_pressed()[pygame.K_8] or pygame.key.get_pressed()[pygame.K_KP_8]: self.natpis = self.natpis + "8"
            if pygame.key.get_pressed()[pygame.K_9] or pygame.key.get_pressed()[pygame.K_KP_9]: self.natpis = self.natpis + "9"
            if pygame.key.get_pressed()[pygame.K_KP_MINUS] or pygame.key.get_pressed()[pygame.K_MINUS]:
                if self.min == False:
                    self.min = True
                    self.natpis = "-" + self.natpis
                else:
                    self.min = False
                    self.natpis = self.natpis[-1:]
            clock.tick(fps)
        screen.blit(font.render((self.natpis), True, black), (self.rect.x + 10, self.rect.y + 10))




pygame.init()
screen = pygame.display.set_mode((width, hidth))
pygame.display.set_caption("Planet")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 26)

cont = pygame.image.load(os.path.join(img_folder, 'cont.png')).convert()
OKNAA_img = pygame.image.load(os.path.join(img_folder, 'non.png')).convert()
Plus = pygame.image.load(os.path.join(img_folder, 'plus.png')).convert()
Massss = pygame.image.load(os.path.join(img_folder, 'mass.png')).convert()
fps_Name = pygame.image.load(os.path.join(img_folder, 'fps_name.png')).convert()

okon_planet = 0
scroll = 0

opat_okna = pygame.sprite.Group()
okna_dop = pygame.sprite.Group()

okNo = okna_nastoi()
opat_okna.add(okNo)

FpS = Fps()
opat_okna.add(FpS)

Fps_Name = Fps_name()
opat_okna.add(Fps_Name)

PLus = plus()
opat_okna.add(PLus)

contin = conti()
opat_okna.add(contin)

running = True
continu = True
while continu:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continu = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                scroll = scroll - 10
            elif event.button == 5:
                scroll = scroll + 10
            if scroll > 0:
                scroll = 0
    screen.fill(white)
    opat_okna.draw(screen)
    okna_dop.draw(screen)
    opat_okna.update()
    okna_dop.update()
    pygame.display.flip()

for i in opat_okna:
    if i.name == "fpS":
        fps = int(i.natpis)




skyobj = pygame.sprite.Group()

black1 = pygame.image.load(os.path.join(img_folder, 'bleck.png')).convert()
sonce1 = pygame.image.load(os.path.join(img_folder, 'Sonce.png')).convert()
planet1 = pygame.image.load(os.path.join(img_folder, 'planet1.png')).convert()
planet2 = pygame.image.load(os.path.join(img_folder, 'planet2.png')).convert()
planet3 = pygame.image.load(os.path.join(img_folder, 'planet3.png')).convert()
planet4 = pygame.image.load(os.path.join(img_folder, 'planet4.png')).convert()
planet5 = pygame.image.load(os.path.join(img_folder, 'planet5.png')).convert()
planet6 = pygame.image.load(os.path.join(img_folder, 'planet6.png')).convert()
skyobjimg = (planet1, planet2, planet3, planet4, planet5, planet6)


for i in opat_okna:
    if i.name == "oknA_nastroi":
        if int(i.MaSs.natpis) != 0:
            # wwodx, wwody, wwodz, wwodspedx, wwodspedy, wwodspedz, m
            planet11 = Planet(int(i.Xx.natpis), int(i.Yy.natpis), int(i.Zz.natpis), int(i.sXx.natpis), int(i.sYy.natpis), int(i.sZz.natpis), int(i.MaSs.natpis))
            skyobj.add(planet11)





while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in skyobj:
        i.obncordx = i.cordx
        i.obncordy = i.cordy
        i.obncordz = i.cordz
    skyobj.update()
    for b in range(len(skyobj)):
        for k in range((len(skyobj)) - 1):
            for i in skyobj:
                for t in skyobj:
                    if i != t:
                        if i.cordz > t.cordz:
                            g = i
                            skyobj.remove(i)
                            skyobj.add(i)
    screen.fill(black)
    skyobj.draw(screen)
    pygame.display.flip()