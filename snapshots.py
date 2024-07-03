import json
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# Load JSON data from snapshots.json
with open('snapshots.json', 'r') as file:
    snapshots = json.load(file)

# Get current date and time
current_date = datetime.utcnow()

# List to hold outdated snapshots
outdated_snapshots = []

# Check each snapshot to see if it's older than 30 days
for snapshot in snapshots:
    created_at = datetime.strptime(snapshot['created_at'], '%Y-%m-%dT%H:%M:%SZ')
    if (current_date - created_at).days > 30:
        outdated_snapshots.append(snapshot['resource_id'])

# If there are outdated snapshots, send an email notification
if outdated_snapshots:
    # Email settings
    smtp_server = 'smtp.fastmail.com'
    smtp_port = 465
    smtp_user = 'jack@jkpe.net'
    smtp_password = '6U2R665Q4A2J5S6P'
    sender_email = 'jack@jkpe.net'
    recipient_email = 'jack@jkpe.net'
    subject = 'Outdated Snapshots Alert'
    
    # Create the email content
    body = 'The following snapshots are older than 30 days:\n\n' + '\n'.join(outdated_snapshots)
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')
else:
    print('No outdated snapshots found.')