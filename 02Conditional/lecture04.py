# You're building a smart thermostat alert system:
# . If the device_status is "active"
# . And temperature > 35 -> Warn: "High temperature alert!"
# · Else: "Temperature normal"
# · If device is off -> "Device is offline"
device_statue = input("on/off: ").lower()
if device_statue == "on":
    print("device is active now")
    set_temp = int(input("set your temperature : "))
    if set_temp > 35:
        print("Warn: High temperature alert!")
    else:
        print("Temperature normal")
else:
    print("device is not active")
