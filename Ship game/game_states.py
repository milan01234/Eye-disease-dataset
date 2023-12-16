class GameState():
     """Traack statistics for alien invasion"""
     def __init__(self,set) -> None:
         """Initalize statistics"""
         self.set=set
         self.reset_stats()
         self.game_active=True
     def reset_stats(self):
          self.ship_left=self.set.ship_limit
