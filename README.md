# Snapshot Alert Script

## Overview

This Python script checks the creation date of snapshots listed in a JSON file (`snapshots.json`). If any snapshot is older than 30 days, it sends a POST request to a specified webhook URL, alerting you with the snapshot's resource ID.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone or download this repository to your local machine.
2. Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/downloads/).
3. Install the `requests` library if you don't have it already. You can install it using pip:

    ```bash
    pip install requests
    ```

## Usage

1. **Prepare the JSON File**:
   - You can retrieve the JSON data using the `doctl` command line tool. Run the following command to get the list of snapshots and save it to a file named `snapshots.json`:

     ```bash
     doctl compute snapshot list --output json > snapshots.json
     ```

   - Ensure the `snapshots.json` file is in the same directory as the script. The file should contain snapshot data in the following format:

     ```json
     [
       {
         "id": "129721643",
         "name": "opnsense-lon1-01-1680180362752",
         "resource_id": "348280077",
         "resource_type": "droplet",
         "regions": ["lon1", "ams3"],
         "min_disk_size": 50,
         "size_gigabytes": 2.96,
         "created_at": "2023-03-30T12:46:04Z"
       },
       {
         "id": "141692420",
         "name": "outl-lon1-01 2023-10-04",
         "resource_id": "375470875",
         "resource_type": "droplet",
         "regions": ["lon1", "ams3"],
         "min_disk_size": 80,
         "size_gigabytes": 2.07,
         "created_at": "2023-10-04T04:56:58Z"
       }
     ]
     ```

2. **Set the Webhook URL**:
   - Open the script file (`snapshot_alert.py`) and replace `'https://example.com/webhook'` with your actual webhook URL.

3. **Run the Script**:
   - Execute the script using Python:

     ```bash
     python snapshot_alert.py
     ```

4. **Check the Output**:
   - The script will check each snapshot's `created_at` date. If a snapshot is older than 30 days, it will send an alert to the webhook and print the result.

## Script Explanation

The script performs the following steps:

1. **Loads the JSON Data**:
   - Reads the `snapshots.json` file and parses its content.

2. **Defines the Time Threshold**:
   - Calculates a date that is 30 days before the current date and time.

3. **Iterates Over Snapshots**:
   - For each snapshot, it checks if the `created_at` date is older than the time threshold.

4. **Sends Alerts**:
   - If a snapshot is older than 30 days, sends a POST request to the webhook URL with the snapshot's `resource_id` and an alert message.

## Example Output

```
Alert sent for snapshot 129721643
Alert sent for snapshot 141692420
```

If the alert fails to send, you will see:

```
Failed to send alert for snapshot 129721643: <HTTP status code>
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Acknowledgements

This script uses the following libraries:
- [Requests](https://docs.python-requests.org/en/master/): HTTP library for Python.

## Contact

If you wish to learn more about DigitalOcean's services, you are welcome to reach out to the sales team at [sales@digitalocean.com](mailto:sales@digitalocean.com). A global team of talented engineers will be happy to provide assistance.
