#!/usr/bin/env python
#This scrupt works for the green taxi data ingestion
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import  tqdm


pg_user = "postgres"
pg_password = "postgres"
pg_host = "localhost"
pg_port = 5433
pg_db = "ny_taxi"

table_name = "lookup_data"


prefix = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc"
url = f"{prefix}/taxi_zone_lookup.csv"



#df_taxi=pd.read_parquet("https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet")



#df_lookup=pd.read_csv("https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv")



engine = create_engine(
    "postgresql://postgres:postgres@localhost:5433/ny_taxi"
)



def run():
    df = pd.read_csv(url)

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False,
        method="multi",
        chunksize=10000
    )



if __name__ == "__main__":
    run()
