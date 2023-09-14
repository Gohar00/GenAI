from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from weather_api import WeatherAPI

# Define a custom request handler that extends BaseHTTPRequestHandler
class WeatherRequestHandler(BaseHTTPRequestHandler):

    # Handle GET requests
    def do_GET(self):
        if self.path.startswith('/get_temperature'):
            # Parse the query parameters from the URL
            query_params = self.path.split('?')[1]
            params_dict = dict(param.split('=') for param in query_params.split('&'))
            city = params_dict.get('city', '')
            country_code = params_dict.get('country_code', '')

            # Initialize WeatherAPI object with API key
            api_key = '5e7523329fe5639e8087bac0ea8f1d37'
            weather_api = WeatherAPI(api_key)

            # Get the temperature using WeatherAPI class
            temperature = weather_api.get_temperature(city, country_code)

            # Prepare the response JSON
            response_data = {'temperature': temperature}

            # Send a 200 OK response with JSON content type
            self.send_response(200)
            self.send_header('Content_type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())
        else:
            # Send a 404 Not Found response for unrecognized paths
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 - Not Found')

# Define a function to run the HTTP server
def run_server():
    try:
        # Specify the server address (host and port)
        server_address = ('', 8000)

        # Create the HTTP server with the custom request handler
        httpd = HTTPServer(server_address, WeatherRequestHandler)
        print('Starting server...')

        # Start the server, and it will listen for requests
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Server stopped.')

# Start the server if this script is executed
if __name__ == '__main__':
    run_server()
