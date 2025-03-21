import requests
import json
latitude = input("enter the latitude")
longitude = input("enter the longitude")
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
response = requests.get(url)
if response.status_code== 200:
   data = response.json()
   weather = data["current_weather"]
   temperature = weather["temperature"]
   windspeed = weather["windspeed"]
   weather_code = weather["weathercode"]
   time = weather["time"]
   is_day = weather["is_day"]
   
      
   winddirection = weather["winddirection"]
   
   def dn():
      if is_day == 0:
         print("its night")
      else:
         print("its day")
      
      
   
   print(f"time :{time}")
   print(f"Tempreture : {temperature} °C")
   print(f"wind speed : {windspeed} km/h" )
   print(f"weather code : {weather_code} " )
   print(f"wind Direction : {winddirection}")
   

   # print(json.dumps(data , indent= 4))
else:
   print(f"error : {response.status_code}")
   
