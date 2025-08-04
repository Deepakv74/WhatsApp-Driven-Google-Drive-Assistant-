from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os

SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate_drive():
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    creds = flow.run_local_server(port=0)
    service = build("drive", "v3", credentials=creds)
    return service

service = authenticate_drive()

def list_files(folder_name):
    query = f"name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder'"
    folders = service.files().list(q=query).execute().get('files', [])

    if not folders:
        return "Folder not found."

    folder_id = folders[0]['id']
    query = f"'{folder_id}' in parents"
    files = service.files().list(q=query).execute().get('files', [])
    
    return "\n".join(f['name'] for f in files) or "No files found."

def delete_file(file_path):
    # Simplified logic: requires full file ID or exact name + folder
    return "Delete requires confirmation in future build."

def move_file(src, dest):
    return "Move feature coming soon."

def summarize_folder(folder_name):
    # You’ll add extraction + OpenAI here
    return f"Summary for {folder_name} coming soon."