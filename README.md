Predictive Forecasting of Care Load & Placement Demand
Overview

This project develops a predictive analytics framework for forecasting future care load and placement demand under the Unaccompanied Alien Children (UAC) Program of the U.S. Department of Health and Human Services (HHS).

The objective is to enable proactive healthcare and shelter resource planning using time-series forecasting and machine learning models.

Problem Statement

Operational decisions within the UAC Program are often reactive due to lack of short-term forecasting capability. Sudden intake surges may lead to:

Shelter overcrowding

Staff workload imbalance

Increased length of stay

This project introduces predictive intelligence for early capacity risk detection.

Dataset

Source: HHS UAC Program Daily Operational Dataset

Key variables include:

Children in HHS Care

Transfers from CBP Custody

Children Discharged from HHS Care

Daily Intake Volume

Methodology
Time-Series Analysis

Trend & seasonality decomposition

Missing value handling

Temporal indexing

Feature Engineering

Lag Features (t-1, t-7, t-14)

Rolling averages

Net Pressure Indicator

Forecasting Models

ARIMA Model

Random Forest Regressor

Key Performance Indicators (KPIs)

Forecast Accuracy

Net Pressure Indicator

Capacity Risk Detection

Surge Lead Time

Forecast Stability

Dashboard

Interactive Streamlit dashboard provides:

Future care load forecast

Discharge demand prediction

Capacity risk visualization

Model comparison

🔗 Live Dashboard: (Paste your Streamlit link here)

Research Contribution

This project transforms historical reporting into predictive decision intelligence supporting proactive healthcare planning and improved child-welfare outcomes.

Tools & Technologies

Python

Pandas

Scikit-learn

Statsmodels

Streamlit

Google Colab

Author

Ahatsham Khan
Healthcare Analytics Domain

⭐ Result

The system enables early-warning forecasting to support data-driven government decision-making and operational preparedness.
