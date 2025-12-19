import random 

actions = [0,1,2,3,4]
#0 - attack
#1 - defend
#2 - heal
#3 - move closer
#4 - move away

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
epsilon = 0.2 # for the random action

def choose_action(state):
    if random.random() < epsilon:
        return random.choice(actions)
    else:
       
        qs = []

        for a in actions:
            val = Q[(state, a)]
            qs.append(val)

        return actions[qs.index(max(qs))]

def step(state, action):
    boss_hp, player_hp, distance = state
    reward = 0
    done = False

    if action == 0 and distance == 0:
        player_hp -= 1
        reward = 10

    elif action == 0 and distance == 1:
        reward = -3

    elif action == 2 and boss_hp < 2:
        boss_hp += 1
        reward = 5

    elif action == 2 and boss_hp == 2:
        reward = -5

    elif action == 3:
        distance = 0
        reward = -1

    elif action == 4:
        distance = 1
        reward = -1
    
    boss_hp = max(0, boss_hp)
    player_hp = max(0, player_hp)

    return (boss_hp, player_hp, distance), reward, done

    
state = (2,2,1)
done = False
steps = 0
MAX_STEPS = 20

while not done and steps < MAX_STEPS:

    action = choose_action(state)
    print("State:",state," Action: ",action)

    ns,reward ,done= step(state,action)
    print("Next state:", ns, "Reward: ",reward)

    state = ns
    steps +=1

if steps >= MAX_STEPS:
    print("Episode ended due to time limit")

   
