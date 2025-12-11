from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

def plot_brightness(df: pd.DataFrame, png_path: Path) -> None:
    """
    Построение и сохранение графика средней яркости изображений.
    """
    x_values = range(len(df))
    y_values = df["avg_brightness"].tolist()

    plt.figure(figsize=(8, 4))
    plt.plot(x_values, y_values, marker="o")
    plt.title("Средняя яркость изображений")
    plt.xlabel("Номер изображения")
    plt.ylabel("Яркость (0–255)")
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(png_path)
    plt.close()