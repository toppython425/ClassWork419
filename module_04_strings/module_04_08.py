# keywords = ['срочно', 'важно', 'немедленно']
#
# message = input("Введите ваше сообщение: ")
#
# urgent = False
# for keyword in keywords:
#     if keyword in message.lower():
#         urgent = True
#         break
#
# if urgent is True:
#     message = "ВНИМАНИЕ: " + message.upper()
# print(f"Обработанное сообщение: {message}")


urgent_keywords = ["асап", "сейчас", "немедленно"]
client_message = input("Введите текст обращения клиента: ")

urgent = False
for keyword in urgent_keywords:
    if keyword in client_message.lower():
        urgent = True
        break

if urgent:
    client_message = "СРОЧНО: " + client_message.upper()
print("Обработанное обращение:", client_message)