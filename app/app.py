nano app/Dockerfile
nano app/requirements.txt
nano terraform/main.tf
from flask import Flask
import os

app = Flask(__name__)

COLOR = os.environ.get("APP_COLOR", "blue")

@app.route("/")
def home():
    return f"""
    <html>
        <head><title>CLO835 Assignment</title></head>
        <body style='background-color:{COLOR};'>
            <h1>Hello from CLO835-Yasmin App!</h1>
            <p>This application is running inside Docker with background color: <b>{COLOR}</b></p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
