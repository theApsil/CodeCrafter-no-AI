from typing import Tuple

def generate_rust_code(task_type: str, params: Tuple[str, ...]) -> str:
    """
    Генерирует код на Rust для заданного типа задачи и параметров.
    
    :param task_type: Тип задачи (sort, init_list, inheritance)
    :param params: Кортеж параметров, извлечённых из шаблона
    :return: Строка с сгенерированным Rust-кодом.
    """
    if task_type == "sort":
        elements, sort_type, _ = params
        # В Rust элементы списка нужно корректно интерпретировать
        # Для упрощения предполагаем, что пользователь задаёт в формате [1,2,3] или ['a','b']
        return f"""
// Rust: сортировка {sort_type}
let mut elements = vec!{elements};
elements.sort();
println!("{{:?}}", elements);
"""

    elif task_type == "init_list":
        start, end, _ = params
        if start.isalpha() and end.isalpha():
            return f"""
// Rust: инициализация списка букв
let elements: Vec<char> = ('{start}'..='{end}').collect();
println!("{{:?}}", elements);
"""
        else:
            return f"""
// Rust: инициализация списка чисел
let elements: Vec<i32> = ({start}..={end}).collect();
println!("{{:?}}", elements);
"""

    elif task_type == "inheritance":
        class_name, parent_class, _ = params
        return f"""
// Rust: условное "наследование" через композицию
struct {class_name} {{
    parent: {parent_class},
}}

impl {class_name} {{
    fn new(parent: {parent_class}) -> Self {{
        {class_name} {{ parent }}
    }}
}}
"""
    return ""
