import random

#pulls data from the sensors (creates it) and supplies it to other modules
#hard coded values until STM32 arrives
def get_telemetry():
    battery_voltage = round(random.uniform(11.8,12.8), 2)
    motor_temperature = round(random.uniform(25.0, 40.0), 1)
    throttle = random.randint(0,100)

    return{
        "battery_voltage": battery_voltage, 
        "motor_temperature": motor_temperature, 
        "throttle": throttle,
        "system_status": "OK"
    }

#test section, calls function and prints results

if __name__ == "__main__":
    data = get_telemetry()
    print(data)