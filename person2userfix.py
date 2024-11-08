
import csv
import requests
import logging
import getpass

# Configure logging
logging.basicConfig(filename='api_requests.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_api_details():
    base_url = input("Enter the base URL (e.g., 'xyz.elsevierpure.com'): ")
    api_key = getpass.getpass("Enter the API key: ")  # Securely input the API key
    return base_url, api_key

def send_request(personuuid, useruuid, api_url, headers):
    url = f"{api_url}{personuuid}"
    data = {
        "user": {
            "systemName": "User",
            "uuid": useruuid
        }
    }
    response = requests.put(url, headers=headers, json=data)
    return response

def process_csv(file_path, api_url, headers):
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        
        # Print CSV headers for debugging
        headers_csv = reader.fieldnames
        print("CSV Headers:", headers_csv)
        logging.info(f"CSV Headers: {headers_csv}")

        for row in reader:
            print("CSV Row:", row)  # Debugging line to print each row
            try:
                personuuid = row['personuuid']
                useruuid = row['useruuid']
                response = send_request(personuuid, useruuid, api_url, headers)
                log_response(personuuid, useruuid, response)
            except KeyError as e:
                logging.error(f"Missing key in CSV file: {e}")
                print(f"Missing key in CSV file: {e}")

def log_response(personuuid, useruuid, response):
    if response.status_code == 200:
        logging.info(f"Successfully updated personuuid: {personuuid} with useruuid: {useruuid}")
    else:
        logging.error(f"Failed to update personuuid: {personuuid} with useruuid: {useruuid}. Status Code: {response.status_code}. Response: {response.text}")

if __name__ == "__main__":
    # Get API details from the user
    base_url, api_key = get_api_details()
    
    # Construct the API URL and headers
    API_URL = f"https://{base_url}/ws/api/persons/"
    HEADERS = {
        "accept": "application/json",
        "api-key": api_key,
        "content-type": "application/json"
    }
    
    # Specify the CSV file path
    csv_file_path = "personuserfix.csv"
    
    # Process the CSV file
    process_csv(csv_file_path, API_URL, HEADERS)
