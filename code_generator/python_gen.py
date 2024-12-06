from typing import Tuple

def bubble_sort_python(elements: list) -> str:
    """
    Возвращает код пузырьковой сортировки на Python.
    """
    return f"""
# Python: пузырьковая сортировка
elements = {elements}
n = len(elements)
for i in range(n):
    for j in range(0, n - i - 1):
        if isinstance(elements[j], str) and isinstance(elements[j+1], str):
            if elements[j].lower() > elements[j+1].lower():
                elements[j], elements[j+1] = elements[j+1], elements[j]
        else:
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
print(elements)
"""

def quick_sort_python(elements: list) -> str:
    """
    Возвращает код быстрой сортировки на Python.
    """
    return f"""
# Python: быстрая сортировка
elements = {elements}

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    for x in arr:
        if isinstance(x, str) and isinstance(pivot, str):
            if x.lower() < pivot.lower():
                left.append(x)
            elif x.lower() == pivot.lower():
                middle.append(x)
            else:
                right.append(x)
        else:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)
    return quicksort(left) + middle + quicksort(right)

sorted_elements = quicksort(elements)
print(sorted_elements)
"""

def generate_python_code(task_type: str, params: Tuple[str, ...]) -> str:
    """
    Генерирует код на Python для заданного типа задачи.

    :param task_type: Тип задачи (sort, init_list, inheritance)
    :param params: Кортеж параметров, извлечённых из шаблона
    :return: Строка с сгенерированным Python-кодом.
    """
    if task_type == "sort":
        elements, sort_type, _ = params
        elements_list = eval(elements)
        if sort_type == "пузырьковой":
            return bubble_sort_python(elements_list)
        elif sort_type == "быстрой":
            return quick_sort_python(elements_list)

    elif task_type == "init_list":
        start, end, _ = params
        if start.isalpha() and end.isalpha():
            return f"""
# Python: инициализация списка букв
elements = [chr(i) for i in range(ord('{start}'), ord('{end}') + 1)]
print(elements)
"""
        else:
            return f"""
# Python: инициализация списка чисел
elements = list(range({start}, {end} + 1))
print(elements)
"""
    elif task_type == "inheritance":
        class_name, parent_class, _ = params
        return f"""
# Python: наследование класса
class {class_name}({parent_class}):
    def __init__(self):
        super().__init__()
        # Ваш код здесь
"""

    return ""
