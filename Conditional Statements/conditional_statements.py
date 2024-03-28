# if
# if else
# if elif -> else if

# Task

def calculate_distance(route_info: dict) -> str:
    if (route_info.get("distance")) and (isinstance(route_info.get("distance"), float)):
        distance = route_info.get("distance")
        return f"Distance to your destination is {distance}"
    elif (route_info.get("speed")) and (isinstance(route_info.get("speed"), float)) and (
            route_info.get("time")) and (isinstance(route_info.get("time"), float)):
        speed = route_info.get("speed")
        time = route_info.get("time")
        distance = speed * time
        return f"Distance to your destination is {distance}"
    else:
        return "No distance info available"


route1 = {
    "distance": 40.5
}
route2 = {
    "speed": 128.6,
    "time": 2.5
}
route3 = {
    "speed": 200.1
}
route4 = {
    "time": 3.5
}

print(calculate_distance(route1))
print(calculate_distance(route2))
print(calculate_distance(route3))
print(calculate_distance(route4))
