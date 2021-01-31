
class Game():
    def __init__(self):
        self.game_running = False
        self.players = []
    
    def game_running(self, running):
        self.game_running = running

    def seat_player(self, player):
        if self.game_running:
            return (False, "Game running.")

        if player not in self.players:
            self.players.append(player)
            return (True, None)
        else:
            return (False, "Already seated.")
    
    def unseat_player(self, player):
        if self.game_running:
            return (False, "Game running.")

        if player in self.players:
            self.players.remove(player)
            return (True, None)
        else:
            return (False, "Wasn't seated.")

    def clear_players(self):
        self.players.clear()

