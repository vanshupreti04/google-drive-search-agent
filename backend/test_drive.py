from google.oauth2 import service_account
from googleapiclient.discovery import build

# Google Drive API scope
SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]

# Service account JSON file
SERVICE_ACCOUNT_FILE = "service_account.json"

# Authenticate
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

# Build Drive service
service = build("drive", "v3", credentials=credentials)

# Fetch files
results = service.files().list(
    q="trashed=false",
    pageSize=50,
    fields="files(id, name, mimeType, modifiedTime, webViewLink)"
).execute()

files = results.get("files", [])

# Display results
if not files:
    print("No files found.")
else:
    print("\nFiles Found:\n")

    for file in files:
        print("----------------------------")
        print("Name       :", file.get("name"))
        print("Type       :", file.get("mimeType"))
        print("Modified   :", file.get("modifiedTime"))
        print("Drive Link :", file.get("webViewLink"))