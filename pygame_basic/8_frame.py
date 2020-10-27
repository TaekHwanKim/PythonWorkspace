import pygame
######################################################
# 파이게임 프레임
# 기본 초기화 ( 반드시 해야 하는 것들 )
pygame.init() # 초기화 (반드시 필요함)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("게임 이름")

# FPS
clock = pygame.time.Clock()
######################################################

    # 1. 사용자 게임 초기화 ( 배경 화면, 이미지, 좌표, 속도, 폰트 등)
  
    # 2. 이벤트 처리 ( 키보드, 마우스 등 )
 
    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update()  # 매 프레임 별로 게임화면 다시 그리기

# 종료 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기(ms)

# 루프 종료
pygame.quit()