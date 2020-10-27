import pygame

pygame.init() # 초기화 (반드시 필요함)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/S/Desktop/PythonWorkspace/pygame_basic/background.png")

# 이벤트 루프
running = True # 게임이 진행중인지 확인하는 변수
while running:
    for event in pygame.event.get():  # pygame 사용시 무조건 사용
        if event.type == pygame.QUIT:  # 창을 닫는 이벤트 체크
            running = False # 이벤트 루프 종료
    
    #screen.fill((255, 255, 0))
    screen.blit(background, (0, 0))  # 배경 그리기

    pygame.display.update()  # 게임화면 다시 그리기



# 루프 종료
pygame.quit()