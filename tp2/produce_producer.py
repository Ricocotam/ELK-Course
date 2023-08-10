import subprocess
from glob import glob

with open("output.log", "a") as logfile:
    ps = []
    for fn in glob("*.txt"):
        print(f"starting producer on {fn}")
        p = subprocess.Popen(["python", "producer.py", fn], stdout=logfile, stderr=logfile)
        ps.append(p)

    for p in ps:
        p.wait()

