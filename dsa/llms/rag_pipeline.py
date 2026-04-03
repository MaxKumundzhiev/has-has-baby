"""
RAG — Retrieval Augmented Generation. Три слова объясняют всё:

Retrieval — достаём релевантные куски из базы знаний по запросу пользователя.
В реальных системах через cosine similarity между embedding векторами, в нашей задаче — через пересечение слов.

Augmented — дополняем запрос пользователя найденным контекстом. Итоговый промпт = контекст + вопрос.

Generation — LLM отвечает на основе контекста, а не только своих весов. Это снижает hallucination.

Зачем RAG а не fine-tuning:
    fine-tuning дорогой и медленный, знания устаревают.
    RAG — дешевле, данные обновляются без переобучения.
"""

documents = [
    "Python was created by Guido van Rossum in 1991.",
    "Machine learning models require large amounts of training data.",
    "RAG combines retrieval systems with language model generation.",
    "Neural networks consist of layers of interconnected nodes.",
    "Data preprocessing includes cleaning, normalization, and splitting.",
    "Overfitting occurs when a model learns training data too well.",
    "Python is widely used in data science and machine learning.",
]

qa_pairs = [
    {
        "query": "who created Python and when?",
        "reference": "Python was created by Guido van Rossum in 1991",
        "answer": "Python was created by Guido van Rossum in 1991",
    },
    {
        "query": "what is overfitting?",
        "reference": "overfitting occurs when model learns training data too well",
        "answer": "overfitting is when the model memorizes training examples",
    },
    {
        "query": "what does RAG stand for?",
        "reference": "RAG combines retrieval systems with language model generation",
        "answer": "RAG is a technique that combines retrieval and generation",
    },
]


def retrieve(query: str, documents: list[str], top_k: int = 2) -> list[str]:
    """
    Находим top_k самых релевантных документов для запроса.

    Логика:
        1. Разбиваем query на слова → множество
        2. Для каждого документа считаем score = пересечение слов с query
           В реальных системах здесь cosine similarity между embedding векторами.
           Мы используем пересечение как упрощение — идея та же: больше общих
           слов = документ более релевантен.
        3. Сортируем по score убыванием
        4. Возвращаем top_k документов с score > 0
           Документы с нулевым score не релевантны — лучше вернуть меньше,
           чем добавлять шум в контекст.
    """
    query_words = set(query.lower().split())
    scores = [(len(query_words & set(doc.lower().split())), doc) for doc in documents]
    scores.sort(key=lambda x: -x[0])
    return [doc for score, doc in scores[:top_k] if score > 0]


def build_prompt(query: str, context: list[str]) -> str:
    """
    Собираем финальный промпт который пойдёт в LLM.

    Логика:
        1. Если контекст пустой — задаём вопрос без контекста.
           Лучше честный промпт без контекста чем нерелевантный шум.
        2. Если контекст есть — вставляем его перед вопросом.
           Явная инструкция "answer based only on the context" критична:
           без неё модель может добавить информацию из своих весов
           которая противоречит контексту → hallucination.

    Структура промпта:
        Context:
        - doc1
        - doc2

        Question: ...
        Answer based only on the context above.
    """
    if not context:
        return f"Question: {query}\nAnswer:"

    context_str = "\n".join(f"- {doc}" for doc in context)
    return (
        f"Context:\n{context_str}\n\n"
        f"Question: {query}\n"
        f"Answer based only on the context above."
    )


def rouge1_f1(reference: str, prediction: str) -> float:
    """
    Считаем ROUGE-1 F1 — автоматическая метрика качества ответа.

    Логика:
        1. Разбиваем оба текста на множества слов (set убирает дубли)
        2. matches = пересечение — слова которые есть в обоих текстах
        3. precision = matches / len(pred) — насколько ответ точный
           (из всего что сказала модель — сколько совпало с эталоном)
        4. recall = matches / len(ref) — насколько ответ полный
           (из всего что было в эталоне — сколько модель покрыла)
        5. F1 = гармоническое среднее — баланс между точностью и полнотой

    Ограничение: set() игнорирует порядок слов и повторения.
    В реальных системах используют ROUGE с учётом повторений (не set а Counter),
    или BERTScore который учитывает семантическую близость.
    """
    ref_words = set(reference.lower().split())
    pred_words = set(prediction.lower().split())
    matches = ref_words & pred_words

    precision = len(matches) / len(pred_words) if pred_words else 0.0
    recall = len(matches) / len(ref_words) if ref_words else 0.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if (precision + recall) > 0
        else 0.0
    )
    return round(f1, 3)


def rag_pipeline(qa_pairs: list[dict], documents: list[str]) -> list[dict]:
    """
    Полный RAG pipeline: retrieve → augment → evaluate.

    Логика для каждой пары (query, reference, answer):
        1. retrieve  — находим релевантные документы из базы
        2. build_prompt — собираем промпт (в реальности отправили бы в LLM,
           здесь answer уже симулирован)
        3. rouge1_f1 — оцениваем качество answer против reference
        4. собираем результат в dict

    В продакшне между шагами 2 и 3 стоит вызов LLM API.
    Здесь answer подставлен заранее чтобы показать pipeline без API.
    """
    results = []
    for pair in qa_pairs:
        query = pair["query"]
        reference = pair["reference"]
        answer = pair["answer"]

        retrieved = retrieve(query, documents)
        prompt = build_prompt(query, retrieved)
        score = rouge1_f1(reference, answer)

        results.append(
            {
                "query": query,
                "retrieved_docs": retrieved,
                "prompt": prompt,
                "answer": answer,
                "rouge1": score,
            }
        )
    return results


results = rag_pipeline(qa_pairs, documents)
for r in results:
    print(f"query:     {r['query']}")
    print(f"retrieved: {r['retrieved_docs']}")
    print(f"rouge1:    {r['rouge1']}")
    print()
