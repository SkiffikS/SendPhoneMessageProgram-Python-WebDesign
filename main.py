from twilio.rest import Client
import eel


eel.init("web")

@eel.expose
def send_sms(text: str, number: str, n: str):

    try:

        account_sid = "AAa00a0000a0aaaa0a000a0aaa0000a000"
        author_tocken = "aa000a00aa000aaa0000aa000000a0aa"

        client = Client(account_sid, author_tocken)

        n = int(n)

        for i in range(n):
            message = client.messages.create(
                body = text,
                from_ = "+00000000000",
                to = number
            )

        return "Повідомлення відправлено успішно!"

    except Exception as ex:
        
        return f"Виникла помилка при відправленні повідомлення"


if __name__ == "__main__":
    eel.start("main.html", size = (700, 700))