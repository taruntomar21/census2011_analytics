import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from DB import DataBase

db = DataBase()

st.header('India Census Analysis (2011) by Maping')

# final_df = pd.read_csv('india-census.csv')

# list_of_states = list(final_df['State'].unique())
# list_of_states.insert(0,'Overall India')
# list_of_districts = list(final_df['District'].sort_values())

st.sidebar.title('India Census Analysis')
st.text("---------------------------------------------------------------------------------------------------------------------------------------------")
States = db.fetch_states()

select = st.sidebar.selectbox(
    'Select',
    ["About","States & UTs", "District"]
)

if select == "States & UTs":
    select_state = st.sidebar.selectbox('Select State & UT', States)
    # select_district = st.sidebar.selectbox('Select District',list_of_districts)

    # primary = st.sidebar.selectbox('Select Primary Parameter',sorted(final_df.columns[5:]))
    # secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(final_df.columns[5:]))
    #

    if select_state:

        col1, col2, col3 = st.columns(3)
        with col1:
            # st.text(select_state)
            ppl = db.fetch_population(select_state)
            st.code('Population - {ppl}'.format(ppl=ppl))
        with col2:
            dist = db.fetch_district(select_state)
            # st.subheader(dist)
            st.code('Total Districts - {dist}'.format(dist=dist))
        with col3:
            lit = db.fetch_litracy(select_state)
            st.code('Avg Litracy Rate - {lit}'.format(lit=lit))

        st.text("---------------------------------------------------------------------------------------------------------------------------------------------")

        col1, col2 = st.columns(2)
        with col1:
            male = db.fetch_male(select_state)
            st.code('Total Male - {male}'.format(male=male))

        with col2:
            female = db.fetch_female(select_state)
            st.code('Total Female - {female}'.format(female=female))

        st.text(
            "---------------------------------------------------------------------------------------------------------------------------------------------")

        col1, col2, col3 = st.columns(3)
        with col1:
            hindu = db.fetch_hindu(select_state)
            st.code("Total Hindus - {hindu}".format(hindu=hindu))

        with col2:
            muslims = db.fetch_muslim(select_state)
            st.code('Total Muslims - {muslims}'.format(muslims=muslims))

        with col3:
            Christians = db.fetch_Christians(select_state)
            st.code('Total Christians - {Christians}'.format(Christians=Christians))

        st.text(
            "---------------------------------------------------------------------------------------------------------------------------------------------")

        col1, col2, col3 = st.columns(3)
        with col1:
            sikhs = db.fetch_sikhs(select_state)
            st.code('Total Sikhs - {sikhs}'.format(sikhs=sikhs))

        with col2:
            Buddhists = db.fetch_Buddhists(select_state)
            st.code('Total Buddhists - {Buddhists}'.format(Buddhists=Buddhists))

        with col3:
            jains = db.fetch_jains(select_state)
            st.code('Total Jains - {jains}'.format(jains=jains))


if select == "District":

    select_state = st.sidebar.selectbox('Select State & UT', States)
    # select_district = st.sidebar.selectbox('Select District',list_of_districts)

    # primary = st.sidebar.selectbox('Select Primary Parameter',sorted(final_df.columns[5:]))
    # secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(final_df.columns[5:]))
    #

    if select_state:
        dists = db.fetch_districts(select_state)
        select_dist = st.sidebar.selectbox("{state}_District".format(state=select_state), dists)

        if select_dist:
            col1, col2, col3 = st.columns(3)
            with col1:
                pass

    # dist_up = db.up_districts()
    # up_districts = st.sidebar.selectbox('UP', dist_up)
    #
    # dist_andhra = db.andhra_districts()
    # andhra_districts = st.sidebar.selectbox('Andhra Pradesh', dist_andhra)
    #
    # dist_arunachal = db.arunachal_districts()
    # arunachal_districts = st.sidebar.selectbox('Arunachal Pradesh', dist_arunachal)

# plot = st.sidebar.button('Plot Map')
#
# if plot:
#     st.text('primary parameter represent size')
#     st.text('secondary parameter represent color')
#
#     if select_state == 'Overall India':
#         # plot for india
#         fig = px.scatter_mapbox(final_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=3.5, size_max=35
#                                 ,mapbox_style='open-street-map', width=1300, height=700, hover_name='District')
#
#         st.plotly_chart(fig, use_container_width=True)
#     else:
#         # plot for state
#         state_df = final_df[final_df['State'] == select_state]
#
#         fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=5,
#                                 size_max=35,mapbox_style="carto-positron", width=1400, height=700, hover_name='District')
#
#         st.plotly_chart(fig, use_container_width=True)
