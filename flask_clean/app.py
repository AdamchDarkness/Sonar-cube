from flask import Flask, render_template
from typing import List

app = Flask(__name__)

class PlayerManager:
    """Gère la liste des joueurs connectés."""
    def __init__(self):
        self.players: List[str] = []

    def add_player(self, name: str) -> int:
        """Ajoute un joueur et renvoie le nombre total."""
        if name not in self.players:
            self.players.append(name)
        return len(self.players)

    def get_players(self) -> List[str]:
        """Retourne la liste des joueurs."""
        return self.players

manager = PlayerManager()

@app.route("/")
def index():
    """Affiche le jeu Snake."""
    return render_template("snake.html")

@app.route("/players")
def get_players():
    """Renvoie la liste des joueurs en JSON."""
    return {"players": manager.get_players()}

if __name__ == "__main__":
    app.run(debug=True)
