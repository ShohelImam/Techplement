import argparse
import time
import requests

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.favorites = set()

    def get_weather_by_city_name(self, city_name):
        url = f"{self.base_url}?q={city_name}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def add_favorite(self, city_name):
        self.favorites.add(city_name)

    def remove_favorite(self, city_name):
        if city_name in self.favorites:
            self.favorites.remove(city_name)

    def list_favorites(self):
        return self.favorites

def main():
    parser = argparse.ArgumentParser(description="Command-line Weather Application")
    parser.add_argument("city", nargs="?", help="City name to check weather for")
    parser.add_argument("--add-favorite", help="Add city to favorites")
    parser.add_argument("--remove-favorite", help="Remove city from favorites")
    parser.add_argument("--list-favorites", action="store_true", help="List favorite cities")
    args = parser.parse_args()

    api_key = "3723b6f79d243fefc1472b7a7d7279ac"  # API key
    app = WeatherApp(api_key)

    if args.city:
        weather_data = app.get_weather_by_city_name(args.city)
        if weather_data:
            print(f"Weather for {args.city}:")
            print(f"Description: {weather_data['weather'][0]['description']}")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Humidity: {weather_data['main']['humidity']}%")
        else:
            print("Failed to fetch weather data for the provided city.")
    
    if args.add_favorite:
        app.add_favorite(args.add_favorite)
        print(f"{args.add_favorite} added to favorites.")

    if args.remove_favorite:
        app.remove_favorite(args.remove_favorite)
        print(f"{args.remove_favorite} removed from favorites.")

    if args.list_favorites:
        favorites = app.list_favorites()
        if favorites:
            print("Favorite Cities:")
            for city in favorites:
                print(city)
        else:
            print("No favorite cities.")

if __name__ == "__main__":
    main()
