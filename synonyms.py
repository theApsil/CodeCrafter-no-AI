from typing import Dict, List

SYNONYMS: Dict[str, List[str]] = {
    "sort": ["отсортируй", "сделай сортировку", "упорядочи"],
    "init_list": ["инициализируй список", "создай список"],
    "inheritance": ["реализуй наследование", "наследуй"]
}

def normalize_text(text: str) -> str:
    """
    Приводит текст к унифицированной форме на основе словаря синонимов.
    
    :param text: Исходный текст для нормализации.
    :return: Нормализованный текст.
    """
    text = text.lower().strip()
    for task_type, keywords in SYNONYMS.items():
        for keyword in keywords:
            if keyword in text:
                text = text.replace(keyword, task_type)
                break
    return text
