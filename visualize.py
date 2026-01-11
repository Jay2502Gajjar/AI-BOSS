import pygame
import time

from trainb import choose_action, step

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RL Boss - Step 4")

font = pygame.font.SysFont(None, 26)
clock = pygame.time.Clock()

epsilon = 0

state = (2, 2, 1)
done = False

boss_action_text = ""
player_action_text = ""

last_step_time = time.time()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not done and time.time() - last_step_time >= 1:
        action = choose_action(state)
        state, reward, done, boss_action_text, player_action_text = step(state, action)
        last_step_time = time.time()

    screen.fill((255, 255, 255))

    boss_hp, player_hp, dist = state

    screen.blit(font.render(f"Boss HP: {boss_hp}", True, (0,0,0)), (40, 40))
    screen.blit(font.render(f"Player HP: {player_hp}", True, (0,0,0)), (40, 80))
    screen.blit(font.render(f"Distance: {'Close' if dist == 0 else 'Far'}", True, (0,0,0)), (40, 120))

    screen.blit(font.render(f"Boss Action: {boss_action_text}", True, (0,0,150)), (40, 180))
    screen.blit(font.render(f"Player Action: {player_action_text}", True, (150,0,0)), (40, 220))

    if done:
        screen.blit(font.render("GAME OVER", True, (200,0,0)), (40, 280))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
