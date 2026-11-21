from notification_service import NotificationService
from email_client import EmailClient


class EmailAdapter(NotificationService):

    def __init__(self, email_client: EmailClient, subject: str = "Notification") -> None:
        self.email_client = email_client
        self.subject = subject

    def send(self, recipient: str, message: str) -> None:
        self.email_client.sendEmail(
            recipient,
            self.subject,
            message
        )