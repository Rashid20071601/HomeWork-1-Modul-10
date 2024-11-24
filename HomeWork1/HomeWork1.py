# Импортируем библиотеки
import threading
from time import sleep, time

# Функция для записи слов в файл
def write_words(word_count, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:  # Открываем файл для записи
            for i in range(1, word_count + 1):  # Цикл записи строк
                file.write(f"Какое-то слово № {i}\n")
                sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")
    except Exception as e:
        print(f"Ошибка записи в файл {file_name}: {e}")

# Засекаем время выполнения функций
functions_start_time = time()

write_words(10, 'example1.txt')  # Запуск функции записи
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

functions_end_time = time()
print(f'Работа функций заняла {round(functions_end_time - functions_start_time, 1)} секунд')  # Выводим время работы

# Засекаем время выполнения потоков
threads_start_time = time()

threads = [  # Создаем потоки
    threading.Thread(target=write_words, args=(10, 'example5.txt')),
    threading.Thread(target=write_words, args=(30, 'example6.txt')),
    threading.Thread(target=write_words, args=(200, 'example7.txt')),
    threading.Thread(target=write_words, args=(100, 'example8.txt'))
]

for thread in threads:
    thread.start()  # Запускаем потоки

for thread in threads:
    thread.join()  # Ждем завершения потоков

threads_end_time = time()
print(f'Работа потоков заняла {round(threads_end_time - threads_start_time, 1)} секунд')  # Выводим время работы потоков
