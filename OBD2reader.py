import asyncio
import obd

# Establish connection with the OBD-II adapter
connection = obd.OBD()

# Define the list of PIDs (Parameter IDs) to monitor
pids = [
    obd.commands.SPEED,  # Vehicle speed
    obd.commands.RPM,  # Engine RPM
    obd.commands.THROTTLE_POS,  # Throttle position
    obd.commands.COOLANT_TEMP,  # Coolant temperature
    obd.commands.INTAKE_TEMP,  # Intake air temperature
    # Add more PIDs as needed
]

# Function to continuously read and print the non-speed and non-RPM parameters
async def read_non_speed_rpm_params():
    while True:
        for pid in pids[2:]:  # Exclude speed and RPM from this loop
            response = connection.query(pid)
            if response.is_successful():
                value = response.value
                print(f"{pid.name}: {value}")
            else:
                print(f"Error retrieving {pid.name} data")
        
        print("---------------------")
        await asyncio.sleep(1)

# Function to continuously read and print the speed and RPM parameters
async def read_speed_rpm_params():
    while True:
        for pid in pids[:2]:  # Only speed and RPM in this loop
            response = connection.query(pid)
            if response.is_successful():
                value = response.value
                print(f"{pid.name}: {value}")
            else:
                print(f"Error retrieving {pid.name} data")
        
        print("---------------------")
        await asyncio.sleep(0.1)

# Main program loop
async def main():
    # Create tasks for reading non-speed and non-RPM parameters, and speed and RPM parameters
    tasks = [
        asyncio.create_task(read_non_speed_rpm_params()),
        asyncio.create_task(read_speed_rpm_params())
    ]

    # Run the tasks concurrently
    await asyncio.gather(*tasks)

# Run the main program loop
asyncio.run(main())
