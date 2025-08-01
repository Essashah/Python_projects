import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import datetime

st.set_page_config(layout="wide")
st.title("📈 US GDP Prediction for the Next 10 Years")

# Load and prepare data
gdp_data = pd.read_csv('A191RL1Q225SBEA.csv')
gdp_data.rename(columns={'observation_date': 'Date', 'A191RL1Q225SBEA': 'GDP'}, inplace=True)
gdp_data['Date'] = pd.to_datetime(gdp_data['Date'])
gdp_data = gdp_data.sort_values('Date')

# Create lag feature (GDP from previous quarter)
gdp_data['GDP_lag1'] = gdp_data['GDP'].shift(1)
gdp_data = gdp_data.dropna()

# Model training
X = gdp_data[['GDP_lag1']]
y = gdp_data['GDP']
model = RandomForestRegressor()
model.fit(X, y)

# Start with the last known GDP
future_dates = []
future_gdp = []

last_known_gdp = gdp_data['GDP'].iloc[-1]
last_known_date = gdp_data['Date'].iloc[-1]

for i in range(40):  # 40 quarters = 10 years
    next_date = last_known_date + pd.DateOffset(months=3)
    predicted_gdp = model.predict([[last_known_gdp]])[0]
    
    future_dates.append(next_date)
    future_gdp.append(predicted_gdp)

    # Update for next iteration
    last_known_gdp = predicted_gdp
    last_known_date = next_date

# Create a DataFrame with predictions
future_df = pd.DataFrame({
    'Date': future_dates,
    'Predicted_GDP': future_gdp
})

# Combine historical and future GDP
full_df = pd.concat([
    gdp_data[['Date', 'GDP']].rename(columns={'GDP': 'Actual_GDP'}),
    future_df.rename(columns={'Predicted_GDP': 'Actual_GDP'})
])

# Plot
st.subheader("📊 GDP Forecast: Historical + Next 10 Years")
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(full_df['Date'], full_df['Actual_GDP'], label='GDP')
ax.axvline(pd.to_datetime('2025-01-01'), color='red', linestyle='--', label='2025 Start')
ax.set_xlabel("Date")
ax.set_ylabel("GDP")
ax.set_title("US GDP Forecast (Quarterly)")
ax.legend()
st.pyplot(fig)

# Display predictions
st.subheader("🗓️ Next 10 Years of Quarterly GDP Predictions")
st.dataframe(future_df.set_index("Date").style.format("{:.2f}"))
