#!/usr/bin/env python
#This scrupt works for the green taxi data ingestion
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import  tqdm

year = 2025
month = 11

pg_user = "postgres"
pg_password = "postgres"
pg_host = "postgres"
pg_port = 5432
pg_db = "ny_taxi"

table_name = "green_taxi_data"


prefix = "https://d37ci6vzurychx.cloudfront.net/trip-data"
url = f"{prefix}/green_tripdata_{year}-{month:02d}.parquet"



#df_taxi=pd.read_parquet("https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet")



#df_lookup=pd.read_csv("https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv")



engine = create_engine(
    "postgresql://postgres:postgres@postgres:5432/ny_taxi"
)



def run():
    df = pd.read_parquet(url)

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
