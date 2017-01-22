import time
from time import mktime
from datetime import datetime


class FormatUtils(object):

    temperature_unit = "fahrenheit" # default

    def getFormattedDate(self, datestr):

        formattedDate = time.strptime(datestr, "%Y-%m-%d")
        # type : 2017-01-07T00:00:00.000-08:00
        date = datetime.fromtimestamp(mktime(formattedDate))
        return date.replace(hour=8, minute=0)
