from typing import Tuple

def bubble_sort_rust(elements: str) -> str:
    """
    Возвращает код пузырьковой сортировки на Rust.
    """
    return f"""
// Rust: пузырьковая сортировка
fn main() {{
    let mut elements = vec!{elements};
    let n = elements.len();
    for i in 0..n {{
        for j in 0..(n - i - 1) {{
            let a = &elements[j];
            let b = &elements[j+1];
            let swap = if a.is_ascii() && b.is_ascii() {{
                a.to_string().to_lowercase() > b.to_string().to_lowercase()
            }} else {{
                a > b
            }};
            if swap {{
                elements.swap(j, j+1);
            }}
        }}
    }}
    println!("{{:?}}", elements);
}}
"""

def quick_sort_rust(elements: str) -> str:
    """
    Возвращает код быстрой сортировки на Rust.
    """
    return f"""
// Rust: быстрая сортировка
fn quicksort<T: PartialOrd + Clone>(arr: Vec<T>) -> Vec<T> {{
    if arr.len() <= 1 {{
        return arr;
    }}
    let pivot = arr[arr.len() / 2].clone();
    let mut left = Vec::new();
    let mut middle = Vec::new();
    let mut right = Vec::new();

    for x in arr {{
        if x < pivot {{
            left.push(x);
        }} else if x == pivot {{
            middle.push(x);
        }} else {{
            right.push(x);
        }}
    }}
    let mut result = quicksort(left);
    result.extend(middle);
    result.extend(quicksort(right));
    result
}}

fn main() {{
    let elements = vec!{elements};
    let sorted = quicksort(elements);
    println!("{{:?}}", sorted);
}}
"""

def generate_rust_code(task_type: str, params: Tuple[str, ...]) -> str:
    """
    Генерирует код на Rust для заданного типа задачи.

    :param task_type: Тип задачи (sort, init_list, inheritance)
    :param params: Кортеж параметров, извлечённых из шаблона
    :return: Строка с Rust-кодом.
    """
    if task_type == "sort":
        elements, sort_type, _ = params
        if sort_type == "пузырьковой":
            return bubble_sort_rust(elements)
        elif sort_type == "быстрой":
            return quick_sort_rust(elements)

    elif task_type == "init_list":
        start, end, _ = params
        if start.isalpha() and end.isalpha():
            return f"""
// Rust: инициализация списка букв
fn main() {{
    let elements: Vec<char> = ('{start}'..='{end}').collect();
    println!("{{:?}}", elements);
}}
"""
        else:
            return f"""
// Rust: инициализация списка чисел
fn main() {{
    let elements: Vec<i32> = ({start}..={end}).collect();
    println!("{{:?}}", elements);
}}
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
fn main() {{
    // Здесь можно создать экземпляр:
    // let p = {parent_class}{{}};
    // let c = {class_name}::new(p);
}}
"""

    return ""
