from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)


#function to fetch hostname and ip
def fetchDetails():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return str(hostname), str(ip)

@app.route("/")
def index():
    return "<h1>Home</h1>"


@app.router("/health")
def health():
    return jsonify(
        status="UP"
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

