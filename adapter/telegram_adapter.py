from notification_service import NotificationService
from telegram_client import TelegramClient


class TelegramAdapter(NotificationService):

    def __init__(self, telegram_client: TelegramClient) -> None:
        self.telegram_client = telegram_client

    def send(self, recipient: str, message: str) -> None:
        self.telegram_client.sendTelegramMessage(recipient, message)