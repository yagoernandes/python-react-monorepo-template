from flask import Flask
from redis import Redis

app = Flask(__name__)

redis = Redis(host='redis', port=6379)

@app.route("/")
def hello_world():
    redis.incr('hits')
    return f"<p>This Compose/Flask demo has been viewed {redis.get('hits').decode('utf-8')} time(s).</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)