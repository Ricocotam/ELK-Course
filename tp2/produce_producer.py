import subprocess
from glob import glob

with open("data/output.log", "a") as logfile:
    ps = []
    print("output log openned")
    for fn in glob("/myfiles/data/*.txt"):
        print(f"starting producer on {fn}")
        p = subprocess.Popen(["python", "/myfiles/producer.py", fn], stdout=logfile, stderr=logfile)
        ps.append(p)

    for p in ps:
        p.wait()

