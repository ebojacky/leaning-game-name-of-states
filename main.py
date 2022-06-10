import turtle
import pandas

game_dic = {
    "us": {"image": "us.gif", "csvfile": "us.csv"},
    "africa": {"image": "africa.gif", "csvfile": "africa.csv"}
            }

my_screen = turtle.Screen()
my_screen.setup(800, 900, 0, 0)

choice = my_screen.textinput("Name the States Game", "Choose 'US' or 'Africa'")
choice = choice.lower()

my_screen.title(f"{choice.upper()} STATES GAME")
image = game_dic[choice]["image"]
csvfile = game_dic[choice]["csvfile"]

my_screen.addshape(image)

my_main_turtle = turtle.Turtle()
my_main_turtle.shape(image)

'''
def get_mouse_click_coor(x, y):
    print(x, y)
my_screen.onscreenclick(get_mouse_click_coor)
my_screen.mainloop()
'''

my_writing_turtle = turtle.Turtle()
my_writing_turtle.penup()
my_writing_turtle.hideturtle()

panda_states_table = pandas.read_csv(csvfile)
states = panda_states_table["state"].tolist()

correctly_typed_states = []

input_message = "Type a state name"

while len(correctly_typed_states) < len(states):
    input_title = f"{len(correctly_typed_states)}/{len(states)} provided"

    reply = my_screen.textinput(input_title, input_message)
    reply = reply.title()

    if reply in states:
        correctly_typed_states.append(reply)
        x = int(panda_states_table[panda_states_table["state"] == reply].x)
        y = int(panda_states_table[panda_states_table["state"] == reply].y)
        my_writing_turtle.goto(x, y)
        my_writing_turtle.write(reply, align="center", font=("Ariel", 12, "normal"))

my_screen.exitonclick()
