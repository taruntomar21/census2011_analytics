import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from DB import DataBase
import json
import os
import requests
import streamlit.components.v1 as components


db = DataBase()

st.header('India Census Analytics Dashboard (2011)')

# final_df = pd.read_csv('india-census.csv')

# list_of_states = list(final_df['State'].unique())
# list_of_states.insert(0,'Overall India')
# list_of_districts = list(final_df['District'].sort_values())

st.sidebar.title('India Census Analysis')
st.text("---------------------------------------------------------------------------------------------------------------------------------------------")
States = db.fetch_states()

select = st.sidebar.selectbox(
    'Select',
    ["About the Project","Overall India","States & UTs", "District"]
)

if select == "About the Project":
    # About button in sidebar
        with st.expander("About This Project"):
            st.markdown("""
            #### India Census Analysis 2011
            ---
            **A data-driven web application** built to explore and visualize 
            India's 2011 Census data interactively.

            ---
            #### Objective
            To make India's Census 2011 data accessible and understandable 
            through interactive visualizations — helping users explore 
            demographic, social, and economic patterns across every 
            state and district of India.
            """)

        with st.expander("About Dataset"):
            st.markdown("""
            ### India Census 2011 Dataset
            ---
            **Source:** Office of the Registrar General  
            & Census Commissioner, India

            ---
            ### Dataset Size
            - **Rows:** 502 (one per district)
            - **Columns:** 75
            - **States/UTs:** 31
            - **Districts:** 502
            - **Missing Values:** None

            ---
            ### Column Categories

            ##### Geography (4 cols) - 
            State, District, Latitude, Longitude

            #### Demographics (5 cols) - 
            Population, Male, Female, Sex Ratio, Literacy Rate

            #### Literacy & Education (10 cols) - 
            Literate, Male Literate, Female Literate, Below Primary, Primary, Middle, Secondary, Higher, Graduate, Other Education

            #### Workers (5 cols) - 
            Workers, Male Workers, Female Workers, Non Workers, Agricultural Workers

            #### Religion (7 cols) - 
            Hindus, Muslims, Christians, Sikhs, Buddhists, Jains, Others

            #### Households (12 cols) - 
            Rural, Urban, Owned, Rented, Household sizes 1 to 9+ persons

            #### Assets (5 cols) - 
            Electric Lighting, Internet, Computer, Television, Telephone/Mobile

            #### Vehicles (3 cols) - 
            Bicycle, Car/Jeep/Van, Scooter/Motorcycle/Moped

            #### Age Groups (4 cols) - 
            Age 0-29, Age 30-49, Age 50+, Age Not Stated

            #### Income/Power Parity (11 cols) - 
            Income brackets from Below ₹45,000 to Above ₹5,45,000

            ---
            ### Key Stats
            - **Min Population:** 35,320
            - **Max Population:** 1,10,60,148
            - **Coverage:** All 28 States + UTs  (Some States and UTs data are missing, I'll add it as I get.)
            - **Year:** Census 2011
            """)

        with st.expander("Key Features"):
            features = [
                ("🌍", "Interactive India Map", "State-wise choropleth with literacy rate & hover details, including clear separate boundary for each state"),
                ("👥", "Demographics", "Population, male/female ratio per state"),
                ("📚", "Literacy Analysis", "Average literacy rate across all states & UTs and Districts"),
                ("🕌", "Religion Distribution", "Bar charts for Hindus, Muslims, Christians, Sikhs, Buddhists, Jains per State & District"),
                ("🏠", "Household Analysis", "Size distribution & asset ownership charts"),
                ("🔍", "District Drill-down", "Explore individual districts within any state"),
                ("📍", "State Map View", "Scatter map showing all districts of selected state"),
                ("📊", "Dataset Explorer", "Browse, filter & download the raw census data"),
            ]

            for emoji, title, desc in features:
                st.markdown(f"""
                <div style="
                    background-color: #1e1e2e;
                    border-left: 3px solid #7c83fd;
                    border-radius: 6px;
                    padding: 8px 10px;
                    margin-bottom: 8px;
                ">
                    <div style="font-size: 14px; font-weight: 600; color: #ffffff;">
                        {emoji} {title}
                    </div>
                    <div style="font-size: 11px; color: #a0a0b0; margin-top: 2px;">
                        {desc}
                    </div>
                </div>
                """, unsafe_allow_html=True)

        with st.expander("Tech Stack"):
            tech_stack = [
                (
                    "🐍", "Python 3.x",
                    "Core Language",
                    "Backbone of the entire project. Handles data fetching, processing, business logic, and connects all components together."
                ),
                (
                    "🗄️", "MySQL",
                    "Database",
                    "Stores all 502 district-level census records. Executes optimized SQL queries (SUM, AVG, GROUP BY, CTEs) to aggregate state & district level stats on the fly."
                ),
                (
                    "🌐", "Streamlit",
                    "Web Framework",
                    "Builds the entire interactive dashboard UI — sidebar navigation, metric cards, charts, maps, and dataframes — all in pure Python with zero frontend code."
                ),
                (
                    "📊", "Plotly",
                    "Visualization",
                    "Powers all interactive charts — Bar charts for religion & household data, Choropleth map for India overview, Scatter Mapbox for district-level state maps."
                ),
                (
                    "🐼", "Pandas",
                    "Data Manipulation",
                    "Converts raw SQL query results into DataFrames. Used for filtering, column selection, hover text generation, and preparing data for Plotly charts."
                ),
                (
                    "🗺️", "GeoJSON",
                    "Map Boundaries",
                    "Provides precise geographic boundary coordinates for all Indian states. Enables Plotly to draw accurate state borders on the choropleth map."
                ),
                (
                    "🔌", "MySQL Connector",
                    "DB Driver",
                    "Official Python driver to connect, authenticate, and communicate with MySQL server. Handles parameterized queries to prevent SQL injection."
                ),
            ]

            for emoji, name, role, detail in tech_stack:
                st.markdown(f"""
                        <div style="
                            background-color: #1a1a2e;
                            border: 1px solid #2a2a4a;
                            border-radius: 8px;
                            padding: 10px 12px;
                            margin-bottom: 10px;
                        ">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div style="font-size: 14px; font-weight: 700; color: #ffffff;">
                                    {emoji} {name}
                                </div>
                                <div style="
                                    font-size: 10px;
                                    background-color: #7c83fd;
                                    color: white;
                                    padding: 2px 8px;
                                    border-radius: 10px;
                                    font-weight: 600;
                                ">
                                    {role}
                                </div>
                            </div>
                            <div style="font-size: 11px; color: #9090aa; margin-top: 5px; line-height: 1.5;">
                                {detail}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

        with st.expander("How To Use"):
                steps = [
                    {
                        "step": "01",
                        "title": "Overall India",
                        "icon": "🌍",
                        "color": "#7c83fd",
                        "description": "Get a bird's eye view of the entire country",
                        "instructions": [
                            "Select 'Overall India' from the sidebar dropdown",
                            "View the interactive choropleth map of all states",
                            "Hover over any state to see Population, Literacy Rate & State name",
                            "States are color-coded by Literacy Rate — yellow = highest, purple = lowest",
                            "Zoom in/out using scroll wheel or map controls",
                        ]
                    },
                    {
                        "step": "02",
                        "title": "States & UTs",
                        "icon": "🏛️",
                        "color": "#00c9a7",
                        "description": "Deep dive into any state or union territory",
                        "instructions": [
                            "Select 'States & UTs' from the sidebar dropdown",
                            "Choose any State or UT from the second dropdown",
                            "View Population, Total Districts & Avg Literacy Rate",
                            "Scroll down to see Male/Female population split",
                            "View Religion distribution via bar chart",
                            "Explore Household size distribution chart",
                            "See district-level scatter map of the selected state",
                        ]
                    },
                    {
                        "step": "03",
                        "title": "District",
                        "icon": "🔍",
                        "color": "#fd7cb5",
                        "description": "Explore granular data at district level",
                        "instructions": [
                            "Select 'District' from the sidebar dropdown",
                            "Choose a State first to load its districts",
                            "Select any District from the third dropdown",
                            "View district-specific Population & Literacy stats",
                            "Compare district data against state averages",
                        ]
                    },
                ]

                all_html = ""

                for s in steps:
                    instructions_html = "".join([
                        f"""
                        <div style="
                            display: flex;
                            align-items: flex-start;
                            gap: 8px;
                            margin-bottom: 6px;
                        ">
                            <span style="
                                background-color: {s['color']};
                                color: white;
                                border-radius: 50%;
                                width: 16px;
                                height: 16px;
                                font-size: 9px;
                                display: flex;
                                align-items: center;
                                justify-content: center;
                                flex-shrink: 0;
                                margin-top: 1px;
                            ">{i + 1}</span>
                            <span style="font-size: 11px; color: #b0b0c0; line-height: 1.5;">
                                {instruction}
                            </span>
                        </div>
                        """
                        for i, instruction in enumerate(s["instructions"])
                    ])

                    all_html += f"""
                    <div style="
                        background-color: #1a1a2e;
                        border: 1px solid #2a2a4a;
                        border-left: 4px solid {s['color']};
                        border-radius: 8px;
                        padding: 14px;
                        margin-bottom: 14px;
                        font-family: sans-serif;
                    ">
                        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
                            <div style="
                                background-color: {s['color']};
                                color: white;
                                font-size: 11px;
                                font-weight: 700;
                                padding: 3px 8px;
                                border-radius: 20px;
                            ">STEP {s['step']}</div>
                            <div style="font-size: 15px; font-weight: 700; color: #ffffff;">
                                {s['icon']} {s['title']}
                            </div>
                        </div>

                        <div style="
                            font-size: 11px;
                            color: {s['color']};
                            margin-bottom: 10px;
                            font-style: italic;
                        ">
                            {s['description']}
                        </div>

                        <div style="border-top: 1px solid #2a2a4a; padding-top: 10px;">
                            {instructions_html}
                        </div>
                    </div>
                    """

                all_html += """
                <div style="
                    text-align: center;
                    font-size: 11px;
                    color: #666677;
                    margin-top: 5px;
                    font-family: sans-serif;
                ">
                    💡 Tip — Use sidebar to navigate between all sections
                </div>
                """

                components.html(all_html, height=750, scrolling=True)

        with st.expander("Developer"):
            developers = [
                {
                    "name": "Tarun Tomar",
                    "role": "Project Lead & Developer",
                    "emoji": "👨‍💻",
                    "color": "#7c83fd",
                    "contributions": [
                        ("🐍", "Python Development"),
                        ("🌐", "Streamlit Dashboard UI"),
                        ("📊", "Plotly Charts & Maps"),
                        ("🗺️", "GeoJSON Map Integration"),
                        ("🏗️", "Project Architecture"),
                        ("🎓", "Data Science & Analysis"),
                        ("🗄️", "MySQL Database Design"),
                        ("🔍", "SQL Query Development"),
                        ("📥", "Data Fetching & Aggregation"),
                        ("⚙️", "Query Optimization"),
                        ("🔗", "DB & Python Integration"),
                        ("✅", "Data Validation & Testing"),
                    ]
                }
            ]

            all_html = ""

            for dev in developers:
                contributions_html = "".join([
                    f'<span style="background-color:#2a2a4a;border-radius:12px;'
                    f'padding:3px 8px;font-size:11px;color:#ccccdd;">'
                    f'{e} {c}</span>'
                    for e, c in dev["contributions"]
                ])

                all_html += f"""
                        <div style="
                            background-color: #1a1a2e;
                            border: 1px solid #2a2a4a;
                            border-top: 3px solid {dev['color']};
                            border-radius: 8px;
                            padding: 12px;
                            margin-bottom: 12px;
                            font-family: sans-serif;
                        ">
                            <div style="font-size:16px; font-weight:700; color:#ffffff;">
                                {dev['emoji']} {dev['name']}
                            </div>
                            <div style="font-size:11px; color:{dev['color']}; font-weight:600; margin:4px 0 10px 0;">
                                {dev['role']}
                            </div>
                            <div style="display:flex; flex-wrap:wrap; gap:6px;">
                                {contributions_html}
                            </div>
                        </div>
                        """

            all_html += """
                    <div style="text-align:center; font-size:11px; color:#666677; margin-top:5px; font-family:sans-serif;">
                        🤝 Built with collaboration & passion
                    </div>
                    """

            # renders real HTML, not markdown
            components.html(all_html, height=200, scrolling=False)

        st.text(
            "---------------------------------------------------------------------------------------------------------------------------------------------")

        st.subheader("Download Row Data: ")

        df = db.fetch_row_data()
        st.dataframe(df)


if select == "Overall India":
    if not os.path.exists("india_states.geojson"):
        url = "https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana.geojson"
        response = requests.get(url)
        with open("india_states.geojson", "w") as f:
            f.write(response.text)

    with open("india_states.geojson", "r") as f:
        india_geojson = json.load(f)

    india_df = db.fetch_all_states_summary()

    # Map DB names → GeoJSON names
    name_mapping = {
        "Jammu And Kashmir": "Jammu and Kashmir",
        "Daman And Diu": "Daman and Diu",
    }

    # Apply mapping before plotting
    india_df['State'] = india_df['State'].replace(name_mapping)

    india_df['hover_text'] = india_df.apply(
        lambda row: f"State: {row['State']}<br>"
                    f"Population: {row['Population']:,}<br>"
                    f"Literacy Rate: {row['Literacy_Rate']}%",
        axis=1
    )

    fig = px.choropleth_mapbox(
        india_df,
        geojson=india_geojson,
        locations='State',
        featureidkey="properties.NAME_1",
        color='Literacy_Rate',
        color_continuous_scale="Viridis",
        mapbox_style="carto-positron",
        zoom=3.5,
        center={"lat": 20.5937, "lon": 78.9629},
        opacity=0.6,
        hover_name='State',
        hover_data={
            'Population': ':,',
            'Literacy_Rate': True,
            'State': False
        },
        width=1200,
        height=700
    )

    fig.update_layout(
        coloraxis_colorbar=dict(title="Literacy Rate"),
        margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )

    st.subheader("Overall India - State wise Overview")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Note - ")
    st.write("In this dataset, We don't have data for some states like Jammu and Kashmir, Telangana, Delhi and others")
    st.write("In future, I'll add")

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

        # plot for state and show border ---------------------------------------------------------

        # Download GeoJSON --
        if not os.path.exists("india_states.geojson"):
            url = "https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana.geojson"
            response = requests.get(url)
            with open("india_states.geojson", "w") as f:
                f.write(response.text)

        with open("india_states.geojson", "r") as f:
            india_geojson = json.load(f)

        # Filter GeoJSON --
        filtered_geojson = {
            "type": "FeatureCollection",
            "features": [
                feature for feature in india_geojson["features"]
                if feature["properties"].get("NAME_1") == select_state
            ]
        }

        state_df = db.fetch_lat_long(select_state)

        fig = px.scatter_mapbox(
            state_df,
            lat="Latitude",
            lon="Longitude",
            zoom=5,
            size_max=25,
            mapbox_style="open-street-map",
            width=600,
            height=500,
            hover_name='District'
        )

        fig.update_layout(
            mapbox={
                "layers": [
                    {
                        "source": filtered_geojson,
                        "sourcetype": "geojson",
                        "type": "line",
                        "below": "traces",
                        "color": "red",
                        "line": {"width": 2},
                    }
                ]
            }
        )

        st.plotly_chart(fig, use_container_width=False)

        # ----------------------------------------------------------------------------------
        col1, col2 = st.columns(2)
        with col1:
            male = db.fetch_data('Male',select_state)
            female = db.fetch_data('Female',select_state)

            fig = go.Figure(
                go.Pie(
                    labels=["Male", "Female"],
                    values=[male,female],
                    hoverinfo="label+percent",
                    textinfo="value"
                ))
            st.subheader("Male vs Female - ")
            st.plotly_chart(fig)

        with col2:
            hindu = db.fetch_data("Hindus", select_state)
            muslims = db.fetch_data("Muslims", select_state)
            Christians = db.fetch_data("Christians",select_state)
            sikhs = db.fetch_data("Sikhs", select_state)
            Buddhists = db.fetch_data("Buddhists",select_state)
            jains = db.fetch_data("Jains",select_state)

            fig = go.Figure(
                go.Bar(
                    x=["Hindus", "Muslims", "Christians", "Sikhs", "Buddhists", "Jains"],
                    y=[hindu, muslims, Christians, sikhs, Buddhists, jains],
                    text=[hindu, muslims, Christians, sikhs, Buddhists, jains],
                    textposition='auto',
                    marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#DDA0DD']
                )
            )

            fig.update_layout(
                xaxis_title="Religion",
                yaxis_title="Population",
                showlegend=False
            )

            st.subheader("Religions - ")
            st.plotly_chart(fig)

        st.text(
            "---------------------------------------------------------------------------------------------------------------------------------------------")

        col1, col2 = st.columns(2)
        with (col1):
            male_literate = db.fetch_data("Male_Literate", select_state)
            female_literate = db.fetch_data("Female_Literate", select_state)

            fig = go.Figure(
                go.Pie(
                    labels=["Male Literate", "Female Literate"],
                    values=[male_literate, female_literate],
                    hoverinfo="label+percent",
                    textinfo="value"
                ))
            st.subheader("Male literate vs Female literate - ")
            st.plotly_chart(fig)

        with col2:
            male_workers = db.fetch_data("Male_Workers", select_state)
            female_workers = db.fetch_data("Female_Workers", select_state)

            fig = go.Figure(
                go.Pie(
                    labels=["Male Workers", "Female Workers"],
                    values=[male_workers, female_workers],
                    hoverinfo="label+percent",
                    textinfo="value"
                ))
            st.subheader("Male Workers vs Female Workers - ")
            st.plotly_chart(fig)

        st.text(
            "---------------------------------------------------------------------------------------------------------------------------------------------")

        col1, col2 = st.columns(2)
        with col1:
            rural_households = db.fetch_data("Rural_Households", select_state)
            urban_households = db.fetch_data("Urban_Households", select_state)

            fig = go.Figure(
                go.Pie(
                    labels=["Rural Households", "Urban Households"],
                    values=[rural_households, urban_households],
                    hoverinfo="label+percent",
                    textinfo="value"
                ))
            st.subheader("Rural Households vs Urban Households - ")
            st.plotly_chart(fig)

        with col2:
            Below_Primary_Education = db.fetch_data("Below_Primary_Education", select_state)
            Primary_Education = db.fetch_data("Primary_Education", select_state)
            Middle_Education = db.fetch_data("Middle_Education", select_state)
            Secondary_Education = db.fetch_data("Secondary_Education", select_state)
            Higher_Education = db.fetch_data("Higher_Education", select_state)
            Graduate_Education = db.fetch_data("Graduate_Education", select_state)
            Other_Education = db.fetch_data("Other_Education", select_state)

            fig = go.Figure(
                go.Bar(
                    x=["Below_Primary_Education", "Primary_Education", "Middle_Education", "Secondary_Education", "Higher_Education", "Graduate_Education","Other_Education"],
                    y=[Below_Primary_Education, Primary_Education, Middle_Education, Secondary_Education, Higher_Education, Graduate_Education, Other_Education],
                    text=[Below_Primary_Education, Primary_Education, Middle_Education, Secondary_Education, Higher_Education, Graduate_Education, Other_Education],
                    textposition='auto',
                    marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#DDA0DD']
                )
            )

            fig.update_layout(
                xaxis_title="Education Level",
                yaxis_title="Population",
                showlegend=False
            )

            st.subheader("Education Level vs Population - ")
            st.plotly_chart(fig)

        st.text(
            "---------------------------------------------------------------------------------------------------------------------------------------------")

        col1, col2 = st.columns(2)
        with col1:
            Age_Group_0_29 = db.fetch_data("Age_Group_0_29", select_state)
            Age_Group_30_49 = db.fetch_data("Age_Group_30_49", select_state)
            Age_Group_50_above = db.fetch_data("Age_Group_50", select_state)
            Age_not_stated_ = db.fetch_data("Age_not_stated", select_state)

            fig = go.Figure(
                go.Bar(
                    x=["Age_Group_0_29", "Age_Group_30_49", "Age_Group_50_above", "Age_not_stated"],
                    y=[Age_Group_0_29, Age_Group_30_49, Age_Group_50_above, Age_not_stated_],
                    text=[Age_Group_0_29, Age_Group_30_49, Age_Group_50_above, Age_not_stated_],
                    textposition='auto',
                    marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#DDA0DD']
                )
            )

            fig.update_layout(
                xaxis_title="Age Categories",
                yaxis_title="Population",
                showlegend=False
            )

            st.subheader("Age Categories - ")
            st.plotly_chart(fig)

        with col2:
            Households_with_Bicycle = db.fetch_data("Households_with_Bicycle", select_state)
            Households_with_Car_Jeep_Van = db.fetch_data("Households_with_Car_Jeep_Van", select_state)
            Households_with_Scooter_Motorcycle_Moped = db.fetch_data("Households_with_Scooter_Motorcycle_Moped", select_state)

            fig = go.Figure(
                go.Bar(
                    x=["Households_with_Bicycle", "Households_with_Car_Jeep_Van", "Households_with_Scooter_Motorcycle_Moped"],
                    y=[Households_with_Bicycle, Households_with_Car_Jeep_Van, Households_with_Scooter_Motorcycle_Moped],
                    text=[Households_with_Bicycle, Households_with_Car_Jeep_Van, Households_with_Scooter_Motorcycle_Moped],
                    textposition='auto',
                    marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#DDA0DD']
                )
            )

            fig.update_layout(
                xaxis_title="Vehicle Type",
                yaxis_title="Number of Households",
                showlegend=False
            )

            st.subheader("Vehicle Types - ")
            st.plotly_chart(fig)

        st.text(
            "---------------------------------------------------------------------------------------------------------------------------------------------")

        col1, col2 = st.columns(2)
        with col1:
            Household_size_1_person_Households = db.fetch_data("Household_size_1_person_Households", select_state)
            Household_size_2_persons_Households = db.fetch_data("Household_size_2_persons_Households", select_state)
            Household_size_3_persons_Households = db.fetch_data("Household_size_3_persons_Households", select_state)
            Household_size_3_to_5_persons_Households = db.fetch_data("Household_size_3_to_5_persons_Households",
                                                                     select_state)
            Household_size_6_8_persons_Households = db.fetch_data("Household_size_6_8_persons_Households", select_state)
            Household_size_9_persons_and_above_Households = db.fetch_data(
                "Household_size_9_persons_and_above_Households", select_state)

            fig = go.Figure(
                go.Bar(
                    x=["1 Person", "2 Persons", "3 Persons", "3 to 5 Persons", "6-8 Persons", "9 & Above"],
                    y=[
                        Household_size_1_person_Households,
                        Household_size_2_persons_Households,
                        Household_size_3_persons_Households,
                        Household_size_3_to_5_persons_Households,
                        Household_size_6_8_persons_Households,
                        Household_size_9_persons_and_above_Households
                    ],
                    text=[
                        Household_size_1_person_Households,
                        Household_size_2_persons_Households,
                        Household_size_3_persons_Households,
                        Household_size_3_to_5_persons_Households,
                        Household_size_6_8_persons_Households,
                        Household_size_9_persons_and_above_Households
                    ],
                    textposition='auto',
                    marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#DDA0DD']
                )
            )

            fig.update_layout(
                xaxis_title="Household Size",
                yaxis_title="Number of Households",
                showlegend=False
            )

            st.subheader("Household Size Distribution ")
            st.plotly_chart(fig)

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
            col1, col2 = st.columns(2)
            with col1:
                # st.text(select_state)
                ppl = db.fetch_dist_data("Population",select_dist)
                st.code('Population - {ppl}'.format(ppl=ppl))
            with col2:
                lit = db.fetch_dist_data("litracy_rate",select_dist)
                st.code('Litracy Rate - {lit}'.format(lit=lit))

            # ----------------------------------------------------------------------

            # DISTRICT MAP ----------------
            st.subheader(f" District Map — {select_state}")

            dist_map_df = db.fetch_dist_lat_long(select_state)

            # highlight selected district
            dist_map_df['is_selected'] = dist_map_df['District'].apply(
                lambda x: 'Selected' if x == select_dist else 'Other Districts'
            )
            dist_map_df['marker_size'] = dist_map_df['District'].apply(
                lambda x: 20 if x == select_dist else 8
            )
            dist_map_df['hover'] = dist_map_df.apply(
                lambda row: f"<b>{row['District']}</b><br>"
                            f"Population: {row['Population']:,}<br>"
                            f"Literacy Rate: {row['Literacy_Rate']}%",
                axis=1
            )

            fig_map = px.scatter_mapbox(
                dist_map_df,
                lat="Latitude",
                lon="Longitude",
                size="marker_size",
                color="is_selected",
                color_discrete_map={
                    'Selected': '#FF6B6B',  # red for selected district
                    'Other Districts': '#7c83fd'  # blue for others
                },
                hover_name="District",
                hover_data={
                    'Population': ':,',
                    'Literacy_Rate': True,
                    'marker_size': False,
                    'is_selected': False
                },
                zoom=5,
                size_max=20,
                mapbox_style="open-street-map",
                height=500,
            )

            # center map on selected district -------
            selected_row = dist_map_df[dist_map_df['District'] == select_dist].iloc[0]
            fig_map.update_layout(
                mapbox=dict(
                    center=dict(
                        lat=selected_row['Latitude'],
                        lon=selected_row['Longitude']
                    ),
                    zoom=6
                ),
                margin={"r": 0, "t": 0, "l": 0, "b": 0},
                legend=dict(
                    title="Districts",
                    bgcolor="#1a1a2e",
                    font=dict(color="white")
                )
            )

            st.plotly_chart(fig_map, use_container_width=True)
            st.divider()

            # ---------------------------------------

            col1, col2 = st.columns(2)
            with col1:
                male = db.fetch_dist_data('Male', select_dist)
                female = db.fetch_dist_data('Female', select_dist)

                fig = go.Figure(
                    go.Pie(
                        labels=["Male", "Female"],
                        values=[male, female],
                        hoverinfo="label+percent",
                        textinfo="value"
                    ))
                st.subheader("Male vs Female - ")
                st.plotly_chart(fig)

            with col2:
                hindu = db.fetch_dist_data("Hindus", select_dist)
                muslims = db.fetch_dist_data("Muslims", select_dist)
                Christians = db.fetch_dist_data("Christians", select_dist)
                sikhs = db.fetch_dist_data("Sikhs", select_dist)
                Buddhists = db.fetch_dist_data("Buddhists", select_dist)
                jains = db.fetch_dist_data("Jains", select_dist)

                fig = go.Figure(
                    go.Bar(
                        x=["Hindus", "Muslims", "Christians", "Sikhs", "Buddhists", "Jains"],
                        y=[hindu, muslims, Christians, sikhs, Buddhists, jains],
                        text=[hindu, muslims, Christians, sikhs, Buddhists, jains],
                        textposition='auto',
                        marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#DDA0DD']
                    )
                )

                fig.update_layout(
                    xaxis_title="Religion",
                    yaxis_title="Population",
                    showlegend=False
                )

                st.subheader("Religions - ")
                st.plotly_chart(fig)

            st.text(
                "---------------------------------------------------------------------------------------------------------------------------------------------")

            col1, col2 = st.columns(2)
            with (col1):
                male_literate = db.fetch_dist_data("Male_Literate", select_dist)
                female_literate = db.fetch_dist_data("Female_Literate", select_dist)

                fig = go.Figure(
                    go.Pie(
                        labels=["Male Literate", "Female Literate"],
                        values=[male_literate, female_literate],
                        hoverinfo="label+percent",
                        textinfo="value"
                    ))
                st.subheader("Male literate vs Female literate - ")
                st.plotly_chart(fig)

            with col2:
                male_workers = db.fetch_dist_data("Male_Workers", select_dist)
                female_workers = db.fetch_dist_data("Female_Workers", select_dist)

                fig = go.Figure(
                    go.Pie(
                        labels=["Male Workers", "Female Workers"],
                        values=[male_workers, female_workers],
                        hoverinfo="label+percent",
                        textinfo="value"
                    ))
                st.subheader("Male Workers vs Female Workers - ")
                st.plotly_chart(fig)

            st.text(
                "---------------------------------------------------------------------------------------------------------------------------------------------")

            col1, col2 = st.columns(2)
            with col1:
                rural_households = db.fetch_dist_data("Rural_Households", select_dist)
                urban_households = db.fetch_dist_data("Urban_Households", select_dist)

                fig = go.Figure(
                    go.Pie(
                        labels=["Rural Households", "Urban Households"],
                        values=[rural_households, urban_households],
                        hoverinfo="label+percent",
                        textinfo="value"
                    ))
                st.subheader("Rural Households vs Urban Households - ")
                st.plotly_chart(fig)

            with col2:
                Below_Primary_Education = db.fetch_dist_data("Below_Primary_Education", select_dist)
                Primary_Education = db.fetch_dist_data("Primary_Education", select_dist)
                Middle_Education = db.fetch_dist_data("Middle_Education", select_dist)
                Secondary_Education = db.fetch_dist_data("Secondary_Education", select_dist)
                Higher_Education = db.fetch_dist_data("Higher_Education", select_dist)
                Graduate_Education = db.fetch_dist_data("Graduate_Education", select_dist)
                Other_Education = db.fetch_dist_data("Other_Education", select_dist)

                fig = go.Figure(
                    go.Bar(
                        x=["Below_Primary_Education", "Primary_Education", "Middle_Education", "Secondary_Education",
                           "Higher_Education", "Graduate_Education", "Other_Education"],
                        y=[Below_Primary_Education, Primary_Education, Middle_Education, Secondary_Education,
                           Higher_Education, Graduate_Education, Other_Education],
                        text=[Below_Primary_Education, Primary_Education, Middle_Education, Secondary_Education,
                              Higher_Education, Graduate_Education, Other_Education],
                        textposition='auto',
                        marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#DDA0DD']
                    )
                )

                fig.update_layout(
                    xaxis_title="Education Level",
                    yaxis_title="Population",
                    showlegend=False
                )

                st.subheader("Education Level vs Population - ")
                st.plotly_chart(fig)

            st.text(
                "---------------------------------------------------------------------------------------------------------------------------------------------")

            col1, col2 = st.columns(2)
            with col1:
                Age_Group_0_29 = db.fetch_dist_data("Age_Group_0_29", select_dist)
                Age_Group_30_49 = db.fetch_dist_data("Age_Group_30_49", select_dist)
                Age_Group_50_above = db.fetch_dist_data("Age_Group_50", select_dist)
                Age_not_stated_ = db.fetch_dist_data("Age_not_stated", select_dist)

                fig = go.Figure(
                    go.Bar(
                        x=["Age_Group_0_29", "Age_Group_30_49", "Age_Group_50_above", "Age_not_stated"],
                        y=[Age_Group_0_29, Age_Group_30_49, Age_Group_50_above, Age_not_stated_],
                        text=[Age_Group_0_29, Age_Group_30_49, Age_Group_50_above, Age_not_stated_],
                        textposition='auto',
                        marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#DDA0DD']
                    )
                )

                fig.update_layout(
                    xaxis_title="Age Categories",
                    yaxis_title="Population",
                    showlegend=False
                )

                st.subheader("Age Categories - ")
                st.plotly_chart(fig)

            with col2:
                Households_with_Bicycle = db.fetch_dist_data("Households_with_Bicycle", select_dist)
                Households_with_Car_Jeep_Van = db.fetch_dist_data("Households_with_Car_Jeep_Van", select_dist)
                Households_with_Scooter_Motorcycle_Moped = db.fetch_dist_data("Households_with_Scooter_Motorcycle_Moped",select_dist)

                fig = go.Figure(
                    go.Bar(
                        x=["Households_with_Bicycle", "Households_with_Car_Jeep_Van",
                           "Households_with_Scooter_Motorcycle_Moped"],
                        y=[Households_with_Bicycle, Households_with_Car_Jeep_Van,
                           Households_with_Scooter_Motorcycle_Moped],
                        text=[Households_with_Bicycle, Households_with_Car_Jeep_Van,
                              Households_with_Scooter_Motorcycle_Moped],
                        textposition='auto',
                        marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#DDA0DD']
                    )
                )

                fig.update_layout(
                    xaxis_title="Vehicle Type",
                    yaxis_title="Number of Households",
                    showlegend=False
                )

                st.subheader("Vehicle Types - ")
                st.plotly_chart(fig)

            st.text(
                "---------------------------------------------------------------------------------------------------------------------------------------------")

            col1, col2 = st.columns(2)
            with col1:
                Household_size_1_person_Households = db.fetch_dist_data("Household_size_1_person_Households", select_dist)
                Household_size_2_persons_Households = db.fetch_dist_data("Household_size_2_persons_Households", select_dist)
                Household_size_3_persons_Households = db.fetch_dist_data("Household_size_3_persons_Households", select_dist)
                Household_size_3_to_5_persons_Households = db.fetch_dist_data("Household_size_3_to_5_persons_Households",
                                                                         select_dist)
                Household_size_6_8_persons_Households = db.fetch_dist_data("Household_size_6_8_persons_Households",
                                                                      select_dist)
                Household_size_9_persons_and_above_Households = db.fetch_dist_data("Household_size_9_persons_and_above_Households", select_dist)

                fig = go.Figure(
                    go.Bar(
                        x=["1 Person", "2 Persons", "3 Persons", "3 to 5 Persons", "6-8 Persons", "9 & Above"],
                        y=[
                            Household_size_1_person_Households,
                            Household_size_2_persons_Households,
                            Household_size_3_persons_Households,
                            Household_size_3_to_5_persons_Households,
                            Household_size_6_8_persons_Households,
                            Household_size_9_persons_and_above_Households
                        ],
                        text=[
                            Household_size_1_person_Households,
                            Household_size_2_persons_Households,
                            Household_size_3_persons_Households,
                            Household_size_3_to_5_persons_Households,
                            Household_size_6_8_persons_Households,
                            Household_size_9_persons_and_above_Households
                        ],
                        textposition='auto',
                        marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#DDA0DD']
                    )
                )

                fig.update_layout(
                    xaxis_title="Household Size",
                    yaxis_title="Number of Households",
                    showlegend=False
                )

                st.subheader("Household Size Distribution ")
                st.plotly_chart(fig)


