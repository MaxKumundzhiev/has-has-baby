"""
# несбалансированный датасет: 90% нулей
y_true = [0]*90 + [1]*10
y_pred = [0]*100  # модель всегда предсказывает 0

На интервью это формулируют так: "accuracy не информативна на несбалансированных данных — смотри на F1 или precision/recall по минорному классу".
"""

from collections import Counter


def evaluate_with_baseline(y_true, y_pred) -> dict:
    # посчитай метрики + baseline accuracy
    # объясни почему модель бесполезна несмотря на высокую accuracy
    metrics: dict = {
        "accuracy": 0.0,
        "precision": 0.0,
        "recall": 0.0,
        "f1": 0.0,
    }

    if not y_pred:
        return metrics

    tp = tn = fp = fn = 0.0
    for true, pred in zip(y_true, y_pred):
        if true == 1 and pred == 1:
            tp += 1
        elif true == 0 and pred == 0:
            tn += 1
        elif true == 0 and pred == 1:
            fp += 1
        elif true == 1 and pred == 0:
            fn += 1

    metrics["accuracy"] = (tp + tn) / len(y_pred)
    metrics["precision"] = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    metrics["recall"] = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    metrics["f1"] = (
        2
        * metrics["precision"]
        * metrics["recall"]
        / (metrics["precision"] + metrics["recall"])
        if (metrics["precision"] + metrics["recall"]) > 0
        else 0.0
    )

    # baseline — модель всегда предсказывает самый частый класс
    majority = Counter(y_true).most_common(1)[0][0]
    baseline_pred = [majority] * len(y_true)
    tp_b = sum(1 for t, p in zip(y_true, baseline_pred) if t == 1 and p == 1)
    tn_b = sum(1 for t, p in zip(y_true, baseline_pred) if t == 0 and p == 0)
    metrics["baseline_accuracy"] = (tp_b + tn_b) / len(y_true)

    return metrics


if __name__ == "__main__":
    y_true = [0] * 90 + [1] * 10
    y_pred = [0] * 100  # модель всегда предсказывает 0

    print(evaluate_with_baseline(y_true, y_pred))
