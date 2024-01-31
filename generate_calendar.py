from ics import Calendar, Event
from datetime import datetime, timedelta

# you can add events as you need 
airdrop_events = [
    ("Namada", "TGE", "2024-03-15"),
    ("AltLayer", "TGE", "2024-01-20"),
    ("Dymension", "Airdrop", "2024-02-10"),
    ("Saga", "Airdrop", "2024-04-01"), 
    ("Frame", "Airdrop", "2024-04-01"), 
    ("Aevo", "TGE", "2024-01-15"),
    ("Thetanuts Finance", "Airdrop", "2024-03-01"),
    ("zkLink", "TGE", "2024-03-01"),
    ("ZetaChain", "TGE", "2024-03-01"),
]

# create a calendar
cal = Calendar()

# add calendars for events
for name, type, date in airdrop_events:
    event = Event()
    event.name = f"{name} {type}"
    event.begin = datetime.strptime(date, "%Y-%m-%d")
    event.duration = timedelta(days=7) 
    event.description = f"{name} {type} on {date}"
    cal.events.add(event)

# save as ICS file
with open("Airdrop_Calendar.ics", "w") as f:
    f.writelines(cal.serialize())
