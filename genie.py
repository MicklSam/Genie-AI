import requests  # Import the requests library to make HTTP requests
import json      # Import the json library to work with JSON data
import sys       # Import the sys module to access command line arguments

# Replace with your actual API key
API_KEY = "AIzaSyCfc0ej_s8AKNiIFccX0P0Vk_gjvcsxPak"

# Check if there is any command line argument provided
if len(sys.argv) > 1:
    user_input = sys.argv[1]  # Get the input text from command line argument
else:
    print("No input text provided.")
    exit()  # Exit the program if no input text is provided

# Define the URL of the API endpoint
url = f"https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key={API_KEY}"

# Prepare the data to be sent to the API
data = {
    "prompt": {
        "text": user_input  # The input text to generate continuation from
    }
}

# Set headers with content type as JSON
headers = {"Content-Type": "application/json"}

# Send POST request with headers and data to the API endpoint
response = requests.post(url, headers=headers, json=data)

# Check for successful response
if response.status_code == 200:
    try:
        response_data = response.json()  # Parse the JSON response
        # Fetch the generated content from the response
        generated_text = response_data.get('candidates', [{}])[0].get('output', 'No output found.')

        # Check if the response contains a numerical result
        if generated_text.strip().isdigit():
            print("Genie: I’m sorry, I only answer bash specific questions.")
        else:
            # Print the generated text
            print(f"Genie: {generated_text.strip()}")
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"Error parsing response: {e}")  # Handle JSON parsing errors
else:
    print(f"Error: {response.status_code} - {response.text}")  # Print error if response status code is not 200
