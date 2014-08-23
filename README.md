google-drive-backup
===================

Use Google Drive to backup your Linux Server

There is a one-off setup authentication process

1. Get the Client ID API from Google API Page

2. Use GetCredential.py to generate an Authentication URL, it means the User open the URL will authorise the upload program to upload to his Google Drive

GetCredential.py CLIENTSECRET_PATH SAVE_STORAGE_NAME

3. Obtain the access token and type it in the console to answer the questions by GetCredential.py

4. filename with name <SAVE_STORAGE_NAME> should be generated. 

And then you can use the UploadToGoogle to upload the file, the syntax is as followed. 

UploadToGoogle.py STORAGE_FILE FULL_FILENAME

The storage file is the file you get in step 1

The FULL_FILENAME is the file you want to upload to

For details, pls refer to my blog