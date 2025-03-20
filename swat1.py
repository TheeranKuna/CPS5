import csv

class Valve:
    def __init__(self):
        self.state = "closed"
        self.transition_counter = 0

    def open(self):
        if self.state == "closed":
            self.state = "transitioning"
            self.transition_counter = 4  # Simulate 4 minutes transition

    def close(self):
        if self.state == "open":
            self.state = "transitioning"
            self.transition_counter = 4  # Simulate 4 minutes transition

    def update_state(self):
        if self.state == "transitioning":
            self.transition_counter -= 1
            if self.transition_counter <= 0:
                if self.state == "transitioning":
                    self.state = "open" if self.state == "transitioning" and self.transition_counter == 0 else "closed"

    def get_state(self):
        return self.state

class Pump:
    def __init__(self):
        self.state = "off"
        self.transition_counter = 0

    def turn_on(self):
        if self.state == "off":
            self.state = "transitioning"
            self.transition_counter = 4  # Simulate 4 minutes transition

    def turn_off(self):
        if self.state == "on":
            self.state = "transitioning"
            self.transition_counter = 4  # Simulate 4 minutes transition

    def update_state(self):
        if self.state == "transitioning":
            self.transition_counter -= 1
            if self.transition_counter <= 0:
                if self.state == "transitioning":
                    self.state = "on" if self.state == "transitioning" and self.transition_counter == 0 else "off"

    def get_state(self):
        return self.state

class Tank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_level = 0
        self.valve = Valve()
        self.pump = Pump()

    def fill(self):
        if self.valve.get_state() == "open":
            if self.current_level < self.capacity:
                self.current_level += 29  # Simulate filling the tank at a rate of 29/min
                if self.current_level > self.capacity:
                    self.current_level = self.capacity
            else:
                print("Tank is full")

    def drain(self):
        if self.pump.get_state() == "on":
            if self.current_level > 0:
                self.current_level -= 28  # Simulate draining the tank at a rate of 28/min
                if self.current_level < 0:
                    self.current_level = 0
            else:
                print("Tank is empty")

    def get_level(self):
        return self.current_level

    def get_level_indicator(self):
        if self.current_level == 0:
            return "Empty"
        elif 0 < self.current_level <= 300:
            return "LL"
        elif 301 <= self.current_level <= 500:
            return "L"
        elif 501 <= self.current_level <= 800:
            return "H"
        elif 801 <= self.current_level <= 1000:
            return "HH"
        else:
            return "Danger"

    def update_valve_state(self):
        if self.current_level <= 500:
            self.valve.open()
        elif self.current_level >= 801:
            self.valve.close()
        self.valve.update_state()

    def update_pump_state(self):
        if 501 <= self.current_level <= 800:
            self.pump.turn_on()
        elif self.current_level >= 801:
            self.pump.turn_on()
            self.valve.close()
        else:
            self.pump.turn_off()
        self.pump.update_state()

# Example usage
tank = Tank(capacity=1200)
print(tank.get_level_indicator())  # Output: Empty

# Open the CSV file in write mode
with open('c:\\Users\\User\\CPS5\\tank_level.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "Level", "Indicator", "Valve", "Pump"])

    # Simulate tank operation
    for time in range(1000):  # Simulate 50 minutes of operation
        tank.fill()
        tank.drain()
        tank.update_valve_state()
        tank.update_pump_state()
        writer.writerow([time, tank.get_level(), tank.get_level_indicator(), tank.valve.get_state(), tank.pump.get_state()])
        print(f"Time: {time}, Level: {tank.get_level()}, Indicator: {tank.get_level_indicator()}, Valve: {tank.valve.get_state()}, Pump: {tank.pump.get_state()}")