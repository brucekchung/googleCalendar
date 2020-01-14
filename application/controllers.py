import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
READ_ONLY_SCOPE = ['https://www.googleapis.com/auth/calendar.readonly']
FULL_SCOPE = ['https://www.googleapis.com/auth/calendar']


class GoogleCalendar:
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """

    def __init__(self):
        self.creds = None

    def _validate(self):
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', FULL_SCOPE)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

    def _events(self):
        """ Calendar API """
        service = build('calendar', 'v3', credentials=self.creds)
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        events_result = service.events().list(
            calendarId='primary', 
            timeMin=now,
            maxResults=10, 
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])
        return events

    def _calendar_list(self):
        """ CalendarList API """
        service = build('calendar', 'v3', credentials=self.creds)
        result = service.calendarList().list().execute()
        calendar_list = result.get('items', [])
        return calendar_list

    def get_events(self):
        self._validate()
        events = self._events()
        return events

    def get_calendar_list(self):
        self._validate()
        calendar_list = self._calendar_list()
        return calendar_list
