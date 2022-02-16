# исполняющий скрипт

api_id = 
api_hash = 

from telethon.sync import TelegramClient
import telethon
import sqlite3
        
counter = 0

client = TelegramClient('session_name', api_id=api_id, api_hash=api_hash)
client.start()

def rows():
    try:
        conn = sqlite3.connect('main.db')
        cur = conn.cursor()

        query = """SELECT * FROM users"""
        record = cur.execute(query)
        result = record.fetchall()

        cur.close()
        conn.commit()
    except sqlite3.Error as err:
        print(err)
    finally:
        conn.close()

    return result

for i in rows():

    counter += 1

    def select():
        try:
            conn = sqlite3.connect('main.db')
            cur = conn.cursor()

            query_phone = f"""SELECT phone FROM users WHERE type = 0 AND id = {counter}"""
            record_phone = cur.execute(query_phone)
            result_phone = record_phone.fetchall()

            query_message = f"""SELECT message FROM users WHERE type = 0 AND id = {counter}"""
            record_message = cur.execute(query_message)
            result_message = record_message.fetchall()

            query_type = f"""SELECT type FROM users WHERE id = {counter}"""
            record_type = cur.execute(query_type)
            result_type = record_type.fetchall()

            if result_type[0][0] == 1:
                update_sended()
                return 1

            if result_type[0][0] == 2:
                update_error()
                return 2

            cur.close()
            conn.commit()
        except sqlite3.Error as err:
            print(err)
        finally:
            conn.close()

        return result_phone, result_message

    def checker(data):
        if data == 1:
            print('Return Error: [type = 1 or 2]')
        elif data == 2:
            update_type_second()
        else:
            phone = data[0][0][0]
            message = data[1][0][0]

            add_contact(phone, message)

    def add_contact(number, message):
        response = client(telethon.functions.contacts.ImportContactsRequest(
            contacts=[telethon.types.InputPhoneContact(
                client_id=0,
                phone = number,
                first_name='Firstname',
                last_name='Lastname'
            )]
        ))

        if response.imported == []:
            print('Такого контакта нету в телеграмме или номер скрыт')
        else:
            send_mes(number, message)

    def send_mes(phone, message):
        send = client.send_message(str(phone), str(message))
        if send.out == True:
            print('Сообщение отправлено')
            update()
        else:
            print('Сообщение не отправлено')

    def update():
        try:
            conn = sqlite3.connect('main.db')
            cur = conn.cursor()

            query = f"""UPDATE users SET type = 1 WHERE id = {counter}"""
            cur.execute(query)
            print('Данные обновлены')

            cur.close()
            conn.commit()
        except sqlite3.Error as err:
            print(err)
        finally:
            conn.close()

    def update_sended():
        try:
            conn = sqlite3.connect('main.db')
            cur = conn.cursor()

            query = f"""UPDATE users SET error_message = 'Сообщение было отправлено' WHERE id = {counter}"""
            cur.execute(query)

            cur.close()
            conn.commit()
        except sqlite3.Error as err:
            print(err)
        finally:
            conn.close()

    def update_error():
        try:
            conn = sqlite3.connect('main.db')
            cur = conn.cursor()

            query = f"""UPDATE users SET error_message = 'сообщение не было отправлено в связи с ошибкой' WHERE id = {counter}"""
            cur.execute(query)

            cur.close()
            conn.commit()
        except sqlite3.Error as err:
            print(err)
        finally:
            conn.close()

    def update_type_second():
        try:
            conn = sqlite3.connect('main.db')
            cur = conn.cursor()

            query = f"""UPDATE users SET type = 2 WHERE id = {counter}"""
            cur.execute(query)

            cur.close()
            conn.commit()
        except sqlite3.Error as err:
            print(err)
        finally:
            conn.close()

    checker(select())


