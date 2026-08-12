# Medicaid Enrollment and Expenditure Forecasting Project

## Overview
This project forecasts annual Medicaid enrollments and expenditures for the next ten years, both nationwide and at the state level. The analysis uses historical Medicaid data from CMS and KFF, combined with Facebook Prophet for time series forecasting.

## Data Sources
- **Enrollment Data:** CMS pi-dataset-july-2026-release.csv
- **Expenditure Data:** CMS-64 New Adult Group Expenditures Dataset
- **Historical Context:** EMRTS blog post "Reflections on Medicaid Enrollment for the Next Decade"

## Repository Structure
├── forecast.py # National enrollment forecast
├── forecast_state.py # State-level enrollment forecast
├── expenditure_forecast.py # National expenditure forecast
├── expenditure_forecast_state.py # State-level expenditure forecast
├── pi-dataset-july-2026-release.csv # Enrollment data
├── medicaid-cms-64-*.csv # Expenditure data
├── national_forecast.csv # National enrollment forecast output
├── national_expenditure_forecast.csv # National expenditure forecast output
├── Virginia_forecast.csv # Virginia enrollment forecast output
├── Virginia_expenditure_forecast.csv # Virginia expenditure forecast output
└── README.md # This file

## Setup

### Prerequisites
- Python 3.x
- pip

### Clone the repository
```bash
git clone https://github.com/RossJiao/medicaid-forecasting-project.git
cd medicaid-forecasting-project

## Install dependencies
pip install pandas matplotlib prophet

Run
National Enrollment Forecast
python3 forecast.py
State Enrollment Forecast (change state name in code)
python3 forecast_state.py
National Expenditure Forecast
python3 expenditure_forecast.py
State Expenditure Forecast (change state name in code)
python3 expenditure_forecast_state.py
Sample Output
National Enrollment Forecast
https://Figure_1.png

National Expenditure Forecast
https://Figure_2.png

Files Generated
File	Description
national_forecast.csv	National enrollment forecast (2026-2036)
national_expenditure_forecast.csv	National expenditure forecast (2026-2036)
Virginia_forecast.csv	Virginia enrollment forecast
Virginia_expenditure_forecast.csv	Virginia expenditure forecast
Model
The project uses Facebook Prophet, a forecasting tool designed for business time series data. It handles:

Trend changes

Seasonality

Holiday effects

Missing data

Technology Stack
Python 3

Facebook Prophet

Pandas (data processing)

Matplotlib (visualization)

Author
Ross Dingyan Jiao

Links
GitHub: https://github.com/RossJiao/medicaid-forecasting-project
