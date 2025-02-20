import asyncio
import random


async def temperature_sensor():
    """Симуляция работы датчика температуры"""
    for i in range(5):
        await asyncio.sleep(random.uniform(1, 3))
        temperature = random.uniform(-10, 35)
        print(f'[Температура] Данные: {temperature:.2f}°C')


async def humidity_sensor():
    """Симуляция работы датчика влажности"""
    for i in range(5):
        await asyncio.sleep(random.uniform(1, 3))
        humidity = random.uniform(30, 90)
        print(f'[Влажность] Данные: {humidity:.2f}%')


async def main():
    print('Запуск системы мониторинга теплицы...\n')
    temperature_task = asyncio.create_task(temperature_sensor())
    humidity_task = asyncio.create_task(humidity_sensor())

    await temperature_task
    await humidity_task
    print('\nМониторинг завершен. Все данные собраны.')


if __name__ == '__main__':
    asyncio.run(main())
