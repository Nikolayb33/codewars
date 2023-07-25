
obj = {
    "gas_station1": {"price": 1.5, "distance": 50}, 
    "gas_station2": {"price": 2.0, "distance": 75}
}
#distance: distance between you and the gasstation in km

costs_gas_station1 = 48.1
costs_gas_station2 = 72.2

# print(type(costs_gas_station1))

currentFuel = 35
#currentFuel: your current fuel in l 
fuelConsumption = 7.5
#fuelConsumption: how much your car consumes in l/100km

distance = 61
# distance between you and gas station
# if gas_station[x:[y:b]]




def gas_station(obj, currentFuel, fuelConsumption):
    if obj["gas_station1"]["price"] < obj["gas_station2"]["price"] and obj["gas_staion1"]["distance"] > currentFuel/fuelConsumption:
        return "gas_station1"
    elif obj["gas_station1"]["price"] < obj["gas_station2"]["price"] and obj["gas_station1"]["distance"] < currentFuel/fuelConsumption:
        return "gas_station2"
    elif obj["gas_station1"]["price"] > obj["gas_station2"]["price"] and obj[""] 
    # pass #happy coding ^.^