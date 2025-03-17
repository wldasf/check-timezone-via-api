import urllib.request, json, os, datetime, sys

def get_local_time(lat, long):
    url = f"http://api.geonames.org/timezoneJSON?lat={lat}&lng={long}&username=wldasf"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        return data["time"]
    
def task(lat, long):
    time_str = get_local_time(lat, long)
    hour = int(time_str.split(" ")[1].split(":")[0])
    images = os.listdir("images")

    if 6 <= hour < 7: prefix = "sunrise"
    elif 7 <= hour < 12: prefix = "morning"
    elif 12 <= hour < 17: prefix = "noon"
    elif 17 <= hour < 19: prefix = "sunset"
    elif 19 <= hour < 24: prefix = "evening"
    elif 0 <= hour < 6: prefix = "night"

    selected_images = [img for img in images if img.startswith(prefix)]
    sys.stdout.write(selected_images[0] + '\n')
    
task(31.9544, 35.9106)
task(-37.8136, 144.9631)
task(-51.63092, -69.2247)
task(35.6995, 139.7714)
