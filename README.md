# 📊 Statistical Analysis of Financial Assets with Python

This project provides a complete and professional **exploratory data analysis (EDA)** framework to evaluate the behavior and risk of financial assets using Python and Jupyter Notebook.

While the examples use Brazilian stocks like `BBDC3.SA`, `ITUB4.SA`, and `BBAS3.SA`, the approach is fully adaptable to **any stock or ETF** available on [Yahoo Finance](https://finance.yahoo.com/).

It focuses on **statistical and visual exploration of daily returns**, making it a valuable tool for:

- 📈 Data scientists exploring financial datasets
- 📉 Analysts assessing asset risk and return profiles
- 📄 Anyone interested in reproducible and insightful financial reporting

---

## 📌 Key Features

- 🗂️ Download historical prices from Yahoo Finance
- 📊 Perform descriptive statistical analysis of daily returns
- 📉 Calculate risk metrics like standard deviation and Value at Risk (VaR)
- 📐 Visualize distributions with histograms and boxplots
- 📈 Analyze cumulative capital growth over time
- 📄 Export complete analysis to a professional PDF report
- 📓 Fully documented and reusable Jupyter Notebook

---

## 🔗 Access the Project

- 📓 **[Open Notebook](notebooks/statistical_analysis.ipynb)**  
- 📄 **[Download PDF Report](reports/statistical_analysis_report.pdf)**

---

## 🧰 Technologies Used

- Python 3
- [Jupyter Notebook](https://jupyter.org/)
- [yfinance](https://pypi.org/project/yfinance/)
- pandas, numpy, matplotlib, seaborn, scipy

---

## 🚀 How to Run

1. Clone the repository or download the `.ipynb` file.
2. Install the required libraries:

```bash
   pip install -r requirements.txt
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

* **Daily Returns** — percent change of adjusted close prices
* **Descriptive Statistics** — mean, std, percentiles, min, max
* **Skewness and Kurtosis** — tail behavior and distribution symmetry
* **Histograms and Boxplots** — for return visualization
* **Cumulative Capital Growth** — evolution of R$1.00 invested
* **Annualized Volatility** — yearly risk based on daily fluctuations
* **Value at Risk (VaR)** — daily potential loss at 95% confidence

---
