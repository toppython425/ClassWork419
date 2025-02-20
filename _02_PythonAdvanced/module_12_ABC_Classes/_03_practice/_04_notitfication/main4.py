from classes4 import EmailNotification

if __name__ == '__main__':
    email_notification = EmailNotification('doe@example.com', 'Hello John')
    email_notification_result = email_notification.send()
    email_notification_counter = 0
    # while not email_notification_result and email_notification_counter < 10:
    #     print(email_notification.get_details())
    #     email_notification_result = email_notification.send()
    #     email_notification_counter += 1
    #
    # if email_notification_counter == 10:
    #     print('Невозможно отправить письмо')
    # else:
    #     print(email_notification.get_details())

    while not email_notification_result:
        if email_notification_counter == 10:
            print('Невозможно отправить письмо')
            break
        print(email_notification.get_details())
        email_notification_result = email_notification.send()
        email_notification_counter += 1
    else:
        print(email_notification.get_details())
