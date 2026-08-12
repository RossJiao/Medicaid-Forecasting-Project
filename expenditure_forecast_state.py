import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

print("Loading expenditure data...")

df = pd.read_csv('medicaid-cms-64-new-adult-group-expenditures-dataset-02172026.csv')

# ============================================================
# 1. FILTER FOR STATE
# ============================================================

state_name = 'Virginia'  # change this to the desired state name

state_df = df[df['State'] == state_name].copy()

# Clean and convert
expenditure_col = 'Total Computable All Medical Assistance Expenditures'
state_df[expenditure_col] = state_df[expenditure_col].astype(str).str.replace(',', '').str.replace('$', '')
state_df[expenditure_col] = pd.to_numeric(state_df[expenditure_col], errors='coerce')

state_df['date'] = pd.to_datetime(state_df['Quarter End Date'])

state_data = state_df.groupby('date')[expenditure_col].sum().reset_index()
state_data.columns = ['ds', 'y']
state_data = state_data.sort_values('ds')

print(f"{state_name}: {len(state_data)} quarters")

# ============================================================
# 2. PROPHET
# ============================================================

model = Prophet()
model.fit(state_data)

future = model.make_future_dataframe(periods=40, freq='QE')
forecast = model.predict(future)

# ============================================================
# 3. PLOT
# ============================================================

fig = model.plot(forecast)
plt.title(f'{state_name} Medicaid Expenditure Forecast')
plt.xlabel('Year')
plt.ylabel('Expenditure ($)')
plt.show()