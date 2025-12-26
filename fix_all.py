def clean_file(filename):
    """Очищает файл от лишних пробелов и добавляет пустую строку в конце"""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 1. Удаляем все пробелы/табы в конце каждой строки
    cleaned_lines = [line.rstrip() + '\n' for line in lines]
    
    # 2. Убеждаемся, что последняя строка заканчивается новой строкой
    if cleaned_lines and not cleaned_lines[-1].endswith('\n\n'):
        cleaned_lines[-1] = cleaned_lines[-1].rstrip() + '\n\n'
    
    # 3. Записываем обратно
    with open(filename, 'w', encoding='utf-8', newline='\n') as f:
        f.writelines(cleaned_lines)
    
    print(f"Файл {filename} очищен")

# Очищаем оба файла
clean_file('mortgage_calculator.py')
clean_file('test_mortgage_calculator.py')