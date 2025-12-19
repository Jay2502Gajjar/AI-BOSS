states = []

for b in range(3):
    for p in range(3):
        for d in range(2):
            states.append((b,p,d))


actions = [0,1,2,3,4]
#0 - attack
#1 - defend
#2 - heal
#3 - move closer
#4 - move away

Q = {}

for s in states:
    for a in actions:
        Q[(s,a)] = 0.0

print("total states:",len(states))
print("total state action pairs", len(Q))