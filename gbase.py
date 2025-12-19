import random
import time

boss_hp = 2
p_hp = 2
distance =1  #0 = close , 1 =far

actions = ["attack","defend","heal","move_closer","move_away"]

print("====Game start====")

while boss_hp >0 and p_hp >0:
    reward = -1
    print("\n----------------")
    print("Boss HP:",boss_hp)
    print("Player HP:",p_hp)
   
    if distance == 0:
        print("Distance : Close")
    else:
        print("Distance: Far")

    action = random.choice(actions)
    print("Boss does: ",action)

    if action == "attack" and distance == 0:
        p_hp -= 1
        reward += 10
        print("Boss hits player")

    elif action == "attack" and distance == 1:
        reward -= 3
        print("Boss attacks but is too far")

    elif action == "heal" and boss_hp<2:
        boss_hp += 1
        reward += 5
        print("Boss heals")

    elif action == "heal" and boss_hp == 2:
        reward -= 5
        print("Boss is at max health no healing done")
    
    elif action == "move_closer":
        distance = 0

    elif action == "move_away":
        distance = 1
    
    if random.random() < 0.4:
        print("Player attacks")

        if action == "defend":
            reward += 5
            print("Boss defended itself")
        elif distance == 0:
            
            boss_hp -= 1
            reward -= 10
            print("Player hits boss")
        elif distance == 1:
            print("Cannot hit boss at this distance")
    
    if p_hp <= 0:
        reward += 100
        print("\nBoss wins the fight")
        break

    if boss_hp <= 0:
        reward -= 100
        print("\nPlayer wins the fight")
        break

    print("Reward this turn:",reward)
    time.sleep(1)


