import pygame , sys , random
pygame.init()
clock = pygame.time.Clock()
screen_width = 700
screen_height = 406
screen = pygame.display.set_mode([700, 406])
ball = pygame.Rect(335,188,20,20)
player = pygame.Rect(690,133,10,140)
opponent = pygame.Rect(0,133,10,140)
bg_color = (0,0,0)
light_grey = (200,200,200)
red = (255,0,0)
ball_speed_x =7 * random.choice((1,-1))
ball_speed_y =7* random.choice((1,-1))
player_speed = 0
opponent_speed = 7
def ball_restart() :
    global ball_speed_y , ball_speed_x

    ball.center = (screen_width/2 , screen_height/2 )
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1,-1))
 

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_DOWN :
                player_speed += 6

            if event.key == pygame.K_UP :
                player_speed -= 6
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_DOWN :
                player_speed -= 6

            if event.key == pygame.K_UP :
                player_speed += 6



    ball.x += ball_speed_x
    ball.y += ball_speed_y
    player.y += player_speed
    if player.top <= 0 :
        player.top = 0
    if player.bottom >= screen_height :
        player.bottom = screen_height
    if opponent.top <ball.y :
        opponent.y += opponent_speed
    if opponent.bottom > ball.y :
        opponent.y -= opponent_speed
    if opponent.top <= 0 :
        opponent.top = 0
    if opponent.bottom >= screen_height :
        opponent.bottom = screen_height

    if ball.top <= 0 or ball.bottom >= screen_height :
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width :
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1    

    screen.fill(bg_color)        
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,red,ball)   
    pygame.draw.aaline(screen,light_grey,(screen_width/2 , 0) , (screen_width/2 , screen_height))    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()