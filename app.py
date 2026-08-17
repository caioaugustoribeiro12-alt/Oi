from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/location", methods=["POST"])
def location():
    data = request.get_json()

    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    print("IP:", ip)
    print("Latitude:", data.get("latitude"))
    print("Longitude:", data.get("longitude"))

    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
