# VIDEO_GAMES

![image](https://github.com/user-attachments/assets/65c0fda2-5ead-431a-b7fd-234fa46a35cb)


1. The Business Problem
Amdari has recently been contacted by a local video-game resale company. Many
businesses have to be on point when it comes to ordering supplies to meet the demand of its
customers. An overestimation of demand leads to bloated inventory and high costs.
Underestimating demand means many valued customers won't get the products they want.
In order to help plan out the supply with demand for the company's video games, the Data
Science Team has been tasked with forecasting monthly sales data in order to synchronize
supply with demand, and aid in decision making that will help build a competitive
infrastructure and measure the growing company’s performance.
Your team is being asked to provide a forecast for the next 4 months of sales. Create and
submit a very detailed report.

The project involves:

1. Exploratory Data Analysis (EDA):

Identifying overall sales trends.
Detecting seasonality and cyclical patterns.
Analyzing sales by category and platform.
Assessing the impact of holidays and promotions.
Determining the influence of weekdays on sales.

2. Predictive Analytics:

Using ARIMA and SES,  (Single Exponential Smoothing) and Holt-Winters models for forecasting.
Evaluating model accuracy and selecting the best-fitting model.
Generating four-month sales forecasts.

3. Steps to Solve the Problem
Load and clean the dataset.
Perform EDA (Visualizing trends, seasonality, category/platform impact, etc.).
Apply time series decomposition to extract trend, seasonality, and error components.
Build ARIMA and ETS models, tuning their parameters based on ACF and PACF plots.
Compare model performance using error metrics (e.g., RMSE, MAPE).
Select the best model and generate four-month forecasts.

4.Understanding the Dataset
The dataset contains the following columns:

Category: The genre of the video game.
Month: The date (first of each month).
Monthly Sales: Total sales in that month.
Year: Extracted year from the date.
DayOfWeek: The weekday of the first day of the month.
Platform: The gaming platform (e.g., Xbox, Nintendo, PC, PlayStation).
Holiday: Binary indicator (1 if a holiday is in that month, 0 otherwise).
Promotion: Binary indicator (1 if there was a promotion, 0 otherwise).

5.Building the model
ARIMA MODEL FORCASTED
2023-09-01    116317.282605
2023-10-01    116682.890976
2023-11-01    113380.775304
2023-12-01    115998.185396
Freq: MS, Name: predicted_mean, dtype: float64
Single Exponential Smoothing (SES) Forecasted
2023-09-01    114150.35762
2023-10-01    114150.35762
2023-11-01    114150.35762
2023-12-01    114150.35762
Freq: MS, dtype: float64

Holt-Winter Model forecasted
2023-09-01     94168.683589
2023-10-01     87588.086270
2023-11-01    101041.512820
2023-12-01    105454.792863
Freq: MS, dtype: float64

Comparing the models
          Actual          ARIMA   Holt-Winters           SES
Month                                                         
2023-09-01  143373  116317.282605   94168.683589  114150.35762
2023-10-01  126410  116682.890976   87588.086270  114150.35762
2023-11-01   91200  113380.775304  101041.512820  114150.35762
2023-12-01  159721  115998.185396  105454.792863  114150.35762

Holt-Winters performs best as it captures seasonality better.
ARIMA provides a stable forecast but does not adjust well to sales fluctuations.
SES produces a constant forecast, making it unsuitable for dynamic sales data.

Final forecast for the four months
Holt-Winter model is used to predict the next four months because it performed best
Forecasted Sales
2024-01-01      94168.683589
2024-02-01      87588.086270
2024-03-01     101041.512820
2024-04-01     105454.792863

Conclusion
Holt-Winters Model was the best choice for forecasting due to clear seasonal trends.
Forecasting helps synchronize supply with demand, avoiding stockouts and overstock situations.
Next Steps: Fine-tune models further using hyperparameter tuning or more advanced techniques like Prophet or LSTMs.
