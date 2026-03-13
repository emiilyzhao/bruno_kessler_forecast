# Installation

## Prerequisites
1. **Python Installation**: Ensure you have Python installed on your system (Python 3.6 or later).
2. **Git Installation**: Ensure you have Git installed on your system.
3. **Streamlit Installation**: Ensure Streamlit is installed. If not, you can install it using `pip`.


### 1. Clone the GitHub Repository

Open your command line interface (CLI) and clone the repository using the `git clone` command. Replace `<repository-url>` with the actual URL of the GitHub repository.
```bash
git clone <repository-url>
```

### 2. Navigate to the Repository Directory

Change your directory to the floned repository folder.

```bash
cd repository 
```

### 3. Install the Dependencies

Install the required dependencies using: 

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit script

Run the script named ` ` using the Streamlit CLI command:

```bash 
streamlit run app.py
```

### 5. Access the Application in Browser

After running the command, Streamlit will start a local server and provide you with a URL (usually http://localhost:8501). Open this URL in your web browser to access your Streamlit application.


## Dependencies

``` python
import os
from glob import glob
import datetime
import folium
import geopandas as gpd
import h5py
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import seaborn as sns
import xarray as xr
from folium.plugins import Draw
from plotly.subplots import make_subplots
from scipy.stats import skew, kurtosis, t
from shapely import geometry
import streamlit as st
from streamlit_folium import st_folium
 
from plotting.functions.plot_EFD import plot_EFD
# from plotting.functions.plot_EFD_merged import plot_EFD
from plotting.functions.plot_LAP import lap_plot
from plotting.functions.plot_LAP import aggregated_LAP_electron
from plotting.functions.plot_HEPPX import heppx_plot
from plotting.functions.plot_SCM import scmplot
from plotting.functions.plot_SCM import aggregated_SCM_angles
from plotting.functions.plot_SCM import aggregated_SCM_waveform
from plotting.functions.plot_sequential_SCM import plot_sequential_SCM
from plotting.functions.plot_sequential_EFD import plot_sequential_EFD
from plotting.functions.plot_sequential_HEPPL import plot_sequential_HEPPL
from plotting.functions.plot_sequential_HEPPX import plot_sequential_HEPPX
from plotting.functions.HEPPH_MUL_plot import plot_sequential_HEPPH
from plotting.functions.HEPD_V2_fixed import plot_HEPPD
from plotting.functions.HEPPD_Mul_plot import plot_HEPD_multiple_files
from plotting.functions.LAP_Mul_plot_Final import plot_sequential_LAP
# from plotting.functions.HEPPL_Mul_plot import plosequential_HEPPL
# from plotting.functions.plot_sequential_HEPPL import plot_proton_electron_count_verse_time
from plotting.functions.plot_HEPPL import plot_proton_electron_count_verse_time
from plotting.functions.plot_HEPPH import plotheph
from plotting.functions.plot_HEPPD import plot_HEPD
from plotting.functions.plot_HEPPL import plot_hepl
```
