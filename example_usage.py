"""
Example usage of the Astronomy Calculator API.

This script demonstrates how to interact with the astronomy calculator
endpoints. Make sure the Flask server is running before executing this script.

Run the server with: python app.py
Then run this script with: python example_usage.py
"""

import requests
import json


BASE_URL = "http://localhost:5000"


def print_response(title, response):
    """Pretty print an API response."""
    print(f"\n{'='*60}")
    print(f"{title}")
    print('='*60)
    print(json.dumps(response.json(), indent=2))
    print()


def main():
    """
    Run example API calls.
    Is AI coding itself yet?
    """
    
    print("Astronomy Calculator API Examples")
    print("=" * 60)
    
    # 1. Get API info
    response = requests.get(f"{BASE_URL}/")
    print_response("1. API Information", response)
    
    # 2. Get current Sun position
    response = requests.get(f"{BASE_URL}/sun")
    print_response("2. Current Sun Position", response)
    
    # 3. Convert absolute magnitude to apparent magnitude
    # Example: The Sun has absolute magnitude 4.83, at 10 parsecs distance
    response = requests.get(
        f"{BASE_URL}/magnitude/absolute-to-apparent",
        params={'M': 4.83, 'distance': 10}
    )
    print_response("3. Absolute to Apparent Magnitude (Sun at 10pc)", response)
    
    # 4. Convert apparent magnitude to absolute magnitude
    # Example: The Sun has apparent magnitude -26.74 at ~0.0000158 parsecs
    response = requests.get(
        f"{BASE_URL}/magnitude/apparent-to-absolute",
        params={'m': -26.74, 'distance': 0.0000158}
    )
    print_response("4. Apparent to Absolute Magnitude (Sun from Earth)", response)
    
    # 5. Calculate distance from magnitudes
    # Example: Calculate Sun's distance using its apparent and absolute magnitudes
    response = requests.get(
        f"{BASE_URL}/magnitude/distance",
        params={'m': -26.74, 'M': 4.83}
    )
    print_response("5. Distance Calculation (Sun)", response)
    
    # 6. Calculate brightness ratio
    # Example: A star that is 5 magnitudes brighter
    response = requests.get(
        f"{BASE_URL}/magnitude/brightness-ratio",
        params={'mag_diff': 5}
    )
    print_response("6. Brightness Ratio (5 magnitude difference)", response)
    
    # 7. Error handling example
    response = requests.get(
        f"{BASE_URL}/magnitude/absolute-to-apparent",
        params={'M': 'invalid', 'distance': 10}
    )
    print_response("7. Error Handling Example (invalid parameter)", response)


if __name__ == '__main__':
    try:
        main()
    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect to the API server.")
        print("Make sure the Flask server is running with: python app.py")
    except Exception as e:
        print(f"\nError: {e}")
