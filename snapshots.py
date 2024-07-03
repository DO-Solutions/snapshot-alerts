import json
from datetime import datetime, timedelta
import requests

# Load the JSON data from the file
with open('snapshots.json', 'r') as file:
    snapshots = json.load(file)

# Define the webhook URL
webhook_url = 'https://webhook.site/3b2d5a8f-7d76-40b2-9b24-77bc539ead98'  # Replace with your actual webhook URL

# Define the time threshold (30 days ago)
time_threshold = datetime.utcnow() - timedelta(days=30)

# Iterate over the snapshots
for snapshot in snapshots:
    created_at = datetime.strptime(snapshot['created_at'], '%Y-%m-%dT%H:%M:%SZ')
    
    # Check if the snapshot is older than 30 days
    if created_at < time_threshold:
        # Prepare the alert data
        alert_data = {
            'resource_id': snapshot['resource_id'],
            'message': f"Snapshot {snapshot['id']} is older than 30 days."
        }
        
        # Send the POST request to the webhook
        response = requests.post(webhook_url, json=alert_data)
        
        # Print the response status
        if response.status_code == 200:
            print(f"Alert sent for snapshot {snapshot['id']}")
        else:
            print(f"Failed to send alert for snapshot {snapshot['id']}: {response.status_code}")