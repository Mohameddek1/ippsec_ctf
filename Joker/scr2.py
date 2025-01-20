import pwd
import os

current_user = pwd.getpwuid(os.getuid()).pw_name
print(f"Current user: {current_user}")
