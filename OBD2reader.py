import time
import obd

# Establish connection with the OBD-II adapter
connection = obd.OBD()

# Define the list of PIDs (Parameter IDs) to monitor
pids = [
    obd.commands.RPM,  # Engine RPM
    obd.commands.SPEED,  # Vehicle speed
    obd.commands.COOLANT_TEMP,  # Coolant temperature
    obd.commands.INTAKE_TEMP,  # Intake air temperature
    obd.commands.MAF,  # Mass air flow rate
    obd.commands.FUEL_LEVEL,  # Fuel level
    obd.commands.FUEL_RATE,  # Fuel consumption rate
    # Add more PIDs as needed from the previous list
]

# Main program loop
while True:
    # Iterate over each PID in the list and read its value
    for pid in pids:
        response = connection.query(pid)
        if response.is_successful():
            value = response.value
            print(f"{pid.name}: {value}")
        else:
            print(f"Error retrieving {pid.name} data")

    print("---------------------")

    # Wait for 1 second before reading the values again
    time.sleep(1)
