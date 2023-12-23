import pymodbus.client as modbus_client

# PLC connection details (replace with your values)
plc_ip_address = "192.168.1.100"
plc_port = 502
register_address = 100

# Create a Modbus client
client = modbus_client.ModbusTcpClient(plc_ip_address, plc_port)

try:
    # Connect to the PLC
    client.connect()
    print("Connected to PLC!")

    # Read a register value
    result = client.read_holding_registers(register_address, 1)
    register_value = result.registers[0]
    print("Register value:", register_value)

except Exception as e:
    print("Connection error:", e)
finally:
    # Close the connection
    if client.is_socket_open():
        client.close()
        print("Connection closed.")
