from notification_service import NotificationService


class SmsNotificationService(NotificationService):

    def send(self, recipient: str, message: str) -> None:
        print(f"SMS sent to {recipient}: {message}")