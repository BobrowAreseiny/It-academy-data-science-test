from datetime import datetime, date

def date_diff(date1, date2):
    if isinstance(date1, str):
        try:
            date1 = datetime.strptime(date1, "%Y-%m-%d")
        except ValueError:
            print(f"не удалось разобрать дату {date1!r}. Ожидается формат YYYY-MM-DD.")
            return None
    if isinstance(date2, str):
        try:
            date2 = datetime.strptime(date2, "%Y-%m-%d")
        except ValueError:
            print(f"Ошибка: не удалось разобрать дату {date2!r}. Ожидается формат YYYY-MM-DD.")
            return None

    if not isinstance(date1, (datetime, date)) or not isinstance(date2, (datetime, date)):
        print("оба аргумента должны быть datetime или строкой в формате YYYY-MM-DD.")
        return None

    date_diff = date2 - date1
    diff_days = date_diff.days

    if diff_days < 0:
        print(f"Рвзница отрицательная. Абсолютное значение разницы:  {abs(date_diff)} lytq")

    return diff_days

if __name__ == '__main__':
    print(date_diff("2024-01-01", "2024-01-10"))
    print(date_diff("2024-01-10", "2024-01-01"))
    print(date_diff(datetime(2023, 5, 1), datetime(2023, 5, 31)))
    print(date_diff("2024-13-01", "2024-01-01"))  # ошибка формата
    print(date_diff(123, "2024-01-01"))  # ошибка типа
