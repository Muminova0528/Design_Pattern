class TelegramClient:

    def sendTelegramMessage(self, chatId: str, text: str) -> None:
        print(f"Telegram message sent to chat {chatId}: {text}")