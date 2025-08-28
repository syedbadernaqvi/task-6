from flask import Flask, Response

app = Flask(__name__)

# Serve CSS directly
@app.route("/static/style.css")
def style():
    css = """
    body {
        font-family: Arial, sans-serif;
        background-color: #f2f6fc;
        text-align: center;
        margin: 0;
        padding: 0;
    }
    .container {
        margin-top: 100px;
    }
    h1 {
        color: #333;
    }
    p {
        font-size: 18px;
        color: #555;
    }
    """
    return Response(css, mimetype="text/css")

# Serve HTML directly
@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Simple Flask App</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="container">
            <h1>🚀 Welcome to My Flask App!</h1>
            <p>This is a simple webpage served with Flask and styled with CSS.</p>
        </div>
    </body>
    </html>
    """
    return Response(html, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
