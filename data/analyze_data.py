import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm

def describe_price_data(symbol: str, df: pd.DataFrame) -> None:
    print("📊 Descriptive Statistics:")
    stats = df.describe()
    print(stats)

    print("\n🔎 Additional Metrics:")
    skew = df["adjusted_close"].skew()
    kurt = df["adjusted_close"].kurt()
    volatility = calculate_daily_volatility(df)
    print(f"📈 Daily Volatility: {volatility:.4%}")

    if isinstance(skew, pd.Series):
        for idx in skew.index:
            print(f"Skewness ({idx}): {skew[idx]:.4f}")
            print(f"Kurtosis ({idx}): {kurt[idx]:.4f}")
    else:
        print(f"Skewness (assimetria): {skew:.4f}")
        print(f"Kurtosis (curtose): {kurt:.4f}")

    plt.figure(figsize=(12, 4))
    plt.plot(df.index, df["adjusted_close"], label="Adjusted Close", color="navy")
    plt.title(f"{symbol} - Adjusted Close Price (2015 - Today)")
    plt.xlabel("Data")
    plt.ylabel("Preço (R$)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 1.5))
    adjusted_close = df["adjusted_close"]
    if isinstance(adjusted_close, pd.DataFrame):
        adjusted_close = adjusted_close.iloc[:, 0]
    sns.boxplot(x=adjusted_close, color="orange")
    plt.title(f"Boxplot - Preço Ajustado ({symbol})")
    plt.tight_layout()
    plt.show()

def calculate_daily_volatility(df: pd.DataFrame) -> float:
    daily_returns = df["adjusted_close"].pct_change().dropna()
    return float(daily_returns.std())

def analyze_daily_returns(symbol: str, df: pd.DataFrame) -> None:
    daily_returns = df["adjusted_close"].pct_change().dropna()

    print("\n📈 Daily Returns Statistics:")
    print(daily_returns.describe())

    mean = daily_returns.mean().item()
    std = daily_returns.std().item()
    skew = daily_returns.skew().item()
    kurt = daily_returns.kurt().item()

    print(f"\nMédia: {mean:.4%}")
    print(f"Desvio Padrão: {std:.4%}")
    print(f"Assimetria (Skewness): {skew:.4f}")
    print(f"Curtose (Kurtosis): {kurt:.4f}")

    x = np.linspace(daily_returns.min(), daily_returns.max(), 100)
    plt.plot(x, norm.pdf(x, mean, std), 'r--', label='Distribuição Normal')

    plt.title(f"Distibuição dos Retornos Diários - {symbol}")
    plt.xlabel("Retorno Diário")
    plt.ylabel("Densidade")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


    plt.figure(figsize=(8, 1.5))
    sns.boxplot(x=daily_returns.squeeze(), color="lightgreen")
    plt.title(f"Boxplot  dos Retornos Diários - {symbol}")
    plt.tight_layout()
    plt.show()
