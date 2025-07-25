import time
import colorist as color
import random as rand

def wait(ms: int):
    time.sleep(ms / 1000)

def sethex():
    r + rand.randint(0,2)
    g + rand.randint(0,2)
    b + rand.randint(0,2)

for count in range(300):
    sethex()
    print(f"\033[38;2;{r};{g};{b}mpoo")
    wait(100)