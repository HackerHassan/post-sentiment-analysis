# ---------| imports |---------
import plotly.express as px
import gmaps.datasets
import gmaps
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from PIL import Image
import ast
# importing the function files
import functions
import product_functions
# ---------| imports |---------

# over here we are opening the 5p logo to personalize the Dash
image = Image.open('5P-ENG Logomark-White_5X.png')
# st.image(image, caption='')

col1, col2 = st.beta_columns(2)
with col1: st.image(image)
with col2: st.title('Analytics')

company_name = '5ivepillars'

# input_password = st.text_input('Password', 'Enter Password')
# st.write('The password you entered is incorrect, please try again')

# st.title('{company_name} Sample Dash'.format(company_name=company_name));
# st.title('Analytics Dashboard')
