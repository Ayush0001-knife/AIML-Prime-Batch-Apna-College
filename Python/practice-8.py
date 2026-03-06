class Player():
      player_Count=0

      def __init__(self,name,level):
            self.name=name
            self.level=level
            Player.player_Count+=1

      @classmethod
      def get_player_count(cls):
            return cls.player_Count
      
      def display_info(self):
            print(f"Name: {self.name}")
            print(f"Level: {self.level}")

            