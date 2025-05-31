import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def describe_price_data(symbol: str, df: pd.DataFrame) -> None:
    print("📊 Descriptive Statistics:")
    stats = df.describe()
    print(stats)

    print("\n🔎 Additional Metrics:")
    skew = df["adjusted_close"].skew()
    kurt = df["adjusted_close"].kurt()

    if isinstance(skew, pd.Series):
        for idx in skew.index:
            print(f"Skewness ({idx}): {skew[idx]:.4f}")
            print(f"Kurtosis ({idx}): {kurt[idx]:.4f}")
    else:
        print(f"Skewness (assimetria): {skew:.4f}")
        print(f"Kurtosis (curtose): {kurt:.4f}")

    plt.figure(figsize=(12, 4))
    plt.plot(df.index, df["adjusted_close"], label="Adjusted Close", color="navy")
    plt.title(f"{symbol} - Adjusted Close Price (2015 - Hoje)")
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
