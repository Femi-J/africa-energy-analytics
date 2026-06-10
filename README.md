# Africa-energy-analytics
**Turning Africa's Energy Data into Decisions**
This repo hosts a growing portfolio of data analysis projects exploring solar potential, electricity access, grid performance, and sustainability across Africa.

[![GitHub](https://img.shields.io/badge/GitHub-Femi--J-181717?logo=github)](https://github.com/Femi-J)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Olufemi_Akintunde-0077B5?logo=linkedin)](https://www.linkedin.com/in/olufemi-akintunde-0540a144)

## 🗂️ Projects
### 1. West Africa Electricity Access Analysis
**Tools:** Python · Pandas · Matplotlib · Seaborn  
**Data:** World Bank Electricity Access Indicators (2020–2023)  
**Key Finding:** Rwanda improved electricity access by 18.7% in 3 years, the fastest in the region. South Africa is the only country going backwards (-0.77% avg YoY).

📓 [Notebook](notebooks/Africa_electricity_access_analysis.ipynb) | 
📊 [Charts](reports/)
---

### 2. West Africa Solar Irradiance Analysis
**Tools:** Python · NASA POWER API · Pandas · Matplotlib  
**Data:** NASA POWER satellite data (2014–2025) — 18 cities, 16 countries  
**Key Finding:** Kano receives 30% more solar irradiance than Lagos. 
The Harmattan effect enhances GHI in coastal zones while suppressing 
it in desert zones, a non-uniform regional effect.

📓 [Notebook](notebooks/west_africa_solar_analysis.ipynb) |
📊 [Charts](reports/)

---
### 3. Solar Irradiance Time Series Analysis
**Tools:** Python · Pandas · Matplotlib · SciPy  
**Data:** NASA POWER (2014–2025) across 5 cities  
**Key Finding:** Lagos GHI stable over 11 years (no trend). Dakar and Lagos show near-zero correlation (0.020), completely independent solar patterns despite both being coastal cities.

📓 [Notebook](notebooks/west_africa_solar_timeseries.ipynb) |
📊 [Charts](reports/)

---
### 4. Geospatial Energy Maps
**Tools:** Python · Folium · GeoPandas  
**Data:** NASA POWER + World Bank  
**Deliverable:** 3 interactive HTML maps combining solar GHI and electricity access data across West Africa.

📓 [Notebook](notebooks/west_africa_geospatial_analysis.ipynb) |
🗺️ [Interactive Map](reports/west_africa_solar_energy_map.html)

---
### 5. MySQL Energy Database
**Tools:** Python · MySQL 8.0 · mysql-connector-python  
**Data:** 2,574 solar records · 16 countries · 3 tables  
**Deliverable:** Fully queryable relational database with 5 analytical SQL queries answering real energy questions.

📓 [Notebook](notebooks/energy_database_mysql.ipynb)

---
### 6. Power BI Energy Dashboard
**Tools:** Power BI Desktop · DAX  
**Data:** NASA POWER + World Bank  
**Deliverable:** Interactive 4-panel dashboard with map, bar chart, line chart, KPI cards and slicers.

📊 [Dashboard File](PowerBI/West%20Africa%20solar%20dashboard.pbix)

---
### 7. Plotly Interactive Charts & Dash App
**Tools:** Python · Plotly Express · Plotly Dash  
**Data:** NASA POWER (2014–2025)  
**Deliverable:** 5 interactive charts including animated monthly GHI chart and a live Dash web application.

📓 [Notebook](notebooks/west_africa_plotly_charts.ipynb) |
📊 [Interactive Charts](reports/)

---
## 🔬 Research Paper

**Seasonal Solar Irradiance Variability and Harmattan Effects Across West African Climate Zones: Evidence from NASA POWER Satallite Data across 18 cities**
Preprint submitted to AfricArXiv via ScienceOpen (May 2026).  

Key finding: The Harmattan effect on solar irradiance is **non-uniform** across West Africa, enhancing GHI in Coastal Humid (+0.574 kWh/m²/day) and Savanna (+0.771 kWh/m²/day) zones while suppressing it in Desert/Arid zones (-1.059 kWh/m²/day).

🔒 [Research Repo](https://github.com/Femi-J/west-africa-solar-research)

## 🛠️ Tools & Technologies

| Category | Tools |
|---|---|
| Languages | Python 3.12 |
| Data Analysis | Pandas · NumPy · SciPy |
| Visualisation | Matplotlib · Seaborn · Plotly · Folium |
| Dashboards | Power BI Desktop · Plotly Dash |
| Database | MySQL 8.0 · mysql-connector-python |
| Geospatial | GeoPandas · Folium |
| Statistics | Mann-Whitney U · Kruskal-Wallis · Mann-Kendall |
| Environment | Jupyter Notebook · Anaconda · VS Code |
| Version Control | Git · GitHub |
---
## Projects
*(Projects will be listed here as they are completed)*

## 📊 Data Sources

- **NASA POWER API** — Solar irradiance data (free, no key required)
  https://power.larc.nasa.gov
- **World Bank** — Electricity access indicators (EG.ELC.ACCS.ZS)
  https://data.worldbank.org/indicator/EG.ELC.ACCS.ZS

---

## 👤 About

**Olufemi Akintunde**
Energy & Sustainability Data Analyst | Renewable Energy Expert

- 🎓 MSc Renewable Energy — Victoria University of Wellington, NZ
- 🎓 MSc Industrial & Production Engineering — University of Ibadan
- 🎓 BEng Mechanical Engineering — LAUTECH, Ogbomosho, Nigeria
- 📜 Data Analytics Certificate — ALX Africa
- 🔬 ORCID: [0009-0006-1174-9289](https://orcid.org/0009-0006-1174-9289)
- 📍 Abuja, Nigeria
- 💼 Open to consulting engagements and collaborations
