# 📊 Statistical Analysis of Financial Assets with Python

This project presents a complete and professional pipeline for conducting **exploratory statistical analysis of financial assets** using Python and Jupyter Notebook. It is designed to be fully reusable for any stock or ETF listed on Yahoo Finance.

Examples in this project use Brazilian stocks such as `BBDC3.SA`, `ITUB4.SA`, and `BBAS3.SA`, but the same methodology applies to any asset with historical data.

---

## 📌 Objectives

* 📈 Download historical prices from Yahoo Finance
* 🔍 Perform descriptive statistical analysis of daily returns
* 🧮 Calculate risk measures such as standard deviation and Value at Risk (VaR)
* 📉 Plot distributions and return behavior
* 🧭 Visualize cumulative capital growth over time
* 📄 Export complete analysis to a polished PDF report

---

## 🧰 Technologies Used

* Python 3
* [Jupyter Notebook](https://jupyter.org/)
* [yfinance](https://pypi.org/project/yfinance/)
* pandas, numpy, matplotlib, seaborn, scipy.stats

---

## 🚀 How to Run

1. Clone the repository or download the `.ipynb` file.
2. Install the required libraries:

```bash
pip install yfinance pandas matplotlib seaborn scipy
```

3. Run the notebook:

```bash
jupyter notebook statistical_analysis.ipynb
```

4. To export to PDF (optional):

```bash
jupyter nbconvert --to pdf --output report_statistical_analysis statistical_analysis.ipynb
```

> ⚠️ You may need a working LaTeX distribution (like TeX Live) to generate the PDF.

---

## 📊 Analyses Performed

* **Daily Returns**: Calculation using percentage change of adjusted close prices.
* **Descriptive Statistics**: Mean, standard deviation, min, max, percentiles.
* **Skewness and Kurtosis**: To evaluate distribution symmetry and tail behavior.
* **Histogram and Boxplots**: To visualize return distributions.
* **Cumulative Capital Growth**: Growth of R\$ 1.00 over time.
* **Volatility (Annualized)**: Estimate of yearly risk based on daily returns.
* **Value at Risk (VaR)**: Estimate of daily potential loss at a given confidence level (e.g., 95%).

---

## 🖼️ Sample Visualization

Example: Growth of R\$ 1.00 invested in each asset:

![Cumulative Growth](img/cumulative_growth.png)

> Replace `img/cumulative_growth.png` with the actual path to your saved graph, if applicable.

---

## 🧩 Extensibility

This notebook is structured to support:

* Adding more assets dynamically;
* Customizing time periods (e.g., 5Y, 10Y);
* Including new metrics (e.g., Sharpe Ratio, beta);
* Integrating with dashboards (e.g., Streamlit, Tableau);
* Exporting data to databases or APIs.

---

## 👨‍💻 Target Audience

* Data Scientists and Analysts
* Finance and Economics students
* Quantitative Researchers
* Anyone interested in financial risk analysis with Python

The **notebook format** makes it easy to follow for users familiar with Jupyter, even if they are not experienced with GitHub.

---

## 🔍 View Full Analysis

- 📄 [Download the Full PDF Report](./reports/statistical_analysis.pdf)
- 📓 [Open the Jupyter Notebook](./statistical_analysis.ipynb)

> All visualizations and statistical insights are reproducible and editable directly from the notebook.

