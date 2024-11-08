
# Person to user Script

This Python script can be used to relate Persons to Users in Pure. It reads UUIDs from a CSV file and updates person records. 

## Requirements

- Python 3.x
- `requests` library

To install the required libraries, run:
```bash
pip install requests
```

## Usage

### 1. Prepare Your CSV File

Ensure your CSV file (`personuserfix.csv` by default) is formatted with the following columns:
- `personuuid`: UUID of the person to update.
- `useruuid`: UUID of the corresponding user

Use `;` as the delimiter (or change to ,)

### 2. Run the Script

1. Clone this repository.
2. Run the script from the command line:
   ```bash
   python person2userfix.py
   ```
3. Enter the required details when prompted:
   - **Base URL**: The base URL of the API (e.g., `xyz.elsevierpure.com`).
   - **API Key**: Your API key for authentication.

### Example Usage

After running the script, you’ll be prompted for the base URL and API key. Once provided, the script will read data from `personuserfix.csv` and send update requests for each entry. The results of each request will be logged in `api_requests.log`.

### Logging

All API responses and potential errors are logged in `api_requests.log`, located in the same directory as the script. This log file includes:
- Success messages for each updated person UUID.
- Errors, including HTTP status codes and response messages, in case of failed requests.

## Script Structure

- `get_api_details()`: Prompts for base URL and API key.
- `send_request()`: Constructs and sends a `PUT` request to the API.
- `process_csv()`: Reads the CSV file, iterates over each row, and calls `send_request` for each entry.
- `log_response()`: Logs the result of each API request.

## Error Handling

- Logs errors for missing keys in the CSV file.
- Logs HTTP errors with the response details.

## Example CSV File

```csv
personuuid;useruuid
123e4567-e89b-12d3-a456-426614174000;456e4567-e89b-12d3-a456-426614174111
789e4567-e89b-12d3-a456-426614174222;123e4567-e89b-12d3-a456-426614174333
```

## License

This project is licensed under the MIT License.
