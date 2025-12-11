from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image


def load_paths_dataframe(csv_path: Path) -> pd.DataFrame:
    """
    Загрузка DataFrame из CSV-файла аннотации ЛР2.
    """
    df = pd.read_csv(csv_path)
    df = df.rename(columns={"absolute_path": "absolute_path", "relative_path": "relative_path"})
    return df


def calculate_brightness(image_path: str) -> float:
    """
    Вычисление средней яркости изображения по всем каналам.
    """
    image = Image.open(image_path).convert("RGB")
    array = np.array(image)
    brightness = float(array.mean())
    return brightness


def add_brightness_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Добавление в DataFrame колонку avg_brightness с яркостью.
    """
    df["avg_brightness"] = df["absolute_path"].apply(
        calculate_brightness
    )
    return df


def sort_by_brightness(df: pd.DataFrame) -> pd.DataFrame:
    """
    Сортировка строки DataFrame по средней яркости.
    """
    sorted_df = df.sort_values(by="avg_brightness", ascending=True)
    return sorted_df


def filter_by_brightness(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """
    Фильтрация DataFrame по яркости: оставляет ярче порога.
    """
    filtered_df = df[df["avg_brightness"] > threshold]
    return filtered_df


def save_dataframe(df: pd.DataFrame, csv_path: Path) -> None:
    """
    Сохранение DataFrame в CSV файл.
    """
    df.to_csv(csv_path, index=False)
