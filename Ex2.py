def euclidean_norm(vec):
    total = 0.0
    for x in vec:
        total += x * x
    return total ** 0.5

def normalize(vec):
    norm = euclidean_norm(vec)
    result = []
    for x in vec:
        result.append(x / norm)
    return result

def dot_product(vec1, vec2):
    total = 0.0
    for a, b in zip(vec1, vec2):
        total += a * b
    return total

def is_number(value):

    if isinstance(value, bool):
        return False

    try:
        value + 0
        value * 1
        value / 1
    except (TypeError, ValueError, ZeroDivisionError):
        return False

    return True

def cosine_distance(vec1, vec2):

    if not isinstance(vec1, (list, tuple)) or not isinstance(vec2, (list, tuple)):
        print("оба вектора должны быть списками чисел.")
        return None

    if len(vec1) == 0 or len(vec2) == 0:
        print("вектор пуст")
        return None

    if len(vec1) != len(vec2):
        print(f"размерности векторов не совпадают ")
        return None

    for i, value in enumerate(vec1):
        if not is_number(value):
            print(f"элемент vec1{i}] = {value!r} не является числом.")
            return None
    for i, value in enumerate(vec2):
        if not is_number(value):
            print(f"элемент vec2[{i}] = {value!r} не является числом.")
            return None

    norm1 = euclidean_norm(vec1)
    norm2 = euclidean_norm(vec2)

    if norm1 == 0.0:
        print("первый вектор нулевой. решение невозможно.")
        return None
    if norm2 == 0.0:
        print("второй вектор нулевой. решение невозможно.")
        return None

    unit1 = normalize(vec1)
    unit2 = normalize(vec2)

    dot = dot_product(unit1, unit2)

    len1 = euclidean_norm(unit1)
    len2 = euclidean_norm(unit2)
    cosine_coeff = dot / (len1 * len2)

    cosine_distance_value = 1.0 - cosine_coeff

    print(f"нормализованный вектор 1: {unit1}")
    print(f"нормализованный вектор 2: {unit2}")
    print(f"скалярное произведение нормализованных векторов: {dot}")
    print(f"косинусный коэффициент: {cosine_coeff}")
    print(f"косинусное расстояние: {cosine_distance_value}")
    return cosine_distance_value


# ------------------- Примеры использования -------------------

# Корректный случай
cosine_distance([1, 2, 3], [4, 5, 6])

# Разные размерности
cosine_distance([1, 2, 3], [4, 5])

# Пустой вектор
cosine_distance([], [1, 2])

# Нулевой вектор
cosine_distance([0, 0, 0], [1, 2, 3])

# Не числа
cosine_distance([1, "a", 3], [4, 5, 6])

# Не список
cosine_distance("abc", [1, 2, 3])
