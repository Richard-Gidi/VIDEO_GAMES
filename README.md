# Video Game Sales Forecasting

![image](https://github.com/user-attachments/assets/65c0fda2-5ead-431a-b7fd-234fa46a35cb)

## 1. Business Problem
Amdari has been contacted by a local video-game resale company that needs to optimize its supply chain for video game inventory. Accurate demand forecasting is crucial to avoid overstocking and stockouts. An overestimation of demand leads to bloated inventory and increased costs, while underestimating demand means valuable customers may not receive the products they want. The Data Science Team's goal is to forecast monthly sales for the next four months to aid in decision-making and improve the company’s competitive edge.

## 2. Project Overview
The project involves the following key components:

### Exploratory Data Analysis (EDA)
- **Identify overall sales trends:** Analyze historical sales data to understand growth patterns over time.
- **Detect seasonality and cyclical patterns:** Investigate recurring sales patterns and fluctuations throughout the year.
- **Analyze sales by category and platform:** Assess how different game categories and platforms contribute to overall sales.
- **Assess the impact of holidays and promotions:** Evaluate how holidays and marketing promotions affect sales figures.
- **Determine the influence of weekdays on sales:** Analyze if sales vary by the day of the week.

### Predictive Analytics
- **Utilize ARIMA and SES (Single Exponential Smoothing) and Holt-Winters models for forecasting.**
- **Evaluate model accuracy and select the best-fitting model.**
- **Generate four-month sales forecasts.**

## 3. Steps to Solve the Problem
1. **Load and clean the dataset:** Prepare the data for analysis by handling missing values and ensuring proper formatting.
2. **Perform EDA:** Visualize trends, seasonality, and the impact of categories/platforms on sales.
3. **Apply time series decomposition:** Extract trend, seasonality, and error components from the sales data.
4. **Build ARIMA and ETS models:** Tune their parameters based on ACF and PACF plots to improve accuracy.
5. **Compare model performance:** Use error metrics such as RMSE (Root Mean Square Error) and MAPE (Mean Absolute Percentage Error) to assess model effectiveness.
6. **Select the best model and generate four-month forecasts.**

## 4. Understanding the Dataset
The dataset contains the following columns:
- **Category:** The genre of the video game (e.g., Action, Adventure).
- **Month:** The date (first of each month).
- **Monthly Sales:** Total sales in that month.
- **Year:** Extracted year from the date.
- **DayOfWeek:** The weekday of the first day of the month.
- **Platform:** The gaming platform (e.g., Xbox, Nintendo, PC, PlayStation).
- **Holiday:** Binary indicator (1 if a holiday is in that month, 0 otherwise).
- **Promotion:** Binary indicator (1 if there was a promotion, 0 otherwise).

## 5. Building the Model

### Forecast Results

| Forecast Type         | Month       | Predicted Sales |
|-----------------------|-------------|------------------|
| **ARIMA**             | 2023-09-01  | 116317.28        |
|                       | 2023-10-01  | 116682.89        |
|                       | 2023-11-01  | 113380.78        |
|                       | 2023-12-01  | 115998.19        |
| **Single Exponential Smoothing (SES)** | 2023-09-01  | 114150.36        |
|                       | 2023-10-01  | 114150.36        |
|                       | 2023-11-01  | 114150.36        |
|                       | 2023-12-01  | 114150.36        |
| **Holt-Winters**      | 2023-09-01  | 94168.68         |
|                       | 2023-10-01  | 87588.09         |
|                       | 2023-11-01  | 101041.51        |
|                       | 2023-12-01  | 105454.79        |

### Comparing the Models
| Month       | Actual  | ARIMA         | Holt-Winters  | SES          |
|-------------|---------|---------------|----------------|--------------|
| 2023-09-01  | 143373  | 116317.28     | 94168.68       | 114150.36    |
| 2023-10-01  | 126410  | 116682.89     | 87588.09       | 114150.36    |
| 2023-11-01  | 91200   | 113380.78     | 101041.51      | 114150.36    |
| 2023-12-01  | 159721  | 115998.19     | 105454.79      | 114150.36    |

### Conclusion
The Holt-Winters Model was selected as the best forecasting method due to its ability to capture seasonal trends effectively. This forecasting will help synchronize supply with demand, minimizing stockouts and overstock situations.

## 6. Final Forecast for the Next Four Months

| Month       | Predicted Sales |
|-------------|------------------|
| 2024-01-01  | 94168.68         |
| 2024-02-01  | 87588.09         |
| 2024-03-01  | 101041.51        |
| 2024-04-01  | 105454.79        |

## 7. Next Steps
- Fine-tune models further using hyperparameter tuning.
- Explore advanced techniques such as Prophet or LSTMs for improved forecasting accuracy.
- Continuously monitor model performance and update with new data to maintain accuracy.

## 8. References
- For detailed methodology and theoretical background on ARIMA and Holt-Winters models, refer to relevant literature and statistical textbooks.
