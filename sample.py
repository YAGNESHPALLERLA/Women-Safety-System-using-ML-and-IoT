import serial
import time

# Set up the serial connection to the GSM module
gsm_port = "/dev/ttyUSB0"  # Replace with the correct port (e.g., COM3 on Windows)
baud_rate = 9600
gsm = serial.Serial(gsm_port, baud_rate, timeout=1)

def send_sms(phone_number, message):
    """
    Sends an SMS using a GSM module.
    """
    try:
        print("Initializing GSM module...")
        gsm.write(b'AT\r')
        time.sleep(1)
        response = gsm.read_all().decode()
        if "OK" not in response:
            print("GSM module not responding. Check the connection.")
            return

        # Set GSM module to SMS text mode
        gsm.write(b'AT+CMGF=1\r')
        time.sleep(1)
        response = gsm.read_all().decode()
        if "OK" not in response:
            print("Failed to set SMS text mode.")
            return

        # Set the recipient phone number
        gsm.write(f'AT+CMGS="{phone_number}"\r'.encode())
        time.sleep(1)

        # Write the message body
        gsm.write(message.encode())
        gsm.write(b'\x1A')  # Send Ctrl+Z to send the SMS
        time.sleep(3)  # Wait for the GSM module to send the message

        response = gsm.read_all().decode()
        if "OK" in response:
            print("SMS sent successfully!")
        else:
            print(f"Failed to send SMS. Response: {response}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        gsm.close()

# Example usage
if __name__ == "__main__":
    recipient_number = "+1234567890"  # Replace with the recipient's phone number
    sms_message = "Hello! This is a test message sent from Python."
    send_sms(recipient_number, sms_message)
