import pygame
import sys
import random


pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("got-your-goat-373963.mp3")
pygame.mixer.music.play(-1)

pygame.font.init()
font = pygame.font.SysFont("Times New Roman", 20)
score = 0

width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Goat Game")
clock = pygame.time.Clock()
time_limit = 45
start_ticks = pygame.time.get_ticks()

#Colors (Red, Green, Blue)
sky_blue = (130, 200, 230)
grass_green = (60, 200, 100)
goat_gray = (150, 150, 150)
rock_gray = (80, 80, 80)
leaf_green = (0,180,0)
balloon_blue = (0, 0, 250)
balloon_string = (0, 250, 0)
face_blue = (0, 0, 250)

#StartPosition
goat_x = 25
goat_y = 50
speed = 10

goat_width = 100
goat_height = 50

rock_width = 300
rock_height = 200
rock_x = 500
rock_y = goat_y + 50
rock_speed = 2
leaf_width = 50
leaf_height = 50
leaf_x = 500
leaf_y = goat_y - 50
rock2_width = 150
rock2_height = 100
rock2_x = 250
rock2_y = goat_y + 25
rock2_speed = 1
leaf2_width = 100
leaf2_height = 50
leaf2_x = 400
leaf2_y = 500


rock_touching = False
rock2_touching = False
rock2_rect = pygame.Rect(rock2_x, rock2_y, rock2_width, rock2_height)




def draw_captainchaser(surface, X, Y):
    
    #Body(X,Y, width, height)
    body = pygame.Rect(X,Y,100,40)
    pygame.draw.rect(surface, goat_gray, body)

    #Head(X,Y,width,height)
    head = pygame.Rect(X+75,Y-15,25,25)
    pygame.draw.rect(surface, goat_gray, head)

    #Front legs(X,Y,width,height)
    frontleg1 = pygame.Rect(X+10, Y+40, 5, 20)
    frontleg2 = pygame.Rect(X+30, Y+40, 5, 20)
    pygame.draw.rect(surface, goat_gray, frontleg1)
    pygame.draw.rect(surface, goat_gray, frontleg2)

    #Back legs(X,Y,width,height)
    backleg1 = pygame.Rect(X+65, Y+40, 5, 20)
    backleg2 = pygame.Rect(X+85, Y+40, 5, 20)
    pygame.draw.rect(surface, goat_gray, backleg1)
    pygame.draw.rect(surface, goat_gray, backleg2)

def game():
    score = 0
    goat_x = 50
    goat_y = 100
    speed = 10

    goat_width = 100
    goat_height = 50
    
    rock_width = 300
    rock_height = 200
    rock_x = 500
    rock_y = goat_y + 50
    rock_speed = 2
    leaf_width = 50
    leaf_height = 50
    leaf_x = 500
    leaf_y = goat_y - 50
    rock2_width = 150
    rock2_height = 100
    rock2_x = 250
    rock2_y = goat_y + 25
    rock2_speed = 1
    leaf2_width = 100
    leaf2_height = 50
    leaf2_x = 400
    leaf2_y = 500


    rock_touching = False
    rock2_touching = False
    rock2_rect = pygame.Rect(rock2_x, rock2_y, rock2_width, rock2_height)


    start_ticks = pygame.time.get_ticks()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(sky_blue)
        #calculate time
        elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000
        time_left = time_limit - elapsed_seconds
        if time_left < 0:
            time_left = 0
        #draw timer
        timer_text = font.render("Time: " + str(time_left), True, (0, 0, 150))
        screen.blit(timer_text, (650, 10))
    


        keys = pygame.key.get_pressed()
        speed = 5
                                        
        #Goat movement
        if keys[pygame.K_LEFT]:
            goat_x -= speed
        if keys[pygame.K_RIGHT]:
            goat_x += speed
        if keys[pygame.K_UP]:
            goat_y -= speed
        if keys[pygame.K_DOWN]:
            goat_y += speed
                                        
        #Keep the goat on screen
        if goat_x < 0:
            goat_x = 0
        if goat_x > width - goat_width:
            goat_x = width - goat_width
        if goat_y < 0:
            goat_y = 0
        if goat_y > height - goat_height:
            goat_y = height - goat_height

        #move the rocks
        rock2_y += rock2_speed
        if rock2_y <= 0:
            rock2_y = 0
            rock2_speed *= -1
        elif rock2_y + 100 >= height:
            rock2_y = height - 100
            rock2_speed *= -1

           
                                            
        goat_rect = pygame.Rect(goat_x, goat_y, goat_width, goat_height)
                                       
                                         
        draw_captainchaser(screen, goat_x, goat_y)

        leaf_rect = pygame.Rect(leaf_x, leaf_y, 40, 20)
        pygame.draw.rect(screen, grass_green, leaf_rect)

        leaf2_rect = pygame.Rect(leaf2_x, leaf2_y, 60, 30)
        pygame.draw.rect(screen, grass_green, leaf2_rect)

        rock_rect = pygame.Rect(rock_x, rock_y, 100, 50)
        pygame.draw.rect(screen, goat_gray, rock_rect)

        rock2_rect = pygame.Rect(rock2_x, rock2_y, 200, 100)
        pygame.draw.rect(screen, goat_gray, rock2_rect)
                                        
        #updates score each time
        if goat_rect.colliderect(leaf_rect):
            score += 1
            leaf_x = random.randint(0, width - leaf_width)
            leaf_y = random.randint(0, height - leaf_height)
        if goat_rect.colliderect(leaf2_rect):
            score += 1
            leaf2_x = random.randint(0, width - leaf2_width)
            leaf2_y = random.randint(0, height - leaf2_height)
                                            
        touching_rock = goat_rect.colliderect(rock_rect)

        if touching_rock and not rock_touching:
            score -= 1
                                            
        rock_touching = touching_rock
                                        
        touching_rock2 = goat_rect.colliderect(rock2_rect)

        if touching_rock2 and not rock2_touching:
            score -= 1

        rock2_touching = touching_rock2
                                        

        #draw the score
        score_text = font.render("Score: " + str(score), True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
                                        
        #Win condition
        if score > 5:
            text = font.render("YOU WIN!", True, (0, 250, 0))
            pygame.draw.circle(screen, balloon_blue, (400, 200), 40)
            pygame.draw.line(screen, balloon_string, (400, 240), (400, 320), 5)
            screen.blit(text, (250, 250))
            pygame.display.flip()
            pygame.time.wait(5000)
            running = False
        #Lose condition
        if score < -10:
            text = font.render("YOU LOSE. GAME OVER!", True, (250, 0, 0))
            pygame.draw.circle(screen, face_blue, (400, 200), 50)
            pygame.draw.circle(screen, (0, 0, 0), (380, 180), 8)
            pygame.draw.circle(screen, (0, 0, 0), (420, 180), 8)
            pygame.draw.arc(screen, (0, 0, 0), (360, 190, 80, 60), 0, 3.14, 4)
            screen.blit(text, (250, 250))
            pygame.display.flip()
            pygame.time.wait(5000)
            running = False
        #Time up condition
        if time_left == 0:
            text = font.render("TIME'S UP! GAME OVER!", True, (250, 0, 0))
            screen.blit(text, (250, 250))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False
            
        
        pygame.display.flip()
#ask user to play again
def restart_screen():
    while True:
        screen.fill(sky_blue)
        title = font.render("Do you want to play again?", True, (0, 0, 250))
        option1 = font.render("Press SPACE to play again", True, (0, 0, 250))
        option2 = font.render("Press ESC to quit", True, (0, 0, 250))
        title_x = width // 2 - title.get_width() // 2
        option1_x = width // 2 - option1.get_width() // 2
        option2_x = width // 2 - option2.get_width() // 2
        title_y = height // 2 - 60
        option1_y = height // 2
        option2_y = height // 2 + 60
        screen.blit(title, (title_x, title_y))
        screen.blit(option1, (option1_x, option1_y))
        screen.blit(option2, (option2_x, option2_y))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False
            
def main():
    while True:
        game()
        if not restart_screen():
            break
    pygame.quit()
    sys.exit()
main()
