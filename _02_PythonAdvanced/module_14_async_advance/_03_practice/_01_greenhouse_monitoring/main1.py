import asyncio
import random


# async def temperature_sensor():
#     """Симуляция работы датчика температуры"""
#     for i in range(5):
#         await asyncio.sleep(random.uniform(1, 3))
#         temperature = random.uniform(-10, 35)
#         print(f'[Температура] Данные: {temperature:.2f}°C')
#
#
# async def humidity_sensor():
#     """Симуляция работы датчика влажности"""
#     for i in range(5):
#         await asyncio.sleep(random.uniform(1, 3))
#         humidity = random.uniform(30, 90)
#         print(f'[Влажность] Данные: {humidity:.2f}%')
#
#
# async def main():
#     print('Запуск системы мониторинга теплицы...\n')
#     temperature_task = asyncio.create_task(temperature_sensor())
#     humidity_task = asyncio.create_task(humidity_sensor())
#
#     await temperature_task
#     await humidity_task
#     print('\nМониторинг завершен. Все данные собраны.')

async def read_temperature_sensor():
    """Имитация считывания данных с датчика температуры."""
    print("Считывание данных с датчика температуры...")
    await asyncio.sleep(random.uniform(1, 3))
    temp = random.uniform(18, 30)
    print(f'Температура в теплице: {temp:.2f}°C')
    return temp


async def read_humidity_sensor():
    """Имитация считывания данных с датчика влажности."""
    print("Считывание данных с датчика влажности...")
    await asyncio.sleep(random.uniform(2, 4))
    humidity = random.uniform(40, 70)
    print(f'Влажность в теплице: {humidity:.2f}%')
    return humidity


async def monitor_climate():
    """Мониторинг данных с датчиков температуры и влажности."""
    # Запускаем оба считывания с использованием asyncio.gather
    temperature_task = read_temperature_sensor()
    humidity_task = read_humidity_sensor()

    # ожидаем завершения обеих задач
    results = await asyncio.gather(temperature_task, humidity_task)

    # Собираем результаты
    temperature, humidity = results
    print(f'Средняя температура: {temperature:.2f}°C')
    print(f'Средняя влажность:{humidity:.2f}%')


if __name__ == '__main__':
    asyncio.run(monitor_climate())
