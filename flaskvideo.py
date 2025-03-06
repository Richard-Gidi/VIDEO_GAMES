from flask import Flask, render_template, request, send_file
import joblib
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
from io import BytesIO

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

        csv = df_predictions.to_csv(index=False)
        buffer = BytesIO()
        buffer.write(csv.encode('utf-8'))
        buffer.seek(0)

        return send_file(buffer, mimetype='text/csv', as_attachment=True, download_name='sales_forecast.csv')
    except Exception as e:
        return str(e)

@app.route('/visualize', methods=['POST'])
def visualize():
    file = request.files['file']
    if file:
        df = pd.read_csv(file)
        if 'Month' in df.columns and 'Predicted Sales ($)' in df.columns:
            df['Month'] = pd.to_datetime(df['Month'])
            plot_html = create_forecast_plot(df['Predicted Sales ($)'], df['Month'].iloc[0])
            return render_template('visualize.html', plot=plot_html)
        else:
            return 'Invalid file format. Ensure it contains "Month" and "Predicted Sales ($)" columns.'
    return 'No file uploaded.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
