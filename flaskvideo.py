from flask import Flask, render_template, request
import joblib
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go

app = Flask(__name__)

# Load models
models = {
    'ARIMA': joblib.load('models/arima_model.pkl'),
    'SES': joblib.load('models/ses_model.pkl'),
    'Holt-Winters': joblib.load('models/holt_winters_model.pkl'),
}

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
    return fig.to_html(full_html=False)

@app.route('/')
def index():
    return render_template('index.html', models=list(models.keys()))

@app.route('/predict', methods=['POST'])
def predict():
    model_choice = request.form['model']
    model = models[model_choice]

    start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
    months = int(request.form['months'])

    try:
        forecast = model.forecast(steps=months)
        predictions = [round(float(x), 2) for x in forecast]

        df_predictions = pd.DataFrame({
            'Month': [(start_date + timedelta(days=30 * i)).strftime('%Y-%m') for i in range(months)],
            'Predicted Sales ($)': predictions
        })

        return render_template('index.html', tables=[df_predictions.to_html(classes='data', header=True, index=False)])
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
