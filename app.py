#!/usr/bin/python3

"""
Run flask application
"""

from os import getenv
from website import create_app

app_port = int(getenv("PORT", 5000))
app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app_port, debug=True)
