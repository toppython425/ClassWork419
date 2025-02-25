import asyncio
import random

ports = [22, 80, 443, 8080, 3306]


async def check_port(port):
    """Симуляция проверки порта"""
    delay = random.uniform(1, 3)
    print(f'Проверка порта {port} начата (займет {delay:.2f} сек.).')
    await asyncio.sleep(delay)
    is_open = random.choice([True, False])
    if is_open:
        print(f'Порт {port} открыт')
    else:
        print(f'Порт {port} закрыт')


async def main():
    print("Начинаем сканирование портов...\n")

    # создаем таски для проверки портов
    tasks = [check_port(port) for port in ports]
    print(tasks)
    # tasks_list = []
    # for port in ports:
    #     tasks_list.append(check_port(port))
    # print(tasks_list)
    await asyncio.gather(*tasks)
    # await asyncio.gather(*tasks_list)
    print('\nСканирование завершено.')


if __name__ == '__main__':
    asyncio.run(main())
