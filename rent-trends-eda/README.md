# Rent Trends EDA - Post-COVID Housing Analysis

## Overview
This project explores rent inflation across U.S cities from 2015 to 2024 using Zillow Observed Rent Index (ZORI) data.   The goal is to identify affordability trends, city-level disparities, and broader economic shifts post-COVID.

---

## Objectives
- Clean and transform time-series rent data (wide -> long)
- Filter and analyze rent trends for key U.S. cities
- Calculate and visualize percent rent growth (2015 -> 2024)
- Begin laying groundwork for future affordability analysis

---

## Dataset
- **Source**: [Zillow Research](https://www.zillow.com/research/data/)
- **File used**: Zori by City (CSV format)
- **Timeframe**: Jan 2015 - Early 2024
- **Structure**: Monthly rent index values for hundred of U.S. cities

---

## Tools
- **Language**: Python
- **Libraries**: pandas, seaborn, matplotlib
- **Platform**: Jupyter Notebook
- **Version Control**: Git + Github

---

## Visualizations 

### Rent Trends Over Time (2015-2024)
Shows rent changes in Washington, D.C., New York, and Chicago using Zillow's ZORI data.

![Rent Trends Line Chart](visuals/rent_trends_line_chart.png)

---

### Percent Rent Growth by City (2015-2024)
This bar chart highlights relative rent inflation across the three cities.

![Percent Growth Bar Chart](visuals/rent_growth_percent_bar.png)

---

## Key Findings 
- Chicago showed the **highest percent rent growth** (~49%) despite lower base rent
- NYC and D.C. saw **stronger dollar increases**, but smaller relative change
- All three cities had a **notable dip in mid 2020**, consistent with COVID impact
- NYC saw the sharpest rebound starting in 2022

--- 

## Deliverables
- A cleaned, well-document notebook
- Visual insights and a short summary
- *(Planned)*: A dashboard for interactivity

---

## Status
Mostly Completed  
**Planned**: Add dashboard and heatmap of regional or correlation data

---

## Author
**Brett Shaia**  
Bachelor of Science in Computer Science  
Master of Science in Data Analytics (In Progress)  
[GitHub Profile](https://github.com/Bshaia) • [Email](mailto:brettshaia@gmail.com)