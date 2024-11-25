import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert():
    try:
        # Email credentials
        sender_email = "yagnesh914@gmail.com"
        sender_password = "*************"  # Replace with your app password for Gmail
        recipient_email = "yagneshpallerla@gmail.com"

        # Message details
        subject = "Emergency Alert!"
        message_body = (
            "This is an alert from the Women Safety System. "
            "Please take immediate action. Call the alert number: 9347004560."
        )

        # Construct email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message_body, 'plain'))

        # Connect to Gmail SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print("Alert email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

# Call the function to send the email
send_email_alert()
