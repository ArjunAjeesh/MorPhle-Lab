from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop_info():
    # Get the full name of the user
    full_name = os.popen('getent passwd $USER | cut -d: -f5').read().strip()

    # Get the system username
    username = os.getlogin()

    # Get the current server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Run the top command to get system stats
    top_output = subprocess.getoutput('top -bn1 | head -n 20')

    # Return the output in HTML format
    return f"""
    <html>
        <body>
            <h2>System Info:</h2>
            <p><strong>Name:</strong> {full_name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <h3>Top Output:</h3>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
