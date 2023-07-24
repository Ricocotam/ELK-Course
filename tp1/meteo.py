import os
import requests
import pandas as pd
from tqdm import trange
from glob import glob
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch

url = "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.{yyyy}{mm:02d}.csv.gz"
os.mkdir("data")
for yyyy in range(1996, 1999):
    for mm in trange(1, 12):
        url_ = url.format(yyyy=yyyy, mm=mm)
        r = requests.get(url_)
        with open(f"data/{yyyy}{mm:02d}.csv.gz", "wb") as f:
            f.write(r.content)

os.system("gzip -d data/*.gz")


es = Elasticsearch("http://elastic:changeme@localhost:9200")
for fn in tqdm(glob("data/*.csv")):
    df = pd.read_csv(fn)
    df["_index"] = "elk-course-0001"
    df["_op_type"] = "index"
    bulk(es, df.to_json(orient="records")) 
