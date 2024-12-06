import re
from typing import Optional, Tuple

TEMPLATES = [
    (r'sort\s+(.+)\s+(пузырьковой|быстрой|бинарной)\s+сортировкой\s+на\s+(python|rust)', "sort"),
    (r'init_list\s+от\s+([a-яё0-9\-]+)\s+до\s+([a-яё0-9\-]+)\s+на\s+(python|rust)', "init_list"),
    (r'inheritance\s+класса\s+(\w+)\s+от\s+(\w+)', "inheritance")
]

def match_template(text: str) -> Tuple[Optional[str], Optional[Tuple[str, ...]]]:
    """
    Сопоставляет нормализованный текст с шаблонами задач.
    
    :param text: Текст для сопоставления.
    :return: Кортеж (task_type, params) или (None, None), если сопоставление не удалось.
    """
    for pattern, task_type in TEMPLATES:
        match = re.match(pattern, text)
        if match:
            return task_type, match.groups()
    return None, None
