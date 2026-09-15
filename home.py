import geopandas as gpd
import numpy as np
import pandas as pd
import streamlit as st

from joblib import load
from notebooks.src.config import DADOS_GEO_MEDIAN, DADOS_LIMPOS, MODELO_FINAL

st.title("Previsão de preços de imóveis na California(USA)")