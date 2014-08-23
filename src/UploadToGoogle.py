#!/usr/bin/python
import os
import sys
import httplib2
import pprint

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage

FULL_FILENAME = sys.argv[2]
PATH, FILENAME = os.path.split(FULL_FILENAME);

storage = Storage(sys.argv[1])
credentials = storage.get()

http = httplib2.Http()
http = credentials.authorize(http)

drive_service = build('drive', 'v2', http=http)

# Insert a file
media_body = MediaFileUpload(FULL_FILENAME, mimetype='application/octet-stream', resumable=True)
body = {
  'title': FILENAME,
  'description': 'Upload from Monepoque',
  'mimeType': 'application/octet-stream',
  'parents': [{'id':'0B44lEwdxENm2UXNybkdBY0p5cmM'}]
}

file = drive_service.files().insert(body=body, media_body=media_body).execute()
pprint.pprint(file)

