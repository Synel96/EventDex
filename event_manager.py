import os
import pandas as pd

class EventManager:
    def __init__(self, filename="events.xlsx"):
        self.filename = filename

    def save_event(self, date_str, event_type, attendees, host):
        data = {
            "Date": [date_str],
            "Event Type": [event_type],
            "Attendees": [attendees],
            "Host": [host]
        }

        if os.path.exists(self.filename):
            try:
                df = pd.read_excel(self.filename)
                df_new = pd.DataFrame(data)
                df = pd.concat([df, df_new], ignore_index=True)
            except Exception as e:
                raise RuntimeError(f"Failed to read existing Excel file: {e}")
        else:
            df = pd.DataFrame(data)

        try:
            df.to_excel(self.filename, index=False)
        except Exception as e:
            raise RuntimeError(f"Failed to save Excel file: {e}")