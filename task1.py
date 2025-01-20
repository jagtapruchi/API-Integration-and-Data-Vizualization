import requests
import matplotlib.pyplot as plt
import os
os.chdir("C:\\Users\\RUCHI\\Codetech IT\\")

#API for air pollution
my_api_key = "58c1d30a444cd0e1f4d41f22eda678f0"

#latitudinal and longitudinal values of India
latitude = 20.5937
longitude = 78.9629

def fetch_air_pollution_data(lat,lon,api_key):
    url = "http://api.openweathermap.org/data/2.5/air_pollution"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key   
    }  #parameters as queries
    try:
        response = requests.get(url,params=params)
        response.raise_for_status()  #exception to be raised in failure of receiving data
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    

data = fetch_air_pollution_data(latitude,longitude,my_api_key)
if data is None:      #error handling
    print("Failed to receive Air Pollution data.\n Please check your connection or API key")
else:
    components = data["list"][0]["components"]

    pollutants = list(components.keys())
    values = list(components.values())

    #sorting data into descending order
    sorted_data = sorted(zip(values, pollutants), reverse=True)
    values, pollutants = zip(*sorted_data)

    # Explode smaller segments for clarity
    explode = [0.1 if value < max(values)*0.1 else 0 for value in values]  

    # Define a function to filter small percentages
    def autopct_filter(pct):
        return f'{pct:.1f}%' if pct >= 1 else ''

    plt.figure(figsize=(10,10))   #pie chart size

    plt.pie(values, labels=None, startangle=140,colors=plt.cm.Paired.colors,    pctdistance=1.07, explode=explode, autopct = autopct_filter)

    plt.title("Air Pollution Component Distribution",fontsize=25)

    #legend shows the values 
    plt.legend(loc="lower left",labels=[f"{pollutant}: {value} µg/m³" for   pollutant,value in zip(pollutants,values)],fontsize=9)

    plt.tight_layout()

    plt.show()