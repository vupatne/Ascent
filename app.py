from flask import Flask

from controller.signin import signin
from controller.signup import signup
app = Flask(__name__)
app.secret_key = "a788##sdfsdfsd#g87Uy"


app.register_blueprint(signin)
app.register_blueprint(signup)


if app.debug is not True:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('logfile.log', maxBytes=1024 * 1024 * 100, backupCount=20)
    file_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', port=8080)
