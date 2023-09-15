from worldlib import *

class RoboVac(FixtureSpec):

    def __init__(self):
        """Construct the object"""
        super().__init__()
        self.battery = 100
        self.working = False

    def __str__(self) -> str:
        """Report the battery remaining"""
        return f"🔋 Battery remaining: {self.battery}% 🔋"

    def battery_usage(self, room_x: int = 0, room_y: int = 0) -> int:
        """Calculate battery usage using room_x, room_y"""
        ###################################################
        ## WORK HERE -- MATCH INDENTATION LEVEL OF THIS COMMENT

        # Calculate square footage of the room
        square_footage = room_x * room_y
        # Calculate the battery drain using a variable identifier
        #       with the name of "drain" 
        drain = (square_footage * 5) // 60
        ## WORK HERE -- MATCH INDENTATION LEVEL OF THIS COMMENT
        ###################################################
        return drain

    def sense_room(self) -> (int, int):
        """Get measurements of the room from input prompts"""
        ###################################################
        ## WORK HERE -- MATCH INDENTATION LEVEL OF THIS COMMENT

        # Take user input of room width using variable idenitifer
        #       "room_x"
        room_x = int(input("enter room width"))
        #  Take user input of room length using variable idenitifer
        #       "room_y"
        room_y = int(input("enter room length"))
        ## WORK HERE -- MATCH INDENTATION LEVEL OF THIS COMMENT
        ###################################################
        return room_x, room_y

    def clean_room(self) -> None:
        """Clean the room"""
        if self.working:
            # If the robot works, clean out the .junk files
            junks = glob("*.junk")
            for junk in junks:
                os.remove(junk)

    def use(self, room_x: int = 0, room_y: int = 0) -> None:
        """Operate the Groomba"""
        try:
            width, length = self.sense_room()
        except:
            print("Looks like there's an issue with the room calculation.")
        # Subtract used battery
        try:
            self.battery -= self.battery_usage(
                width, length
            )
        except:
            print("Looks like there's an issue with the battery usage calculation.")

def main():
  
    # Check if room still contains junk, tell
    # that branch of the story
    if glob("*.junk"):
        n.path.change({"act": 2, "scene": 0})
        n.narrate()
  
    # Ask if user wants to turn the Groomba on
    q = narrator.YesNoQuestion({
        "question":"Turn on the Groomba™",
        "outcomes": [{"act": 4, "scene": 0}, {"act": 5, "scene": 0}]
    })
  
    # If not, then...well, it's your garage
    n.path.change(q.ask())
    if n.path.act == 5:
        n.narrate()
        return
    
    # Create and run the RoboVac
    robot = RoboVac()
    robot.use()

    # Check the final result
    benchmark = int(check_flag("battery"))
    if robot.battery == benchmark:
        robot.working = True
        robot.clean_room()
        set_flag('groombad', True)
        n.path.change({"act": 3, "scene": 0})
    
    if robot.battery > benchmark: 
        n.path.change({"act": 6, "scene": 0})
    
    # Print the remaining battery charge
    print(robot)

    # Tell the story
    n.narrate()

if __name__ == "__main__":
    """If run from command line, run main function"""
    main()
