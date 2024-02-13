#!/usr/bin/python3
"""
Web server 
"""
from api.v1.views import app_views
from flask import Flask, jsonify, make_response

app = Flask(__name__)
app.register_blueprint(app_views)

# Enable debug mode
app.debug = True

# Configure the logger
import logging

logging.basicConfig(level=logging.DEBUG)


@app.errorhandler(404)
def not_found(error):
    """json 404 page"""
    app.logger.error("404 Error: %s", error)
    return make_response(jsonify({"error": "Not found"}), 404)


@app.errorhandler(500)
def server_error(error):
    """500 server error"""
    app.logger.error("500 Error: %s", error)
    return make_response(jsonify({"error": "Failure"}), 500)


if __name__ == "__main__":
    # python -m api.v1.app
    app.run(host="0.0.0.0", port=5000)
