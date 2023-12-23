# plc_connection.py
import serial
import time

class PLCConnection:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.connection = None

    def connect(self):
        print(f"port: {self.port}")
        print(f"baudrate: {self.baudrate}")
        try:
            self.connection = serial.Serial(self.port, self.baudrate, timeout=2)
            return True
        except Exception as e:
            print(f"Error connecting to PLC: {e}")
            return False

    def disconnect(self):
        if self.connection and self.connection.isOpen():
            self.connection.close()

    def send_data(self, data):
        if self.connection and self.connection.isOpen():
            try:
                self.connection.write(data.encode())
                return True
            except Exception as e:
                print(f"Error sending data to PLC: {e}")
        return False
