#!/usr/bin/env python

from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(
            {
                "message":"Hello, World"
            }
    ), 200

if __name__ == '__main__':
    app.run(port=9080)
