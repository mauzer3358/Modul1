# Напишите 4 переменных которые буду обозначать следующие данные:
# Количество выполненных ДЗ (запишите значение 12)
# Количество затраченных часов (запишите значение 1.5)
# Название курса (запишите значение 'Python')
# Время на одно задание (вычислить используя 1 и 2 переменные)
# Выведите на экран(в консоль), используя переменные, следующую строку:
# Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.

home_works = 12
time = 1.5
name = 'Python'
time_task = time / home_works
print('Курс: ', name + ', всего задач:' + str(home_works) + ', затраченно часов: ', str(time) + ', среднее время выполнения ', time_task, ' часа')