def send_email(message, recipient, sender="university.help@gmail.com"):
    a = ["@", ".com", ".ru", ".net"]
    if not any(i in recipient for i in a) or not any(i in sender for i in a):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")


send_email("Привет", "Poleshookmail", "Poleshookmail.ru")

