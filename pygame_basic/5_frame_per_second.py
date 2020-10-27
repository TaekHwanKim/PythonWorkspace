import pygame

pygame.init() # 초기화 (반드시 필요함)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/S/Desktop/PythonWorkspace/pygame_basic/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:/Users/S/Desktop/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size # 캐릭터의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_height / 2) # 화면 가로의 절반 (가운데) 에 위치하게
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 위치하게

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 이벤트 루프
running = True # 게임이 진행중인지 확인하는 변수
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정

# 프레임   

    for event in pygame.event.get():  # pygame 사용시 무조건 사용
        if event.type == pygame.QUIT:  # 창을 닫는 이벤트 체크
            running = False # 이벤트 루프 종료
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
        

    character_x_pos += to_x * dt # dt값으로 이동보정
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width -character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height -character_height

    screen.blit(background, (0, 0))  # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update()  # 게임화면 다시 그리기



# 루프 종료
pygame.quit()