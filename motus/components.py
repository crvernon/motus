from typing import Dict, List

import numpy as np
import pandas as pd
from hamilton.function_modifiers import tag, extract_columns, extract_fields, model

from .models import tell


def yearly_county_population_fields_expected(target_year: int) -> List[str]:
    """List of expected fields in the county population data.

    """

    return ['county_FIPS', f'pop_{target_year}']


def yearly_county_population_fields_rename(target_year: int,
                                           population_field_name: str = "Population") -> dict:
    """List of expected fields in the county population data.

    """

    return {'county_FIPS': 'County_FIPS',
            f'pop_{target_year}': population_field_name}


def yearly_county_population_historic(county_population_by_year_file: str,
                                      target_year: int,
                                      yearly_county_population_fields_expected: List[str],
                                      yearly_county_population_fields_rename: dict,
                                      # index_col: None = None,
                                      header: int = 0,
                                      sort_field_name: str = "County_FIPS",
                                      population_field_name: str = "Population"
                                      ) -> pd.Series:
    """Ingest county population data.

    """

    df = pd.read_csv(county_population_by_year_file,
                       index_col=None,
                       header=header)[yearly_county_population_fields_expected]

    df.rename(columns=yearly_county_population_fields_rename, inplace=True)

    df.sort_values(sort_field_name, inplace=True)

    df[population_field_name] = df[population_field_name].round(0).astype(int)

    return df[population_field_name]



def wrf_to_mean_balancing_authority_historical(max_year: int,
                                               yearly_county_population: pd.Series,
                                               ) -> pd.Series:
    pass


def balancing_authority_population_yearly(target_year: int,
                                          population: pd.Series) -> pd.Series:
    """Compute a series of population data aggregated """

    return population * target_year


@extract_fields({"x_train": np.ndarray, "x_test": np.ndarray})
def my_data() -> Dict[str, np.ndarray]:
    """asdf"""

    return {"x_train": np.array([1, 2, 3]),
            "x_test": np.array([1, 2, 3])}


@tag(experiment="b", subexperiment="n1")
# @model(Tell, "balancing_authority_population_yearly")
def electricity_demand_by_year(balancing_authority_population_yearly: pd.Series) -> pd.Series:

    return balancing_authority_population_yearly * 2


