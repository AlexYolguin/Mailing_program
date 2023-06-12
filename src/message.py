from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


message = MIMEMultipart()
message["Subject"] = "Open Me4"

text = MIMEText("Test4")
message.attach(text)