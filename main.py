from code_generator.python_gen import generate_python_code
from code_generator.rust_gen import generate_rust_code
from templates import match_template
from synonyms import normalize_text
from typing import Dict, Any, Tuple, Optional


def generate_code(task_type: str, params: Tuple[str, ...]) -> Dict[str, str]:
    """
    Генерирует код на Python и Rust для заданного типа задачи и параметров.

    :param task_type: Тип задачи (sort, init_list, inheritance)
    :param params: Кортеж параметров, извлечённых из шаблона
    :return: Словарь с ключами "Python" и "Rust", содержащий сгенерированный код.
    """
    if task_type == "sort":
        return {
            "Python": generate_python_code("sort", params),
            "Rust": generate_rust_code("sort", params)
        }
    elif task_type == "init_list":
        return {
            "Python": generate_python_code("init_list", params),
            "Rust": generate_rust_code("init_list", params)
        }
    elif task_type == "inheritance":
        return {
            "Python": generate_python_code("inheritance", params),
            "Rust": generate_rust_code("inheritance", params)
        }
    return {}

if __name__ == "__main__":
    print("Введите задачу:")
    input_text = input("> ")
    normalized_text = normalize_text(input_text)
    task_type, params = match_template(normalized_text)

    if task_type:
        code = generate_code(task_type, params)
        print("Сгенерированный код:\n")
        for lang, code_output in code.items():
            print(f"--- {lang} ---\n{code_output}")
    else:
        print("Шаблон задачи не распознан.")