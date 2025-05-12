import random
counters = [0] * 6
for _ in range(6000):
    tmpe = random.randint(1, 6)
    counters[tmpe - 1] += 1
for i in range(6):
    print(f"{i + 1}: {counters[i]}")

