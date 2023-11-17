from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os.path

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]

def main():
    creds = None
    # Load existing credentials from token.json if available
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print("Please authorize the application.")
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    # Authorize using credentials
    service = build('gmail', 'v1', credentials=creds)

    # Get label ID for 'Test_Label'
    response = service.users().labels().list(userId='me').execute()
    labels = response.get('labels', [])
    test_label_id = None
    for label in labels:
        if label['name'] == 'Test_Label':
            test_label_id = label['id']
            break

    if not test_label_id:
        print("Label 'Test_Label' not found.")
        exit()

    # Get messages from the specified sender (no-reply@accounts.google.com)
    response = service.users().messages().list(userId='me', q='from:no-reply@accounts.google.com').execute()

    # Move matching messages to the 'Test_Label' label and archive
    if 'messages' in response:
        for message in response['messages']:
            # Get current labels on the message
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            current_labels = msg['labelIds']

            # Add the 'Test_Label' to the message and remove 'INBOX' label
            current_labels.append(test_label_id)
            current_labels.remove('INBOX')  # Remove 'INBOX' label to archive
            service.users().messages().modify(userId='me', id=message['id'], body={'removeLabelIds': ['INBOX'], 'addLabelIds': [test_label_id]}).execute()

    print("Done moving emails to 'Test_Label' and archiving.")

if __name__ == "__main__":
    main()
