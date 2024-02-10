from flask import Flask

app = Flask(__name__)


@app.route("/")
def site1():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route("/index")
def site2():
    return "<h1>И на Марсе будут яблони цвести!</h1>"


@app.route("/promotion")
def promotion():
    s = [
        "Человечество вырастает из детства."
        "Человечеству мала одна планета."
        "Мы сделаем обитаемыми безжизненные пока планеты."
        "И начнем с Марса!"
        "Присоединяйся!"
    ]
    return "".join(f"<p>{s}</p>" for s in s)


@app.route("/promotion_image")
def image():
    return """
    <html>
        <head>
            <title>Колонизация</title>
            <link rel="stylesheet" type="text/css" href="/static/css/style.css">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        </head>
        <body>
            <h1>Жди нас, Марс!</h1>
            <img src="static/img/MARS.png">
            <div class="alert alert-primary" role="alert">
                Человечество вырастет из детства.
            </div>
            <div class="alert alert-success" role="alert">
                Человечеству мала одна планета.
            </div>
            <div class="alert alert-danger" role="alert">
                Мы сделаем обитаемыми безжизенные пока планеты
            </div>
            <div class="alert alert-warning" role="alert">
                И начнём с Марса!
            </div>
            <div class="alert alert-info" role="alert">
                Присоединяйся!
            </div>
        </body>
    </html>
    """
