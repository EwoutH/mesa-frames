from collections.abc import Collection
from typing import Literal

import pandas as pd
import polars as pl
from numpy import ndarray

####----- Agnostic Types -----####
AgnosticMask = Literal["all", "active"] | None
AgnosticIds = int | Collection[int]

###----- Pandas Types -----###

ArrayLike = pd.api.extensions.ExtensionArray | ndarray
AnyArrayLike = ArrayLike | pd.Index | pd.Series
PandasMaskLike = AgnosticMask | pd.Series | pd.DataFrame | AnyArrayLike
PandasIdsLike = AgnosticIds | pd.Series | pd.Index

###----- Polars Types -----###

PolarsMaskLike = AgnosticMask | pl.Expr | pl.Series | pl.DataFrame | Collection[int]
PolarsIdsLike = AgnosticIds | pl.Series

###----- Generic -----###

DataFrame = pd.DataFrame | pl.DataFrame
Series = pd.Series | pl.Series
Index = pd.Index | pl.Series
BoolSeries = pd.Series | pl.Series
MaskLike = AgnosticMask | PandasMaskLike | PolarsMaskLike
IdsLike = AgnosticIds | PandasIdsLike | PolarsIdsLike

###----- Time ------###
TimeT = float | int
