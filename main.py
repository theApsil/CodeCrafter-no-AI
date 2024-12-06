from templates import match_template
from synonyms import normalize_text
from code_generator.python_gen import generate_python_code
from code_generator.rust_gen import generate_rust_code
from typing import Tuple, Optional

def generate_code(task_type: str, params: Tuple[str, ...]) -> str:
    """
    Генерирует код для заданного типа задачи и параметров только на том языке, который запрошен.
    
    :param task_type: Тип задачи (sort, init_list, inheritance)
    :param params: Кортеж параметров, извлечённых из шаблона
    :return: Строка с сгенерированным кодом (на Python или Rust).
    """
    lang = params[-1]

    if lang == "python":
        return generate_python_code(task_type, params)
    elif lang == "rust":
        return generate_rust_code(task_type, params)
    else:
        return "# Неподдерживаемый язык"

if __name__ == "__main__":
    print("Введите задачу:")
    input_text = input("> ")
    normalized_text = normalize_text(input_text)
    task_type, params = match_template(normalized_text)

    if task_type:
        code = generate_code(task_type, params)
        print("Сгенерированный код:\n")
        print(code)
    else:
        print("Шаблон задачи не распознан.")
