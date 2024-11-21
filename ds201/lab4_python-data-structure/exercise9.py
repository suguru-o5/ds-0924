weather = {
    "Monday": {"temperature": 20, "humidity": 60},
    "Tuesday": {"temperature": 22, "humidity": 55},
    "Wednesday": {"temperature": 19, "humidity": 65},
    "Thursday": {"temperature": 23, "humidity": 50},
    "Friday": {"temperature": 21, "humidity": 70},
}

def calculate_highest_and_lowest(nested_dictionary: dict, key: any):
    temp_list = []
    for detail in nested_dictionary.values():
        temp_list.append(detail[key])
    return {"highest": max(temp_list), "lowest": min(temp_list)}

# 1. Print the weather details for each day.
for day, detail in weather.items():
    print(
        f"Day: {day}, Temperature: {detail['temperature']}, Humidity: {detail['humidity']}"
    )

# 2. Find and print the day with the highest temperature.
highest_and_lowest = calculate_highest_and_lowest(weather, "temperature")
for day, detail in weather.items():
    if detail["temperature"] == highest_and_lowest["highest"]:
        print(day)

# 3. Find and print the day with the lowest humidity.
highest_and_lowest = calculate_highest_and_lowest(weather, "humidity")
for day, detail in weather.items():
    if detail["humidity"] == highest_and_lowest["lowest"]:
        print(day)

# 4. Update the temperature of "Wednesday" to 25 and print the updated weather data.
weather["Wednesday"]["temperature"] = 25
print(weather)

# 5. Add weather data for "Saturday" with temperature 24 and humidity 60 to the dictionary and print the updated weather data.
weather["Saturday"] = {"temperature": 24, "humidity": 60}
print(weather)