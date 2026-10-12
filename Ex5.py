def word_cont(string_line):

    if not isinstance(string_line, (list, tuple)):
        print("на вход должен быть подан список строк.")
        return None

    if len(string_line) == 0:
        print("список запросов пуст.")
        return None

    words_count={}
    total = 0

    for query in string_line:
        if not isinstance(query, str):
            print(f"элемент {query!r} не является строкой")
            return None

        words = query.split()
        n = len(words)

        words_count[n] = words_count.get(n, 0) + 1
        total += 1

    if total == 0:
        print("не найдено ни одного непустого запроса")
        return None

    words_count_in_percent = {}
    for n in sorted(words_count.keys()):
        percent = words_count[n] / total * 100
        words_count_in_percent[n] = percent

    return words_count_in_percent


def print_distribution(words_count_in_percent):
    if words_count_in_percent is None:
        return

    for n in sorted(words_count_in_percent.keys()):
        percent = words_count_in_percent[n]

        if n % 10 == 1 and n % 100 != 11:
            word_form = "слово"
        elif n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
            word_form = "слова"
        else:
            word_form = "слов"

        if percent == int(percent):
            percent_str = f"{int(percent)}%"
        else:
            percent_str = f"{percent:.1f}%"

        print(f"{n}:{word_form}: {percent_str}")

if __name__ == "__main__":
    search_queries = [
        "watch new movies",
        "coffee near me",
        "how to find the determinant",
        "python",
        "data science jobs in UK",
        "courses for data science",
        "taxi",
        "google",
        "yandex",
        "bing",
        "foreign exchange rates USD/BYN",
        "Netflix movies watch online free",
        "Statistics courses online from top universities",
    ]

    words_count_in_percent = word_cont(search_queries)
    print_distribution(words_count_in_percent)