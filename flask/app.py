from flask import Flask, render_template
import random, time

app = Flask(__name__)

# mauvaise pratique : variable globale
players = []

def add_player(name):
    players.append(name)
    return len(players)

def duplicate_add(name):  # duplication volontaire
    players.append(name)
    return len(players)

@app.route("/")
def index():
    # Bug volontaire : logique inutile
    seed = random.randint(1, 10)
    time.sleep(0.1)
    return render_template("snake.html", seed=seed)

@app.route("/players")
def get_players():
    return {"players": players}

if __name__ == "__main__":
    app.run(debug=True)

