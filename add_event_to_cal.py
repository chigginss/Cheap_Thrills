""" Creating an event with Google Calendar API """

# take event data from eventbrite API
# send to correct route via Flask
# add this event data to Google Calendar vis API 

# Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
events_add = service.events().list(calendarId='primary').execute()
events = events_result.get('items', [])
