## India Census Analysis 2011

A data-driven interactive web application built to explore and visualize India’s Census 2011 dataset using modern data analytics tools.

---

### Project Overview

This project transforms raw census data into interactive insights using dashboards, maps, and visualizations.

It allows users to explore:
- Population distribution
- Literacy rates
- Religion demographics
- Household patterns
- District-level analytics

---

### Objective
To make India’s Census 2011 data easy to understand and explore through:
- Interactive visualizations
- State & district-level drill-down
- Real-time data querying using SQL


### Dataset Information

**Source**: Office of the Registrar General & Census Commissioner, India

**Dataset Summary**
- *Rows*: 502 (District-level data)
- *Columns*: 75
- *States/UTs Covered*: 31
- *Missing Values*: None

**Data Categories**
- *Geography*: State, District, Latitude, Longitude
- *Demographics*: Population, Male, Female, Sex Ratio, Literacy Rate
- *Education*: Literate, Primary, Secondary, Graduate, etc.
- *Workers*: Total, Male, Female, Agricultural Workers
- *Religion*: Hindus, Muslims, Christians, Sikhs, Buddhists, Jains
- *Households*: Rural, Urban, Ownership, Size Distribution
- *Assets*: Internet, Computer, TV, Mobile, Electricity
- *Vehicles*: Bicycle, Car, Scooter
- *Age Groups*: 0–29, 30–49, 50+
- *Income Groups*: ₹45,000 to ₹5,45,000+


---

### Key Features

**Interactive India Map**
- Choropleth map of all states
- Color-coded by literacy rate
- Hover insights (Population, Literacy Rate)

**Demographics Analysis**
- Population distribution
- Male vs Female comparison

**Literacy Insights**
- State & district-level literacy analysis

**Religion Distribution**
- Comparative bar charts across regions

**Household Analytics**
- Household size distribution
- Asset ownership patterns

**District Drill-Down**
- Explore each district in detail

**State Map View**
- Scatter map showing districts of selected state

**Dataset Explorer**
- Browse, filter & download raw data

---

### Tech Stack

**Python** - Core backend logic & data processing

**MySQL** - Database storing census data

**Streamlit** - Web app framework

**Plotly** - Interactive visualizations

**Pandas** - Data manipulation & analysis

**GeoJSON** - Map boundaries for visualization

**MySQL Connector** - Database connectivity


### How to Use

**Overall India**
- View India-wide literacy & population map
- Hover on states for insights

**States & UTs**
- Select any state
- Explore:
	Population stats, Literacy rate, Religion distribution, Household data

**District Analysis**
- Select state → district
- Deep dive into district-level insights

---

### Future Improvements

	•	Add latest Census data (2021 when available)
	•	Integrate live API data
	•	Add predictive analytics (ML models)
	•	Deploy on cloud with scalable database
