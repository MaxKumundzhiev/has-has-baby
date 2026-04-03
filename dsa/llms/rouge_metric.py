"""
Дан список пар (reference, prediction).
Посчитай ROUGE-1 F1 — не только recall, но и precision, и их гармоническое среднее.

precision = доля слов из prediction которые есть в reference
recall    = доля слов из reference которые есть в prediction
f1        = 2 * precision * recall / (precision + recall)


Ожидаемые результаты — проверь себя после написания:

("the cat sat on the mat", "the cat sat")                       → precision=1.0, recall=0.5, f1=0.667
("the cat sat on the mat", "the cat sat on the mat the cat")    → precision=0.667, recall=1.0, f1=0.8
("machine learning is great", "deep learning is great")         → precision=0.75, recall=0.75, f1=0.75
("hello world", "foo bar")                                      → precision=0.0, recall=0.0, f1=0.0
"""

pairs = [
    ("the cat sat on the mat", "the cat sat"),  # высокий precision, низкий recall
    (
        "the cat sat on the mat",
        "the cat sat on the mat the cat",
    ),  # низкий precision, высокий recall
    ("machine learning is great", "deep learning is great"),  # частичное совпадение
    ("hello world", "foo bar"),  # нет совпадений
]


def rouge1(reference: str, prediction: str) -> dict:
    ref_words = set(reference.split())
    pred_words = set(prediction.split())
    matches = ref_words & pred_words  # одно пересечение

    precision = round(len(matches) / len(pred_words), 3) if pred_words else 0.0
    recall = round(len(matches) / len(ref_words), 3) if ref_words else 0.0
    f1 = (
        round(2 * precision * recall / (precision + recall), 3)
        if (precision + recall) > 0
        else 0.0
    )

    return {"precision": precision, "recall": recall, "f1": f1}


for ref, pred in pairs:
    print(rouge1(ref, pred))
