from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]
SERVICE_ACCOUNT_FILE = "service_account.json"

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

drive_service = build("drive", "v3", credentials=credentials)


def search_drive_files(q: str):
    results = drive_service.files().list(
        q=q,
        pageSize=20,
        fields="files(id, name, mimeType, modifiedTime, webViewLink)"
    ).execute()

    return results.get("files", [])