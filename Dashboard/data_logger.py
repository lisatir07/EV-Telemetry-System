import csv
import os
from datetime import datetime

# function that logs data : takes telemetry dictionary
# and saves it as one row in a CSV file

def save_data(data):
    timestamp = datetime.now()

    #check if file already exists
    file_exists = os.path.exists("telemetry_data.csv")

    #creates CSV file
    with open("telemetry_data.csv", "a", newline="") as file:

        #create tool to write to the file
        writer = csv.writer(file)

        #add headers if file does not exist
        if not file_exists:
            writer.writerow([
                "timestamp",
                "battery_voltage",
                "motor_temperature",
                "throttle",
                "system_status"
            ])

        #write to file 
        writer.writerow([
            timestamp,
            data["battery_voltage"],
            data["motor_temperature"],
            data["throttle"],
            data["system_status"]
        ])
    
