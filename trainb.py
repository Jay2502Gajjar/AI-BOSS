import random
import time
import matplotlib.pyplot as plt

# BOSS actions
# 0 - attack
# 1 - defend
# 2 - heal
# 3 - move closer
# 4 - move away

actions = [0,1,2,3,4]
r_per_ep = []

#state = (boss_hp,player_hp,dist)
states = []

for b in range(3):
    for p in range(3):
        for d in range(2):
            states.append((b,p,d))


Q = {}
for s in states:
    for a in actions:
        Q[(s,a)] = 0.0


alpha = 0.1
gamma = 0.9
epsilon = 0.2

ep_min = 0.05
ep_dec = 0.995


def choose_action(state):
    if random.random() < epsilon:
        return random.choice(actions)
    else:

        qs = []

        for a in actions:
            qs.append(Q[(state,a)])

        return actions[qs.index(max(qs))]


def step(state, action):
    boss_hp, player_hp, distance = state
    reward = 0
    done = False
    boss_action = "NONE"
    player_action = "NONE"


    if action == 0 and distance == 0:        #attack
        player_hp -= 1
        reward += 10
        boss_action = "boss attacks"

    elif action == 0 and distance == 1:
        reward -= 5
        boss_action = "cannot hit player too far"

    elif action == 1:                        #defend
        boss_action = "boss defends"

    elif action == 2 and boss_hp < 2:        #heal
        boss_hp += 1
        reward += 5
        boss_action = "heals"

    elif action == 2 and boss_hp == 2:
        reward -= 5
        boss_action = "HP full heal wasted"

    elif action == 3:                        #move closer
        distance = 0
        reward += 1
        boss_action = "boss moves closer"

    elif action == 4:                        #move away
        distance = 1
        reward -= 1
        boss_action = "boss moves away"


    if player_hp > 0 and distance == 0 and random.random() < 0.6:
        if action == 1:
            reward += 5
            boss_action += " | blocked player"
            player_action = "Player attacks (hit blocked)"
        else:
            boss_hp -= 1
            reward -= 10
            boss_action += " | took damage"
            player_action = "player attacks"
    else:
        player_action = "player does nothing"

    boss_hp = max(0,boss_hp)
    player_hp = max(0,player_hp)

    if player_hp <=0:
        reward += 100
        done = True
        boss_action += " | BOSS WINS"
        player_action = "PLAYER DEFEATED"

    elif boss_hp <= 0:
        reward -= 100
        done = True
        boss_action += " | BOSS DIES"
        player_action = "PLAYER WINS"


    return (boss_hp, player_hp, distance), reward, done, boss_action, player_action


eps = 200

for ep in range(eps):
    state = (2,2,1)
    done = False
    steps = 0
    treward = 0
    MAX_STEPS = 20

    while not done and steps<MAX_STEPS:
        action = choose_action(state)
        ns,reward,done, _,_= step(state,action)

        qold = Q[(state,action)]
        if done:
            bqn = 0
        else:
            bqn = max(Q[(ns,a)] for a in actions)

        Q[(state,action)] = qold +alpha*(reward + gamma*bqn-qold)

        state = ns
        treward += reward
        steps +=1

    print("episode:",ep,"total reward:",treward)
    r_per_ep.append(treward)

    if epsilon>ep_min:
        epsilon *= ep_dec


plt.plot(r_per_ep)
plt.xlabel("episode")
plt.ylabel("total reward")
plt.title("learning curve")
plt.show()



epsilon = 0
state = (2,2,1)
done = False
step_no = 1

print("\n------------testing------------\n")

while not done:
    action = choose_action(state)
    ns, reward, done, boss_action, player_action = step(state,action)

    print("step:",step_no)
    print("state:",state)
    print("bboss action  :",boss_action)
    print("Player action:",player_action)
    print("Next state:",ns)
    print("Reward:",reward)
    print("-"*30)

    state = ns
    step_no += 1
   



if __name__ == "__main__":
    pass
