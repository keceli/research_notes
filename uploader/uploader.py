import argparse
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
import sys

def get_input(prompt):
    return input(prompt)

def upload_file(file_path, folder_id, service):
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_path, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"File {file_path} uploaded successfully, File ID: {file.get('id')}")

def main():
    parser = argparse.ArgumentParser(description='Upload files to a Google Drive folder.')
    parser.add_argument('--service_account_file', type=str, default='/home/keceli/soft/spring-bonfire-381703-87307d8befde.json', help='Path to the service account key file.')
    parser.add_argument('--folder_id', type=str, default='1cSsfaBIVLilb6-zstXw0p0dEkgpwfJap', help='ID of the destination folder on Google Drive.')
    parser.add_argument('--files', nargs='+', help='Paths to the files to be uploaded.')

    args = parser.parse_args()

    service_account_file = args.service_account_file if args.service_account_file else get_input('Enter the path to your service account key file: ')
    folder_id = args.folder_id if args.folder_id else get_input('Enter the ID of the destination folder on Google Drive: ')
    files = args.files if args.files else get_input('Enter the paths to the files to be uploaded, separated by spaces: ').split()

    if not os.path.exists(service_account_file):
        print(f"Service account key file not found at {service_account_file}")
        sys.exit(1)

    # Authenticate using the service account
    creds = service_account.Credentials.from_service_account_file(service_account_file, scopes=['https://www.googleapis.com/auth/drive'])

    # Build the Google Drive service
    service = build('drive', 'v3', credentials=creds)

    for file_path in files:
        if os.path.exists(file_path):
            upload_file(file_path, folder_id, service)
        else:
            print(f"File {file_path} not found.")

if __name__ == '__main__':
    main()

