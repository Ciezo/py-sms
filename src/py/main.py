'''
    @author Cloyd Van S. Secuya
    @description This is a script that implements our SMS Service wrapped in Rest Client with Twilio
'''


from sms_service import sms_alert_msg
from datetime import datetime
'''
Call the function here to begin creating the following:
    1. Message body
    2. Recipient number
'''
current_time_date = str(datetime.now())
body = "Hello, this is Test message! " + current_time_date
to_number = ""

# Param: body, to_number
sms_alert_msg(body, to_number)