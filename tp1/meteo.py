import os
from uuid import uuid4
import requests
import pandas as pd
from tqdm import trange, tqdm
from glob import glob
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch

url = "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.{yyyy}{mm:02d}.csv.gz"
os.mkdir("data")
for yyyy in range(1996, 2022):
    for mm in trange(1, 12):
        url_ = url.format(yyyy=yyyy, mm=mm)
        r = requests.get(url_)
        with open(f"data/{yyyy}{mm:02d}.csv.gz", "wb") as f:
            f.write(r.content)

os.system("gzip -d data/*.gz")

es = Elasticsearch("http://elastic:changeme@localhost:9200")
def doc_generator(df, fn):
    df_iter = df.iterrows()
    for index, document in df_iter:
        d = {
                "_index": 'elk-meteo-0001',
                "_op_type": "create",
                "_id" : f"{uuid4()}",
                "_source": document.to_json(),
            }
        yield d


for fn in tqdm(glob("data/*.csv")):
    df = pd.read_csv(fn, sep=";")
    bulk(es, doc_generator(df, fn))
