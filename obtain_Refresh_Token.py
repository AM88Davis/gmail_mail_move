from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_ID = '306617801984-pfvi3hs7fijjrhmoa73k6ku8voo5n162.apps.googleusercontent.com'
CLIENT_SECRET = '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'
SCOPES = ['https://www.googleapis.com/auth/gmail.labels']  # Modify scopes as needed

flow = InstalledAppFlow.from_client_secrets_file(
    'credentials.json',
    scopes=SCOPES,
    redirect_uri='urn:ietf:wg:oauth:2.0:oob'  # For local testing
)

flow.run_local_server(port=8080)

credentials = flow.credentials
print(f"Refresh token: {credentials.refresh_token}")
