import sys

from app import app


@app.route("/")
def hello():
    version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
    message = "Hello World from Flask in a uWSGI Nginx Docker container with Python {} (default)".format(
        version
    )
    return message


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
