import joblib
import pandas as pd
from flask import Flask, request, jsonify, render_template
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# Load ARIMA model
arima_model = joblib.load('models/arima_model.pkl')

# Function to create forecast
def generate_forecast(start_date, months):
    try:
        forecast = arima_model.forecast(steps=months)
        predictions = [round(float(x), 2) for x in forecast]

        df_predictions = pd.DataFrame({
            'Month': [(start_date + timedelta(days=30 * i)).strftime('%Y-%m') for i in range(months)],
            'Predicted Sales ($)': predictions
        })
        return df_predictions, None
    except Exception as e:
        return None, str(e)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d')
    months = int(request.form.get('months'))

    predictions, error = generate_forecast(start_date, months)
    if error:
        return jsonify({'error': error}), 400

    return predictions.to_json(orient='records')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
