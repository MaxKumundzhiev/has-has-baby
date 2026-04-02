def task_1():
    """
    Задача 1 — базовые метрики (простая)

    ожидается:
    {"accuracy": 0.8, "precision": 0.8, "recall": 0.8, "f1": 0.8}

    TP (true positive)
    TN (true negative)
    FP (false positive)
    FN (false negative)

    accuracy = ...
    """

    y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

    def evaluate(y_true: list[int], y_pred: list[int]) -> dict:
        """
        На примере классификации котов и собак (кот=0, собака=1)

        TP 1→1 — на фото собака, предсказала собаку    ✓
        TN 0→0 — на фото кошка,  предсказала кошку     ✓
        FP 0→1 — на фото кошка,  предсказала собаку    ✗ ложная тревога
        FN 1→0 — на фото собака, предсказала кошку     ✗ пропустила

        Precision — из всех кого назвала собакой, сколько реально собаки?
            высокий precision = редко путает кошку с собакой
            формула: TP / (TP + FP)

        Recall — из всех реальных собак, сколько нашла?
            высокий recall = редко пропускает собак
            формула: TP / (TP + FN)

        если высокий precision, низкий recall —
            модель осторожная: говорит "собака" только когда уверена,
            но много собак пропускает (называет кошками)

        если высокий recall, низкий precision —
            модель агрессивная: находит почти всех собак,
            но часто путает — называет кошек собаками

        F1 — баланс между ними: 2 * P * R / (P + R)
        """

        if not y_true:
            return {"accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0}

        tp = tn = fp = fn = 0
        for true, pred in zip(y_true, y_pred):
            if true == 1 and pred == 1:
                tp += 1
            if true == 0 and pred == 0:
                tn += 1
            if true == 0 and pred == 1:
                fp += 1
            if true == 1 and pred == 0:
                fn += 1

        accuracy = (tp + tn) / len(y_pred)
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = (
            2 * precision * recall / (precision + recall)
            if (precision + recall) > 0
            else 0.0
        )
        return {
            "accuracy": round(accuracy, 3),
            "precision": round(precision, 3),
            "recall": round(recall, 3),
            "f1": round(f1, 3),
        }

    res = evaluate(y_true, y_pred)
    print(res)


task_1()
