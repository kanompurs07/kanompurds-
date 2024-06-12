# juego de pong 
import pygame
import random 


SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 10

PADDEL_SPEED = 6
BALL_SPEED = 5

def main():

   pygame.init()

   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

   pygame.display.set_caption("pong")

   paddle_1_post = [50, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2]
   paddle_2_post = [SCREEN_WIDTH - 50 - PADDLE_WIDTH, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2]
   ball_post = [(SCREEN_WIDTH - BALL_SIZE) // 2, (SCREEN_HEIGHT - BALL_SIZE) // 2]
   ball_speed = [random.choice([-BALL_SPEED, BALL_SPEED]), random.choice([-BALL_SPEED, BALL_SPEED])]


   socer_1 = 0
   socer_2 = 0 

   front = pygame.font.Font(None,36)

   clock = pygame.time.Clock()


   running = True
   while running:
      screen.fill(COLOR_BLACK)

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False

      key = pygame.key.get_pressed()

      if key [pygame.K_w] and paddle_1_post[1] > 0:
         paddle_1_post[1] -= PADDEL_SPEED
      if key [pygame.K_s] and paddle_1_post[1] < SCREEN_HEIGHT - PADDLE_HEIGHT:
         paddle_1_post[1] += PADDEL_SPEED

      
      if key [pygame.K_UP]  and paddle_2_post[1] > 0:
         paddle_2_post[1] -= PADDEL_SPEED
      if key [pygame.K_DOWN] and paddle_1_post[1] < SCREEN_HEIGHT - PADDLE_HEIGHT:
         paddle_2_post[1] += PADDEL_SPEED


      ball_post[0] += ball_speed[0]
      ball_post[1] += ball_speed[1]

      if ball_post[1] <= 0 or ball_post[1] >= SCREEN_HEIGHT - BALL_SIZE:
         ball_speed[1] = -ball_speed[1]

      if (ball_post[0] <= paddle_1_post[0] + PADDLE_WIDTH and
         paddle_1_post[1] < ball_post[1] < paddle_1_post[1] + PADDLE_HEIGHT ):
         ball_speed[0] = -ball_speed[0]
      
      if (ball_post[0] >= paddle_2_post[0] - BALL_SIZE and 
         paddle_2_post[1] < ball_post[1] < paddle_2_post[1] + PADDLE_HEIGHT):
         ball_speed[0] = -ball_speed[0]
      
      if ball_post[0] <= 0:
         socer_2 += 1
         ball_post = [(SCREEN_WIDTH - BALL_SIZE) //2, (SCREEN_HEIGHT - BALL_SIZE) //2 ]
         ball_speed = [random.choice([-BALL_SPEED, BALL_SPEED]), random.choice([-BALL_SPEED, BALL_SPEED])]

      if ball_post[0] >= SCREEN_WIDTH - BALL_SIZE:
         socer_1 += 1
         ball_post = [(SCREEN_WIDTH - BALL_SIZE)//2, (SCREEN_HEIGHT - BALL_SIZE)//2]
         ball_speed =  [random.choice([BALL_SPEED, BALL_SPEED]), random.choice([BALL_SPEED, BALL_SPEED])]

      pygame.draw.rect(screen, COLOR_WHITE, (*paddle_1_post, PADDLE_WIDTH, PADDLE_HEIGHT))
      pygame.draw.rect(screen, COLOR_WHITE, (*paddle_2_post, PADDLE_WIDTH, PADDLE_HEIGHT))
      pygame.draw.rect(screen, COLOR_WHITE, (*ball_post, BALL_SIZE, BALL_SIZE))

      socer_text = front.render(f"{socer_1} - {socer_2}",True, COLOR_WHITE)
      screen.blit(socer_text, ((SCREEN_WIDTH - socer_text.get_width()) // 2, 20))


      pygame.display.flip()

      clock.tick(60)
   pygame.quit()

if __name__ == "__main__":
   main()
        



