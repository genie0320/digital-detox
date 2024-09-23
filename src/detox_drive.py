import json

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import getAuth


def main(SCOPES):
    creds = getAuth.get_mail_auth(SCOPES)
    try:
        # Call the Gmail API
        service = build("drive", "v3", credentials=creds)
        files = service.files().list().execute().get("files", [])

        if not files:
            print("No files found.")
            return
        print("success")
        # for f in files:
        #     print(f)
        with open("gdrive.json", "w", encoding="utf-8-sig") as f:
            f.write(json.dumps(files, ensure_ascii=False))

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    # If modifying these scopes, delete the file token.json.
    SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]

    main(SCOPES)
