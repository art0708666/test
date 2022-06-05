
import pygame
import random

pygame.init()
clock = pygame.time.Clock()

W = 600
H = 600

screen = pygame.display.set_mode([W , H])
screen_rect = screen.get_rect()

star = pygame.image.load("image/star.png")
unicorn = pygame.image.load("image/unicorn.png")
bg_image = pygame.image.load("image/bacground/mountain.png")
bg_scale = pygame.transform.scale(bg_image, (W, H))


font = pygame.font.Font(None  , 80)
font2 = pygame.font.Font(None , 80)
text = font.render("Меню", True, [255, 0, 0])
text2 = font2.render("Настройки",True ,[255, 0, 0])
rect_text = text.get_rect()
rect_text2 = text2.get_rect()
rect_text.centerx = W/2
rect_text.centery = H/2
rect_text2.centerx = -300
rect_text2.centery = -200

star_rect = star.get_rect()
unicorn_rect = unicorn.get_rect()
bg_rect = bg_image.get_rect()

pygame.display.set_caption("Супер игра")
unicorn_rect.center = screen_rect.center
unicorn_rect.bottom = screen_rect.bottom
star_rect.x = 80
star_rect.y = 40
bg_rect.center = W / 2 , H / 2




GO = True
mv_up = False
mv_down = False
mv_right = False
mv_left = False
mv_left_up = False
mv_right_up = False
mv_left_down = False
mv_right_down = False
probel = False


pygame.display.flip()
while GO:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GO = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                 mv_up = True
            elif event.key == pygame.K_s:
                 mv_down = True
            elif event.key == pygame.K_d:
                 mv_right = True
            elif event.key == pygame.K_a:
                 mv_left = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    left_button = False
            elif event.button == 3
            """elif event.key == pygame.K_q:
                 mv_left_up = True
            elif event.key == pygame.K_e:
                 mv_right_up = True
            elif event.key == pygame.K_z:
                 mv_left_down = True
            elif event.key == pygame.K_c:
                 mv_right_down = True
            elif event.key == pygame.K_SPACE:
                 probel = True"""

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                 mv_up = False
            elif event.key == pygame.K_s:
                 mv_down = False
            elif event.key == pygame.K_d:
                 mv_right = False
            elif event.key == pygame.K_a:
                 mv_left = False
            elif event.key == pygame.K_q:
                 mv_left_up = False
            elif event.key == pygame.K_e:
                 mv_right_up = False
            elif event.key == pygame.K_z:
                 mv_left_down = False
            elif event.key == pygame.K_c:
                 mv_right_down = False
            elif event.key == pygame.K_SPACE:
                 probel = False

    if mv_up and screen_rect.top < unicorn_rect.top:
        unicorn_rect.y -= 1
    if mv_down and screen_rect.bottom > unicorn_rect.bottom:
        unicorn_rect.y += 1
    if mv_right and screen_rect.right > unicorn_rect.right:
        unicorn_rect.x += 1
    if mv_left and screen_rect.left < unicorn_rect.left:
        unicorn_rect.x -= 1
    if mv_left_up and screen_rect.top < unicorn_rect.top:
        unicorn_rect.x -= 1
        unicorn_rect.y -= 1
    elif mv_right_up and screen_rect.top < unicorn_rect.top:
        unicorn_rect.x += 1
        unicorn_rect.y -= 1
    elif mv_left_down and screen_rect.bottom > unicorn_rect.bottom:
        unicorn_rect.x -= 1
        unicorn_rect.y += 1
    elif mv_right_down and screen_rect.bottom > unicorn_rect.bottom:
        unicorn_rect.x += 1
        unicorn_rect.y += 1
    elif probel and screen_rect.top < unicorn_rect.top:
        unicorn_rect.y -= 6
    screen.blit(bg_scale, (0,0))
    screen.blit(text, rect_text)
    screen.blit(text2, rect_text2)
    screen.blit(unicorn,unicorn_rect)
    screen.blit(star, star_rect)
    clock.tick(1000)
    pygame.display.flip()
pygame.quit()