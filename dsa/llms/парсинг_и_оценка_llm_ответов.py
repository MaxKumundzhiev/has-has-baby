"""
Дан список ответов модели и эталонных ответов.
Реализуй простую метрику качества:
    для каждого ответа посчитай долю слов из эталона которые присутствуют в ответе модели (упрощённый ROUGE-1 recall).
"""

references = [
    "the cat sat on the mat",
    "python is a programming language",
    "machine learning requires data",
]

predictions = [
    "a cat was sitting on mat",  # почти верно
    "python is used for programming",  # частично
    "deep learning needs lots of data",  # частично
]


def rouge1_recall(reference: str, prediction: str) -> float:
    """return count of words from reference which are in prediction"""
    ref_words, pred_words = set(reference.split()), set(prediction.split())
    matches = ref_words.intersection(pred_words)
    return round(len(matches) / len(ref_words), 3) if ref_words else 0.0


def evaluate_outputs(references, predictions) -> list[dict]:
    return [
        {"reference": r, "prediction": p, "rouge1": rouge1_recall(r, p)}
        for r, p in zip(references, predictions)
    ]


print(evaluate_outputs(references, predictions))
