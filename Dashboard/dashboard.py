import telemetry
import time
import data_logger

#Creates data display 
def display_dashboard(data):

    print("==============================")
    print("    EV TELEMETRY DASHBOARD    ")
    print("==============================")

    print(f"Battery Voltage: {data['battery_voltage']} V")
    print(f"Motor Temperature: {data['motor_temperature']} °C")
    print(f"Throttle: {data['throttle']} %")
    print(f"System Status: {data['system_status']} ")

    print("==============================")

while True:

    #get data from telemetry module
    data = telemetry.get_telemetry()
    
    #save data into file using data_logger module
    data_logger.save_data(data)

    #display data
    display_dashboard(data)

    #add delay for smooth function
    time.sleep(1)

