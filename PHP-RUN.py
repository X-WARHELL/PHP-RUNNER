import os
import random
import time
import requests

# clear the terminal
os.system('clear')


print ("__        __         _   _      _ _ ")
print ("\ \      / /_ _ _ __| | | | ___| | |")
print (" \ \ /\ / / _` | '__| |_| |/ _ \ | |")
print ("  \ V  V / (_| | |  |  _  |  __/ | |")
print ("   \_/\_/ \__,_|_|  |_| |_|\___|_|_|")


print("\n  -- (WarHell) -- [Professional Warhill Morse Code Translator Follow us on GitHub]\n  -- (WarHell) -- [ github : https://gthub.com/X-WARHELL]")
print("")

# ask for the php file path
php_file_path = input('Enter the path of the PHP file: ')
os.system('clear')


for i in range(1, 10):
    print(f'on the way to run {i*10}%')
    time.sleep(2)

os.system('clear')
# read the contents of the php file
with open(php_file_path, 'r') as f:
    php_code = f.read()


# define the flask app
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST'])
def run_php():
    try:
        subprocess.check_output(['php', '-r', request.get_data().decode('utf-8')])
        return 'The PHP file was run'
    except subprocess.CalledProcessError as e:
        return 'The file has errors'

# start the flask app in a separate thread
import threading

def start_flask_app():
    app.run(port=5000)

flask_thread = threading.Thread(target=start_flask_app)
flask_thread.start()

# say the words on the way to run

# send the php code to the flask app and wait for the response
response = requests.post('http://localhost:5000', data=php_code.encode('utf-8'))
print(response.text)
