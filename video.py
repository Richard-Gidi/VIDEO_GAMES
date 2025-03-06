import joblib
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Load models
models = {
    'ARIMA': joblib.load('models/arima_model.pkl'),
    'SES': joblib.load('models/ses_model.pkl'),
    "Holt-Winters": joblib.load('models/holt_winters_model.pkl'),
    'Prophet': joblib.load('models/prophet_model.pkl')  # Ensure this is the trained model
}

# Set page configuration
st.set_page_config(
    page_title="Video Game Sales Forecast",
    layout="wide"
)

# Sidebar menu
menu = st.sidebar.selectbox("Menu", ["Prediction", "Visualization"])

# Function to create the forecast plot
def create_forecast_plot(predictions, start_date):
    dates = [start_date + timedelta(days=30 * i) for i in range(len(predictions))]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates,
        y=predictions,
        mode='lines+markers',
        name='Forecast',
        line=dict(color='#1f77b4', width=2),
        marker=dict(size=8)
    ))
    fig.update_layout(
        title='Sales Forecast',
        xaxis_title='Date',
        yaxis_title='Predicted Sales ($)',
        template='plotly_white',
        hovermode='x unified'
    )
    return fig

# Prediction menu
if menu == "Prediction":
    st.title("🧠 Video Game Sales Prediction")

    model_choice = st.selectbox("Select Model", list(models.keys()))
    model = models[model_choice]

    start_date = st.date_input("Select Start Date", datetime.today())
    months = st.number_input("Number of months to forecast", min_value=1, max_value=12, value=3, step=1)

    if st.button("Generate Forecast"):
        try:
            if model_choice == 'Prophet':
                future = model.make_future_dataframe(periods=months * 30, freq='D')
                forecast = model.predict(future)
                predictions = forecast.tail(months)['yhat'].tolist()  # Monthly aggregation
            else:
                forecast = model.forecast(steps=months)
                predictions = [round(float(x), 2) for x in forecast]

            df_predictions = pd.DataFrame({
                'Month': [(start_date + timedelta(days=30 * i)).strftime('%Y-%m') for i in range(months)],
                'Predicted Sales ($)': predictions
            })
            st.dataframe(df_predictions, use_container_width=True)

            csv = df_predictions.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Forecast", data=csv, file_name='sales_forecast.csv', mime='text/csv')
        except Exception as e:
            st.error(f"Error generating forecast: {str(e)}")

# Visualization menu
elif menu == "Visualization":
    st.title("📈 Sales Forecast Visualization")

    uploaded_file = st.file_uploader("Upload Forecast CSV", type=['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        if 'Month' in df.columns and 'Predicted Sales ($)' in df.columns:
            df['Month'] = pd.to_datetime(df['Month'])
            fig = create_forecast_plot(df['Predicted Sales ($)'], df['Month'].iloc[0])
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Invalid file format. Ensure it contains 'Month' and 'Predicted Sales ($)' columns.")
