#To Install
To run make sure you run pip
pip3.10 install beautifulsoup4 requests google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client



#To Run
python3.10 scrape_apartments.py

#Requirements
You'll need to download the credentials.json from Sean Thomas

###Downloading Credentials.json

o create credentials and download a credentials.json file for accessing the Google Drive API within a Python application, follow these steps:

Go to the Google Cloud Console: https://console.cloud.google.com/

Sign in with your Google account or create a new one.

Create a new project or select an existing one by clicking the project dropdown in the top-right corner of the console.

Once you have selected a project, open the navigation menu (hamburger icon in the top-left corner), and navigate to "APIs & Services" > "Dashboard".

Click the "+ ENABLE APIS AND SERVICES" button at the top of the page.

In the API Library, search for "Google Drive API" and click on it.

Click the "Enable" button to enable the Google Drive API for your project.

Once the API is enabled, you'll be taken to the Google Drive API page. Click "Create credentials" in the "Getting started" section or navigate to "APIs & Services" > "Credentials" in the sidebar, and then click "Create credentials" > "OAuth client ID".

If prompted, set up the OAuth consent screen by providing the required information (Application name, User support email, etc.) and clicking "Save and continue". You can skip optional fields if they're not applicable.

On the "Create OAuth 2.0 client ID" screen, select "Desktop app" as the application type, provide a name for your client (e.g., "My Python App"), and click "Create".

After creating the OAuth client, you'll see a popup with your client ID and secret. Click "OK" to close the popup.

In the "Credentials" tab, you'll see your newly created client ID. Click the download icon on the right side of your client ID. This will download a credentials.json file containing your OAuth 2.0 client ID and secret.

Now, you have your credentials.json file, which you can use within your Python application to access the Google Drive API.

For a sample Python application using the Google Drive API, check the official quickstart guide: https://developers.google.com/drive/api/v3/quickstart/python