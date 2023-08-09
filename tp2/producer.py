import sys
import time
import random

if __name__ == "__main__":
    fn = sys.argv[1]
    with open(fn, "r") as f:
        for ln, lc in enumerate(f.readlines()):
            r = random.random()
            time.sleep(1 + r - 0.5)
            print(f"{fn} #{ln} - {lc}")

