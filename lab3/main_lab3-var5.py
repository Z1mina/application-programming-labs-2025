from pathlib import Path

from functions import parse_args, load_image, invert_colors, show_images, save_image


def main() -> None:
    """
    Главная функция
    """
    args = parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    # Загрузка изображения
    img = load_image(input_path)

    # Вывод размера
    print(f"Размер изображения (height, width, channels): {img.shape}")

    # Инверсия цветов
    inverted_img = invert_colors(img)

    # Показ
    show_images(img, inverted_img)

    # Сохранение
    save_image(output_path, inverted_img)

    print(f"Результат сохранён в: {output_path}")


if __name__ == "__main__":
    main()