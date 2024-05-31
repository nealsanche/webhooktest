from flask import Flask, request
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['POST'])
def save_post_data():
    # Get the data from the request
    data = request.get_data(as_text=True)
    
    # Get the client IP address
    client_ip = request.remote_addr
    
    # Generate a filename with the current date, time, and client IP address
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"{timestamp}_{client_ip}.txt"
    
    # Ensure the directory exists
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Save the data to a file
    file_path = os.path.join('data', filename)
    with open(file_path, 'w') as file:
        file.write(data)
    
    return 'Data saved', 200

if __name__ == '__main__':
    app.run(port=5000)
