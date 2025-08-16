from flask import Flask
import os
import signal
import psutil

app = Flask(__name__)

@app.route('/kill_chrome')
def kill_chrome():
    # Find and kill all Chrome processes
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] and "chrome" in proc.info['name'].lower():
            try:
                os.kill(proc.info['pid'], signal.SIGTERM)
            except Exception as e:
                print(f"Error killing {proc.info['pid']}: {e}")
    return "Chrome closed"

if __name__ == '__main__':
    app.run(port=5000)
