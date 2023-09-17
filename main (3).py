''' Implement a class called player that represents cricket player.The player class should have a
method called play() which prints "The player is playing cricket. Derive a two classes,Batsman and
Bowler,from the player class. Override the play() method in each derived class to print" The batsman
is batting"and the bowler is bowling", respectively write a program to create subject or both the
Bathsman and bowler classes and call the play() method for each object.'''


# Define the base class player
class player:
     def play(self):
         print("The player is playing cricket.")

# Define the derived class Batsman
class Batsman(player):
      def play(self):
          print("The batsman is batting.")

# Define the derived class bowler
class Bowler(player):
      def play(self):
          print("The bowler is bowling.")

# Create objects of batsman and bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play() method for each object 
batsman.play()
bowler.play()