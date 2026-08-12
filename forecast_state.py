import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

print("Loading data...")

df = pd.read_csv('pi-dataset-july-2026-release.csv')

# ============================================================
# 1. FILTER FOR A SPECIFIC STATE
# ============================================================

state_name = 'Virginia'  # change this to the desired state name

state_df = df[df['State Name'] == state_name].copy()
state_df['date'] = pd.to_datetime(state_df['Reporting Period'].astype(str) + '01', format='%Y%m%d')

state_data = state_df.groupby('date')['Total Medicaid Enrollment'].sum().reset_index()
state_data.columns = ['ds', 'y']
state_data = state_data.sort_values('ds')

print(f"{state_name}: {len(state_data)} months of data")

# ============================================================
# 2. PROPHET MODEL
# ============================================================

model = Prophet()
model.fit(state_data)

# ============================================================
# 3. FORECAST 10 YEARS
# ============================================================

future = model.make_future_dataframe(periods=120, freq='ME')
forecast = model.predict(future)

print("Forecast complete.")

# ============================================================
# 4. PLOT
# ============================================================

fig = model.plot(forecast)
plt.title(f'{state_name} Medicaid Enrollment Forecast')
plt.xlabel('Year')
plt.ylabel('Enrollment')
plt.show()

# ============================================================
# 5. SAVE
# ============================================================

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(f'{state_name}_forecast.csv', index=False)
print(f"Forecast saved to {state_name}_forecast.csv")