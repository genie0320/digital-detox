from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import getAuth


def main(SCOPES):
    creds = getAuth.get_mail_auth(SCOPES)
    try:
        # Call the Gmail API
        service = build("gmail", "v1", credentials=creds)
        results = service.users().labels().list(userId="me").execute()
        labels = results.get("labels", [])

        if not labels:
            print("No labels found.")
            return
        print("Labels:")
        for label in labels:
            print(label["name"])

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    # If modifying these scopes, delete the file token.json.
    SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

    main(SCOPES)
