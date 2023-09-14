import unittest
from weather_api import WeatherAPI

class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = "5e7523329fe5639e8087bac0ea8f1d37"
        self.weather_api = WeatherAPI(self.api_key)

    def test_get_temperature_valid_city(self):
        # Test with a valid city and country code
        temperature = self.weather_api.get_temperature("London", "UK")
        self.assertIsInstance(temperature, (int, float))  # Check if the temperature is a number

    def test_get_temperature_invalid_city(self):
        # Test with an invalid city (should return None)
        temperature = self.weather_api.get_temperature("NonExistentCity", "XX")
        self.assertIsNone(temperature)

    def test_get_temperature_empty_city(self):
        # Test with an empty city name (should return None)
        temperature = self.weather_api.get_temperature("", "FR")
        self.assertIsNone(temperature)

    def test_get_temperature_empty_country_code(self):
        # Test with an empty country code (should return None)
        temperature = self.weather_api.get_temperature("Berlin", "")
        self.assertIsNone(temperature)

    #TODO
    # def test_get_temperature_invalid_country_code(self):
    #     # Test with an invalid country code (should return None)
    #     temperature = self.weather_api.get_temperature("Paris", "INVALID")
    #     self.assertIsNone(temperature)


if __name__ == '__main__':
    unittest.main()
