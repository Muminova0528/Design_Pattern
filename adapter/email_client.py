class EmailClient:

    def sendEmail(
        self,
        emailAddress: str,
        subject: str,
        body: str
    ) -> None:
        print(
            f"Email sent to {emailAddress} | "
            f"Subject: {subject} | Body: {body}"
        )
        