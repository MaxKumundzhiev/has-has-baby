"""
шаг 1: найти все уникальные классы → {0, 1, 2}

шаг 2: для каждого класса посчитать precision
    класс 0:
        TP = сколько раз true=0 и pred=0
        FP = сколько раз true≠0 и pred=0
        precision_0 = TP / (TP + FP)

    класс 1: то же самое
    класс 2: то же самое

шаг 3: macro = среднее по всем классам
    (precision_0 + precision_1 + precision_2) / 3
"""


def precision_for_class(y_true: list[int], y_pred: list[int], cls: int) -> float:
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == cls and p == cls)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t != cls and p == cls)
    return tp / (tp + fp) if (tp + fp) > 0 else 0.0


def macro_precision(y_true: list[int], y_pred: list[int]) -> float:
    classes = set(y_true)
    precisions = [precision_for_class(y_true, y_pred, c) for c in classes]
    return round(sum(precisions) / len(classes), 4)


if __name__ == "__main__":
    y_true = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
    y_pred = [0, 2, 1, 0, 1, 2, 1, 1, 0, 0]
    print(macro_precision(y_true, y_pred))
