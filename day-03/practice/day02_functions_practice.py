import requests
import json

api_url = "https://api.thecatapi.com/v1/images/0XYvRd7oD"
processed_data = {} # dictionary to store processed data

print("Fetching data from the API...", api_url) # server URL (API)
try:
    response = requests.get(api_url)    # send GET request to the API
    response.raise_for_status()  # raises exception for bad status codes
    print("Response Status Code:", response.status_code) # 200 means OK
    print("Response JSON Data:", response.json(), "\n") # print the json data
    print(f"The JSON data is below: ")
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")
    exit(1) 

def process_cat_api_data(response_json):
    processed_data = {} # dictionary to store processed data
    
    for key, value in response_json.items():   # Check multiple key-value pairs in the response, more than one conditions
        if key == "id" or key == "url":
            print(f"{key}: {value}") # print the key-value pairs of the details in the response

            processed_data[key] = value  # save the key-value pairs
            
        if key == "breeds":
            try:
                print("wikipedia_url:", value[0]["wikipedia_url"])
                print("vcahospitals_url:", value[0]["vcahospitals_url"])   
                
                processed_data["wikipedia_url"] = value[0]["wikipedia_url"] 
                processed_data["vcahospitals_url"] = value[0]["vcahospitals_url"]
            except (IndexError, KeyError) as e:
                print(f"Error processing breeds data: {e}")
    
    return processed_data

# saves the processed data into a file
try:
    with open("cat_api_data.json", "w") as json_file:
        json.dump(process_cat_api_data(response.json()), json_file, indent=4)   # call the function to process and save data
    print("\nCat API data has been saved to 'cat_api_data.json'")
except IOError as e:
    print(f"Error saving data to file: {e}")