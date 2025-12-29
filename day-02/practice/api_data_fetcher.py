import requests
import json

api_url = "https://api.thecatapi.com/v1/images/0XYvRd7oD"
processed_data = {} # dictionary to store processed data

print("Fetching data from the API...", api_url) # server URL (API)
response = requests.get(api_url)    # send GET request to the API
print("Response Status Code:", response.status_code) # 200 means OK
print("Response JSON Data:", response.json(), "\n") # print the json data
print(f"The JSON data is below: ") 

# Check multiple key-value pairs in the response, more than one conditions
for key, value in response.json().items():
    if key == "id" or key == "url":
        print(f"{key}: {value}") # print the key-value pairs of the details in the response

        processed_data[key] = value   # save
        
    if key == "breeds":
        print("wikipedia_url:", value[0]["wikipedia_url"])
        print("vcahospitals_url:", value[0]["vcahospitals_url"])   
        
        processed_data["wikipedia_url"] = value[0]["wikipedia_url"]
        processed_data["vcahospitals_url"] = value[0]["vcahospitals_url"]

# saves the processed data into a file
with open("cat_api_data.json", "w") as json_file:
    json.dump(processed_data, json_file, indent=4)

print("\nCat API data has been saved to 'cat_api_data.json'")