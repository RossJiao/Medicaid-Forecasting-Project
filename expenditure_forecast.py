import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

print("Loading expenditure data...")

# ============================================================
# 1. LOAD EXPENDITURE DATA
# ============================================================

df = pd.read_csv('medicaid-cms-64-new-adult-group-expenditures-dataset-02172026.csv')

print(f"Columns: {df.columns.tolist()}")
print(f"Rows: {len(df)}")

# ============================================================
# 2. CLEAN AND AGGREGATE DATA
# ============================================================

# Convert Quarter End Date to datetime
df['date'] = pd.to_datetime(df['Quarter End Date'])

# Use Total Computable All Medical Assistance Expenditures
expenditure_col = 'Total Computable All Medical Assistance Expenditures'

# Remove dollar signs and commas, convert to float
df[expenditure_col] = df[expenditure_col].astype(str).str.replace(',', '').str.replace('$', '')
df[expenditure_col] = pd.to_numeric(df[expenditure_col], errors='coerce')

# ============================================================
# 3. NATIONAL AGGREGATE
# ============================================================

# Group by date and sum all states
national = df.groupby('date')[expenditure_col].sum().reset_index()
national.columns = ['ds', 'y']
national = national.sort_values('ds')

print(f"National data: {len(national)} quarters")
print(national.head())

# ============================================================
# 4. PROPHET MODEL
# ============================================================

model = Prophet()
model.fit(national)

# ============================================================
# 5. FORECAST 10 YEARS (40 quarters)
# ============================================================

future = model.make_future_dataframe(periods=40, freq='QE')
forecast = model.predict(future)

# ============================================================
# 6. PLOT
# ============================================================

fig = model.plot(forecast)
plt.title('Medicaid National Expenditure Forecast')
plt.xlabel('Year')
plt.ylabel('Expenditure ($)')
plt.show()

# ============================================================
# 7. SAVE
# ============================================================

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv('national_expenditure_forecast.csv', index=False)
print("Forecast saved to national_expenditure_forecast.csv")