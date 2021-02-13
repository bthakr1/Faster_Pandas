# limitations of appending

from datetime import datetime

def parse_time(ts):
    # [02/Jul/2012:16:38:56 -0400]
    time = datetime.strptime(ts,'[%d/%b/%Y:%H:%M:%S %z'])
    return time.replace(tzinfo=None) # Removes time zone