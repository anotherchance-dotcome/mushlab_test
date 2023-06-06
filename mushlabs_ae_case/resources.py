import os
from abc import abstractmethod
from typing import Optional

import requests
from dagster import ConfigurableResource, get_dagster_logger
from dagster_dbt import DbtCliClientResource
from dagster_duckdb_pandas import DuckDBPandasIOManager
from pydantic import Field

# get path from root because the dbt cli is a little buggy with relative paths
FILE_PATH = os.path.dirname(os.path.abspath(__file__))

DBT_PROJECT_DIR = os.path.join(FILE_PATH, "dbt_project")
#DBT_PROJECT_DIR = os.path.join(FILE_PATH, "mushlabs_ae_case")
DBT_PROFILE_DIR = os.path.join(DBT_PROJECT_DIR, "profiles")

logger = get_dagster_logger()

duckdb_io_manager = DuckDBPandasIOManager(
    database=os.path.join(FILE_PATH, "..", "dbt_duckdb.db")
)


class IGHOODataResource(ConfigurableResource):
    @abstractmethod
    def make_api_call(self, *args, **kwargs) -> dict:
        raise NotImplementedError()


class GHOODataResource(IGHOODataResource):
    base_url: str = Field(
        "https://ghoapi.azureedge.net/api/", description="GHO API base url"
    )
    #'f(https://ghoapi.azureedge.net/api/{endpoint})'
    def make_api_call(
        self,
        # more params are needed
        endpoint:str,
        *args,
        #endpoint# add
        **kwargs
    ) -> dict:
        url = self.base_url + endpoint
        response = requests.get(url,*args,**kwargs)
        return response.json()
        ...


resource_def = {
    "LOCAL": {
        "io_manager": duckdb_io_manager,
        "gho": GHOODataResource.configure_at_launch(),
        "dbt": DbtCliClientResource(
            project_dir=DBT_PROJECT_DIR,
            profiles_dir=DBT_PROFILE_DIR,
            target="local",
        ),
    },
}
