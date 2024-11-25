import smtplib
import serial
import time
from sklearn.externals import joblib
import json
from twilio.rest import Client

# Load pre-trained ML model
model = joblib.load('ml_model.pkl')  # Replace with your model file

# Serial communication setup (e.g., Arduino)
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust port and baud rate

# Twilio credentials for SMS alerts
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_client = Client(account_sid, auth_token)

def send_alert(location):
    """Send SMS or email alert."""
    message = f"Emergency Alert! Location: {location}"
    print("Sending alert...")
    
    # Twilio SMS example
    twilio_client.messages.create(
        body=message,
        from_='+1234567890',  # Replace with Twilio number
        to='+0987654321'  # Replace with recipient's number
    )

    # Email example
    sender_email = "your_email@gmail.com"
    receiver_email = "receiver_email@gmail.com"
    password = "your_password"
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        print("Email sent!")
    except Exception as e:
        print(f"Error sending email: {e}")

while True:
    try:
        # Read data from serial
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            print(f"Received data: {data}")
            
            # Assuming the data is JSON with 'sensor_data' and 'location'
            parsed_data = json.loads(data)
            sensor_data = parsed_data.get('sensor_data')
            location = parsed_data.get('location')
            
            # Predict emergency
            prediction = model.predict([sensor_data])
            if prediction == 1:  # Assuming 1 indicates an emergency
                send_alert(location)
                
        time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
        break
