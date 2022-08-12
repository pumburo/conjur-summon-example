import os, time, sys

try:
    username = os.environ['APP_USERNAME']
    password = os.environ['APP_PASSWORD']
except:
    username = "username"
    password = "password"

while True:
    print(username)
    print(password)
    sys.stdout.flush()
    os.chdir('.')
    time.sleep(10)