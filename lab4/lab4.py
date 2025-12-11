from pathlib import Path

from data_frame import(load_paths_dataframe, add_brightness_column, sort_by_brightness, filter_by_brightness, save_dataframe)
from visualization import  plot_brightness

def main() -> None:
    """
    Главная функция
    """
    # путь к CSV из ЛР2
    annotation_csv = Path("annotation.csv")

    # загрузка данных и формирование DataFrame
    df_paths = load_paths_dataframe(annotation_csv)

    # добавление колонки по варианту (средняя яркость)
    df_with_brightness = add_brightness_column(df_paths)

    # сортировка по новой колонке
    df_sorted = sort_by_brightness(df_with_brightness)

    # фильтрация
    mean_brightness = float(df_sorted["avg_brightness"].mean())
    df_filtered = filter_by_brightness(df_sorted, mean_brightness)

    # построение графика по отсортированным данным
    plot_brightness(
        df_sorted,
        png_path=Path("brightness_plot.png"),
    )

    # сохранение итогового dataframe и графика
    save_dataframe(df_filtered, csv_path=Path("result.csv"))


if __name__ == "__main__":
    main()