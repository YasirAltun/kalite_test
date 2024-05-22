from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import subprocess
import eventlet
import psutil
import time
from threading import Thread

eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('start_test')
def start_test(test_name):
    try:
        result = subprocess.run(['python', f'{test_name}.py'], capture_output=True, text=True)
        output = result.stdout
        if not output:
            output = "No output captured."
        socketio.emit('test_output', {'test_name': test_name, 'output': output})
    except Exception as e:
        socketio.emit('test_output', {'test_name': test_name, 'output': str(e)})

@socketio.on('stop_test')
def stop_test(test_name):
    emit('test_output', {'test_name': test_name, 'output': 'Test durduruldu.'})

def send_ram_usage():
    while True:
        ram_usage = psutil.virtual_memory().percent
        socketio.emit('ram_usage', {'usage': ram_usage})
        time.sleep(1)

def send_network_usage():
    old_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    while True:
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        network_usage = (new_value - old_value) / (1024 * 1024)  # MBps
        old_value = new_value
        socketio.emit('network_usage', {'usage': network_usage})
        time.sleep(1)

def send_cpu_usage():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        socketio.emit('cpu_usage', {'usage': cpu_usage})
        time.sleep(1)

if __name__ == '__main__':
    Thread(target=send_ram_usage).start()
    Thread(target=send_network_usage).start()
    Thread(target=send_cpu_usage).start()
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)
