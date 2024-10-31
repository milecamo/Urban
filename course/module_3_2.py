# Задача "Рассылка писем"

def send_email(message, recipient, *, sender='university.help@gmail.com'):
    for i in recipient, sender:
        address = i.lower()
        add_length = len(i)
        if ((not '@' in address) or
                not ('.com' == address[add_length - 4:add_length] or
                     '.net' == address[add_length - 4:add_length] or
                     '.ru' == address[add_length - 3:add_length])):
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            return
    if sender.lower() == recipient.lower():
        print("Нельзя отправить письмо самому себе!")
        return
    if "university.help@gmail.com" == sender.lower():
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        return
    print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Cообщение на короткий адрес', 'e@')
