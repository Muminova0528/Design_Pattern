from sms_notification_service import SmsNotificationService
from telegram_client import TelegramClient
from email_client import EmailClient
from telegram_adapter import TelegramAdapter
from email_adapter import EmailAdapter
from notification_manager import NotificationManager


def main() -> None:
    # 1. SMS notification
    sms_service = SmsNotificationService()
    sms_manager = NotificationManager(sms_service)
    sms_manager.send_notification(
        "+998901234567",
        "Hello via SMS!"
    )

    # 2. Telegram notification
    telegram_client = TelegramClient()
    telegram_adapter = TelegramAdapter(telegram_client)
    telegram_manager = NotificationManager(telegram_adapter)
    telegram_manager.send_notification(
        "123456789",
        "Hello via Telegram!"
    )

    # 3. Email notification
    email_client = EmailClient()
    email_adapter = EmailAdapter(email_client, "Test Email")
    email_manager = NotificationManager(email_adapter)
    email_manager.send_notification(
        "test@example.com",
        "Hello via Email!"
    )


if __name__ == "__main__":
    main()