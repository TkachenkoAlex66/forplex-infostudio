import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Главная страница студии."""
    return render_template("index.html")


if __name__ == "__main__":
    # Render сообщает нужный порт через переменную окружения PORT.
    # Локально, если переменной нет, используется 5000.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
