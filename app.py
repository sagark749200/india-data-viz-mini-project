import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
st.set_page_config(layout="wide")

final_df = pd.read_csv('India.csv')
list_of_states = list(final_df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India ka data Viz')
selected_state = st.sidebar.selectbox('Select State',list_of_states)
primary = st.sidebar.selectbox('Select Primary parameter',sorted(final_df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary parameter',sorted(final_df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:

    st.text('Size represent primary parameter')
    st.text('color represent secondary parameter')
    if selected_state == 'Overall India':
        # plotting for india
        fig = px.scatter_map(final_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,
                             map_style="carto-positron",size_max=35,width=1200,height=700,color_continuous_scale="inferno",hover_name="District")

        st.plotly_chart(fig,use_container_width=True)
    else:
        #plot for states
        state_df = final_df[final_df['State'] == selected_state]

        fig = px.scatter_map(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=6,
                             map_style="carto-positron", size_max=35, width=1200, height=700,
                             color_continuous_scale="inferno",hover_name="District")

        st.plotly_chart(fig, use_container_width=True)


