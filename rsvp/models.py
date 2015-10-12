import datetime
import json
import time

from django.db import models

class Associate(models.Model):
    # Associate's email address
    email = models.EmailField()

    # Associate's name
    name = models.CharField(max_length=200)

    # JSON to store the dates that the associate has RSVPed for
    rsvp_dates = models.TextField()

    def is_coming_today(self):
        """
        Function which parses the rsvp_dates and sees if the associate has 
        RSVPed for today.

        Returns true if they have, false otherwise
        """
        dates = json.loads(self.rsvp_dates)
        today = datetime.date.today()
        for date in dates:
            rsvp_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            if rsvp_date == today:
                return True

        return False