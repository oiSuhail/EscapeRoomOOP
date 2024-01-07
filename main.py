class GameObj:
    def __init__(self, name, appearance, feel, smell):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell
    
    def look(self):
        return f"You look at the {self.name}. {self.appearance}\n"
    
    def touch(self):
        return f"You look at the {self.name}. {self.feel}\n"
    
    def sniff(self):
        return f"You look at the {self.name}. {self.smell}\n"
    
class Room:

    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    def check_code(self, code):
        return code == self.escape_code
    
    def get_game_objects_name(self):
        names = []
        for object in self.game_objects:
            names.append(object.name)
        return names
    
class Game:

    def __init__(self):
        self.attempts = 0
        objects = self.create_objects()
        self.room = Room(951, objects)

    def create_objects(self):
        return [
            GameObj("Remote",
                    "It's a black remote with 9 black buttons and 1 red button with the value 10",
                    "Someone has removed the number 0 in the red button",
                    "It smells like a tomato seasoned chips"),
            GameObj("Table",
                    "It's a brown table made of wood but it has an additional leg",
                    "It has a weird look since there's a one more leg at the right side",
                    "It smells like there's a red wine spilled on it"),
            GameObj("Note",
                    "Someone has wrote in the note \"I tried to call the police but they did not respond\"",
                    "Someone cutted the edge of the note",
                    "Its smells like a blood"),
            GameObj("Bowl of soup",
                    "It appears to be tomato soup",
                    "It has cooled down to room tempereture",
                    "You detect 7 different herbs and spices"),
            GameObj("Clock",
                    "The hour hand is pointing towards the note, the minute hand towards the table, and the second hand towards the remote",
                    "The battery compartment is open and empty",
                    "It smeels of plastic")
        ]


    def take_turn(self):
        prompt = self.get_room_prompt()
        selection = input(prompt)

        if selection.isnumeric() == True:
            selection = int(selection)

            if selection <= len(self.room.get_game_objects_name()):
                print(self.select_object(selection))
                self.take_turn()
            else:
                is_code_correct = self.guess_code(selection)
                if is_code_correct:
                    print("The code is correct, Congrats!")
                else:
                    if self.attempts == 3:
                        print("Game Over!")
                    else:
                        print(f"incorrect you have {self.attempts}/3 attempt left")
                        self.take_turn()

        else:
            print("Wrong input")
            self.take_turn()
    
    def get_room_prompt(self):
        prompt = "Enter the 3 digit lock code or choose an item to interact with:\n\n"
        names = self.room.get_game_objects_name()
        index = 1
        for name in names:
            prompt += f"{index}. {name}\n"
            index += 1
        return prompt
    
    def select_object(self, index):
        selected_object = self.room.game_objects[index-1]
        prompt = self.get_object_interaction_string(selected_object.name)
        interaction = input(prompt)
        clue = self.interact_with_object(selected_object, interaction)
        print(clue)
        return ""

    def get_object_interaction_string(self, name):
        return f"How do you want to interact with the {name}?\n1. Look\n2. Touch \n3. Smell\n"
    
    def interact_with_object(self, object, interaction):
        if interaction == "1":
            return object.look()
        elif interaction == "2":
            return object.touch()
        elif interaction == "3":
            return object.sniff()
        else:
            return "Wrong input"
        
    def guess_code(self, code):
        if self.room.check_code(code) == True:
            return True
        else:
            self.attempts += 1
            return False

game = Game()
game.take_turn()