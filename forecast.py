# Medicaid Enrollment and Expenditure Forecasting
# Objective: Forecast annual Medicaid enrollments and expenditures
# nationwide and state-specific for the next 10 years.

import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

print("Loading data...")

# ============================================================
# 1. LOAD DATA
# ============================================================

df = pd.read_csv('pi-dataset-july-2026-release.csv')

# ============================================================
# 2. AGGREGATE TO NATIONAL LEVEL
# ============================================================

enrollment_col = 'Total Medicaid Enrollment'

df['date'] = pd.to_datetime(df['Reporting Period'].astype(str) + '01', format='%Y%m%d')

# Group by date and sum all states
national = df.groupby('date')[enrollment_col].sum().reset_index()
national.columns = ['ds', 'y']

# Sort by date
national = national.sort_values('ds')

print(f"Data loaded: {len(national)} months")
print(national.head())

# ============================================================
# 3. PROPHET MODEL
# ============================================================

model = Prophet()
model.fit(national)

# ============================================================
# 4. FORECAST 10 YEARS
#    Use 'ME' (Month End) instead of 'M'
# ============================================================

future = model.make_future_dataframe(periods=120, freq='ME')
forecast = model.predict(future)

print("Forecast complete.")

# ============================================================
# 5. PLOT
# ============================================================

fig = model.plot(forecast)
plt.title('Medicaid National Enrollment Forecast')
plt.xlabel('Year')
plt.ylabel('Enrollment')
plt.show()

# ============================================================
# 6. SAVE FORECAST
# ============================================================

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv('national_forecast.csv', index=False)
print("Forecast saved to national_forecast.csv")