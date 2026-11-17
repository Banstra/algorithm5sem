from collections import deque

def queue_with_numbers():
    queue = deque()
    
    print("=" * 60)
    print("РАБОТА С ЧИСЛОВОЙ ОЧЕРЕДЬЮ")
    print("=" * 60)
    
    while True:
        print("\n" + "-" * 60)
        print("МЕНЮ:")
        print("-" * 60)
        print("1. Добавить число в очередь")
        print("2. Извлечь число из очереди")
        print("3. Показать очередь")
        print("4. Сумма всех элементов в очереди")
        print("5. Среднее значение элементов")
        print("6. Минимальный элемент")
        print("7. Максимальный элемент")
        print("0. Выход")
        print("-" * 60)
        
        choice = input("Введите номер действия (0-7): ").strip()
        
        if choice == '1':
            try:
                num = float(input("Введите число: ").strip())
                queue.append(num)
                print(f" Число {num} добавлено в очередь")
            except ValueError:
                print(" Ошибка! Введите корректное число")
        
        elif choice == '2':
            if len(queue) == 0:
                print(" Очередь пуста!")
            else:
                item = queue.popleft()
                print(f" Извлечено число: {item}")
        
        elif choice == '3':
            if len(queue) == 0:
                print(" Очередь пуста!")
            else:
                print(f" Очередь: {list(queue)}")
        
        elif choice == '4':
            if len(queue) == 0:
                print(" Очередь пуста!")
            else:
                total = sum(queue)
                print(f" Сумма всех элементов: {total}")
        
        elif choice == '5':
            if len(queue) == 0:
                print(" Очередь пуста!")
            else:
                avg = sum(queue) / len(queue)
                print(f" Среднее значение: {avg:.2f}")
        
        elif choice == '6':
            if len(queue) == 0:
                print(" Очередь пуста!")
            else:
                min_val = min(queue)
                print(f" Минимальный элемент: {min_val}")
        
        elif choice == '7':
            if len(queue) == 0:
                print(" Очередь пуста!")
            else:
                max_val = max(queue)
                print(f" Максимальный элемент: {max_val}")
        
        elif choice == '0':
            print("\n" + "=" * 60)
            print("До свидания!")
            print("=" * 60)
            break
        
        else:
            print(" Неверный ввод!")
            
if __name__ == "__main__":
    queue_with_numbers()