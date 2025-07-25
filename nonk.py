import time
import random as rand

def wait(ms: int):
    time.sleep(ms / 1000)

r, g, b = 0, 0, 0

def sethex():
    global r, g, b
    r += rand.randint(0,10)
    g += rand.randint(0,10)
    b += rand.randint(0,10)
    return r,g,b

for count in range(30):
    sethex()
    print(f"\033[38;2;{r};{g};{b}mpoo")
    wait(100)