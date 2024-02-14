import json
import datetime

class Note:
    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.timestamp = datetime.datetime.now().isoformat()

    def to_dict(self):
        return {
            'title': self.title,
            'body': self.body,
            'timestamp': self.timestamp
        }

    def __str__(self):
        return f"Title: {self.title}\nBody: {self.body}\nTimestamp: {self.timestamp}"
