from worldlib import *
from arglite import parser as cliarg

class Keypad(FixtureSpec):

    def __init__(self):
        super().__init__()
        self.entry_code = check_flag("code")

    def use(self, **kwargs) -> bool:
        if kwargs["code"] == self.entry_code:
            set_flag("keycode")
            return True
        return False

def main():
    result = None
    pad = Keypad()
    try:
        result = pad.use(
            code=cliarg.keycode
        )
    except:
        n.path.change({"act": 2, "scene": 0})
    
    if not result:
        n.path.change({"act": 2, "scene": 0})

    n.narrate()

if __name__ == "__main__":
    main()
