from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Define your OAuth 2.0 credentials
client_id = '306617801984-pfvi3hs7fijjrhmoa73k6ku8voo5n162.apps.googleusercontent.com'
client_secret = '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'
refresh_token = '1//05SuMJepy2YcfCgYIARAAGAUSNwF-L9IrlVF0120O23soQSbIR5Ldb1MgtLMfJjxtUhSuPb-nFSsK5h9IjyJ_3hwted8cX6T9yqY'




# Create OAuth 2.0 credentials object
credentials = Credentials(
    None,
    refresh_token=refresh_token,
    token_uri='https://accounts.google.com/o/oauth2/token',
    client_id=client_id,
    client_secret=client_secret
)

# Authorize using credentials
service = build('gmail', 'v1', credentials=credentials)

# Define the label name you want to create
new_label_name = 'Test_Label2'

# Create label payload
label_payload = {'labelListVisibility': 'labelShow', 'messageListVisibility': 'show', 'name': new_label_name}

# Create the label using Gmail API
created_label = service.users().labels().create(userId='me', body=label_payload).execute()

print(f"Label '{created_label['name']}' created successfully!")
