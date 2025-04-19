from flask import Flask, redirect, request, session
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
