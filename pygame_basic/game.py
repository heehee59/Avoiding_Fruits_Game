# *** 사용 이미지 출처 ***
# 사람 이미지 : 플래티콘 Humans 아이콘 팩 (https://www.flaticon.com/kr/packs/humans)
# 과일 이미지 : png트리 (https://kor.pngtree.com/freepng/mosaic-pixel-wind-various-fruit-elements_4794603.html)
# 배경 이미지 :

import pygame
import random

pygame.init()

# 화면 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("*** 과일 피하기 게임 ***")
background = pygame.image.load("C:/Users/sock4/Desktop/Shooting_Game/pygame_basic/background.jpg")
clock = pygame.time.Clock()

# 캐릭터 설정
character = pygame.image.load("C:/Users/sock4/Desktop/Shooting_Game/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동 좌표 및 속도
to_x = 0
to_y = 0
character_speed = 0.6

# 떨어지는 과일
orange = pygame.image.load("C:/Users/sock4/Desktop/Shooting_Game/pygame_basic/orange.png")
lemon = pygame.image.load("C:/Users/sock4/Desktop/Shooting_Game/pygame_basic/lemon.png")
cherry = pygame.image.load("C:/Users/sock4/Desktop/Shooting_Game/pygame_basic/cherry.png")
water = pygame.image.load("C:/Users/sock4/Desktop/Shooting_Game/pygame_basic/water.png")
peach = pygame.image.load("C:/Users/sock4/Desktop/Shooting_Game/pygame_basic/peach.png")
avo = pygame.image.load("C:/Users/sock4/Desktop/Shooting_Game/pygame_basic/avo.png")
berry = pygame.image.load("C:/Users/sock4/Desktop/Shooting_Game/pygame_basic/berry.png")
grape = pygame.image.load("C:/Users/sock4/Desktop/Shooting_Game/pygame_basic/grape.png")
fruits = [orange, lemon, cherry, water, peach, avo, berry, grape]
rd = random.randint(0, len(fruits))
fall_img_size = fruits[rd].get_rect().size
fall_img_width = fall_img_size[0]
fall_img_height = fall_img_size[1]
fall_img_x_pos = random.randint(0, (screen_width - fall_img_width))
fall_img_y_pos = 0
fall_img_speed = 20

# 몫
heart = pygame.image.load("C:/Users/sock4/Desktop/Shooting_Game/pygame_basic/heart.png")
heart_size = heart.get_rect().size
heart_width = heart_size[0]
heart_height = heart_size[1]
heart_x_pos = [350, 390, 430]
hearts = [heart, heart, heart]

# 게임 오버
over = pygame.image.load("C:/Users/sock4/Desktop/Shooting_Game/pygame_basic/over.png")
over_size = over.get_rect().size
over_width = over_size[0]
over_height = over_size[1]
over_x_pos = (screen_width / 2) - (over_width / 2)
over_y_pos = (screen_height / 2) - (over_height / 2) - 30

# 이벤트 루프
running = True
while running:

    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character = pygame.image.load("C:/Users/sock4/Desktop/Shooting_Game/pygame_basic/character_toleft.png")
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character = pygame.image.load("C:/Users/sock4/Desktop/Shooting_Game/pygame_basic/character_toright.png")
                to_x += character_speed

        if event.type == pygame.KEYUP:
            character = pygame.image.load("C:/Users/sock4/Desktop/Shooting_Game/pygame_basic/character.png")
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt

    # 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 떨어지는 똥 랜덤 위치 설정
    fall_img_y_pos += fall_img_speed

    if fall_img_y_pos > screen_height:
        fall_img_y_pos = 0
        fall_img_x_pos = random.randint(0, (screen_width - fall_img_width))

    # 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(fruits[rd], (fall_img_x_pos, fall_img_y_pos))
    for heart_v in range(len(hearts)):
        screen.blit(hearts[heart_v], (heart_x_pos[heart_v], 10))

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    fall_img_rect = fruits[rd].get_rect()
    fall_img_rect.left = fall_img_x_pos
    fall_img_rect.top = fall_img_y_pos

    if character_rect.colliderect(fall_img_rect):
        hearts.pop()

    # 게임 오버 메시지
    if len(hearts) <= 0:
        screen.blit(over, (over_x_pos, over_y_pos))

    pygame.display.update()


pygame.time.delay(3000)

pygame.quit()