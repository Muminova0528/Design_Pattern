from notification_service import NotificationService


class NotificationManager:

    def __init__(self, notification_service: NotificationService) -> None:
        self.notification_service = notification_service

    def send_notification(self, recipient: str, message: str) -> None:
        self.notification_service.send(recipient, message)