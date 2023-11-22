from google.oauth2.credentials import Credentials 
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import os.path

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]

def main():
    creds = None



    # Variable definitions
    # NOTE: Comment out the credential file pertaining to the gmail mailbox that you are trying to change.

    ## credentialFile = "credentials_anthonycardenemail.json" # anthonycardenemail@gmail.com email credentails
    ## jsonToken = "token_anthonycardenemail.json" # anthonycardenemail@gmail.com email credentails

    credentialFile = "credentials_am88davis.json" # am88davis@gmail.com email credentials
    jsonToken = "token_am88davis.json" # am88davis@gmail.com email credentials

    labelName = "Robinhood"
    sender = 'from:*@robinhood.com'
    



    # Load existing credentials from token.json if available
    # Checks for the jsonToken. Creates the token if it's not found.
    if os.path.exists(jsonToken):
        creds = Credentials.from_authorized_user_file(jsonToken, SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print("Please authorize the application.")
            flow = InstalledAppFlow.from_client_secrets_file(credentialFile, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        # NOTE: go to the directory and CHANGE the token name to whatever the email is that you are using.
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    # Authorize using credentials
    service = build('gmail', 'v1', credentials=creds)

    # Get label ID for labelName
    response = service.users().labels().list(userId='me').execute()
    labels = response.get('labels', [])
    test_label_id = None
    for label in labels:
        if label['name'] == labelName:
            test_label_id = label['id']
            break

    if not test_label_id:
        print(f"Label {labelName} not found.")
        exit()

    # Get messages from the specified sender (no-reply@accounts.google.com)
    ### TO DO: Make the q = a variable
    response = service.users().messages().list(userId='me', q=sender).execute()

    # Move matching messages to the labelName label and archive
  
    if 'messages' in response:
        for message in response['messages']:
            # Get current labels on the message
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            current_labels = msg['labelIds']

            # Add the labelName to the message and remove 'INBOX' label
            current_labels.append(test_label_id)
            current_labels.remove('INBOX')  # Remove 'INBOX' label to archive
            service.users().messages().modify(userId='me', id=message['id'], body={'removeLabelIds': ['INBOX'], 'addLabelIds': [test_label_id]}).execute()

    print(f"Done moving emails to {labelName} and archiving.")

if __name__ == "__main__":
    main()
