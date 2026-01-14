# server.py - Web Terminal SaWiT OS (Versi Stabil)
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import threading
import sys
from main import shell, load_filesystem, DEFAULT_FS, DEFAULT_USERS, DEFAULT_SYSTEM

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Izinkan dari mana saja

sessions = {}

def run_shell(sid):
    class WebIO:
        def __init__(self, sid):
            self.sid = sid

        def write(self, text):
            if not text.endswith('\n'):
                text += '\n'
            socketio.emit('output', text, room=self.sid)

        def flush(self):
            pass

    # Redirect stdout & stderr
    sys.stdout = WebIO(sid)
    sys.stderr = WebIO(sid)

    def web_input(prompt=""):
        socketio.emit('prompt', prompt, room=sid)
        # Tunggu input dari client
        sessions[sid]['waiting'] = True
        while sessions[sid]['waiting']:
            threading.Event().wait(0.1)
        return sessions[sid]['last_input']

    # Override input
    import builtins
    builtins.input = web_input

    # Jalankan shell
    fs = load_filesystem(DEFAULT_FS)
    try:
        shell(fs, DEFAULT_USERS, DEFAULT_SYSTEM)
    except Exception as e:
        socketio.emit('output', f"\nError fatal: {e}\n", room=sid)

@app.route('/')
def index():
    return render_template('terminal.html')

@socketio.on('connect')
def handle_connect(auth):
    sid = request.sid
    sessions[sid] = {
        'waiting': False,
        'last_input': ''
    }
    print(f"[+] Client connected: {sid}")
    threading.Thread(target=run_shell, args=(sid,), daemon=True).start()

@socketio.on('input')
def handle_input(data):
    sid = request.sid
    text = data.get('text', '').rstrip()
    if sid in sessions and sessions[sid]['waiting']:
        sessions[sid]['last_input'] = text + '\n'
        sessions[sid]['waiting'] = False
        print(f"Input dari {sid}: {text}")

@socketio.on('disconnect')
def handle_disconnect():
    sid = request.sid
    if sid in sessions:
        del sessions[sid]
    print(f"[-] Client disconnected: {sid}")

if __name__ == '__main__':
    print("SaWiT OS Web Terminal berjalan!")
    print("Akses di: http://localhost:5000")
    print("Atau dari device lain: http://<IP_KAMU>:5000")
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)