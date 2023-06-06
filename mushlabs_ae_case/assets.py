import pandas as pd
import numpy as np # add
import json #add
import requests #add
import random
#from assets_dbt_python.utils import random_data
from dagster import asset
from dagster_dbt import load_assets_from_dbt_project

from mushlabs_ae_case.resources import DBT_PROFILE_DIR, DBT_PROJECT_DIR, IGHOODataResource

dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_DIR,
    profiles_dir=DBT_PROFILE_DIR,
)


@asset(key_prefix=["core"], compute_kind="pandas")
def raw_gho_gender_inequality(
    gho: IGHOODataResource,
) -> pd.DataFrame:
    "this is gender inequality"
    endpoint = "MDG_0000000015"
    response = gho.make_api_call(endpoint)
    json_data = response['value']
    valueRaw = [row.get("Value") for row in json_data] #number of people affected
    gender = [row.get("Dim1") for row in json_data] #gender
    df = pd.DataFrame({"Value": valueRaw, "Dim1": gender})
    print(df)
    return df
    ...


@asset(key_prefix=["core"], compute_kind="pandas")
def raw_gho_countries(
    gho: IGHOODataResource,
) -> pd.DataFrame:
    ###################added by me##############################
    "this is raw countries" 
    #endpoint = "RegionCountry"
    endpoint = "MDG_0000000015"
    response = gho.make_api_call(endpoint)
    json_data = response['value']
    # region_names = [row.get("RegionName") for row in json_data]
    # country_names = [row.get("CountryName") for row in json_data]
    timedime = [row.get("TimeDim") for row in json_data] # time
    spatial_dim = [row.get("SpatialDim") for row in json_data]  #country name
    df1 = pd.DataFrame({"TimeDim": timedime, "SpatialDim": spatial_dim})
    return df1
    ...

