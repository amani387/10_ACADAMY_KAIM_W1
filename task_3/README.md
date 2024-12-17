# Task 3: Correlation Between News Sentiment and Stock Movements

## **Objective**
Analyze the relationship between daily news sentiment and stock price movements to uncover potential correlations and dependencies.

---

## **Steps**

### **1. Data Preparation**
- **News Data**:
  - Extracted news headlines and their corresponding dates.
  - Performed sentiment analysis using `TextBlob` to assign polarity scores ranging from `-1` (negative sentiment) to `+1` (positive sentiment).
- **Stock Data**:
  - Processed stock price data from `AAPL_historical_data.csv`.
  - Calculated **daily returns** as the percentage change in adjusted closing prices.
- **Alignment**:
  - Normalized and merged news sentiment scores with stock data using `date` as the common key.

---

### **2. Sentiment Analysis**
- Sentiment scores were computed using `TextBlob`:
  - **Positive Sentiment**: Score > 0.
  - **Neutral Sentiment**: Score = 0.
  - **Negative Sentiment**: Score < 0.

---

### **3. Correlation Analysis**
- Calculated the **Pearson correlation coefficient** to quantify the strength of the relationship between:
  - Sentiment Scores.
  - Daily Stock Returns.

---

### **4. Visualizations**
Generated key plots to support the analysis:
1. **Scatter Plot**:
   - Visualized the relationship between sentiment scores and daily stock returns.
2. **Histogram of Sentiment Scores**:
   - Displayed the distribution of sentiment scores.
3. **Histogram of Daily Returns**:
   - Highlighted the spread and variability of stock returns.
4. **Boxplot of Returns by Sentiment Category**:
   - Showed the variation in stock returns for Positive, Neutral, and Negative sentiment categories.
5. **Trend Line**:
   - Plotted 7-day rolling averages for sentiment scores and daily returns.
6. **Density Plot**:
   - Emphasized areas of high concentration between sentiment and returns.

---

## **Results**
- **Pearson Correlation Coefficient**: `0.03`
  - Indicates a **very weak positive correlation** between sentiment scores and stock price movements.
- **Scatter Plot Insights**:
  - No significant linear trend between sentiment and stock returns.
  - Most data points were clustered near zero for both variables.

---

## **Key Challenges**
1. **Data Alignment**:
   - Mixed date formats required careful normalization to merge datasets.
2. **Weak Correlation**:
   - Sentiment data had limited variability, reducing its explanatory power.
3. **Market Complexity**:
   - Stock prices are influenced by numerous factors beyond sentiment, such as macroeconomic indicators, earnings reports, and speculation.

---

## **How to Run the Code**

### **Prerequisites**
1. Install required Python libraries:
   ```bash
   pip install pandas matplotlib seaborn textblob
