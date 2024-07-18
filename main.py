from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S States Game")
image = 'blank_states_img.gif'
screen.addshape(image)


turtle = Turtle()
turtle.shape(image)



data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []
game_on = True
# guessing = True

while(game_on):
    state_guess = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Name the state").title()
    
    if state_guess == "Exit":
        break

    if (state_guess in states and state_guess not in guessed_states):
        #get coordinates
        state = data[data.state == state_guess]
        # print(state)
        x = int(state.x)
        y = int(state.y)
        # print(x,y)
        #add name to map
        state_writer = Turtle(visible=False)
        state_writer.penup()
        state_writer.goto(x,y)
        state_writer.write(state_guess)
        #add name to guessed_states
        guessed_states.append(state_guess)
        # print("guessed_states:", guessed_states)

#convert unguessed states to csv
states_to_learn = []
for state in states:
    if state not in guessed_states:
        states_to_learn.append(state)

# turn states_to_learn dict to csv
states_to_learn_df = pandas.DataFrame(states_to_learn)
states_to_learn_df.to_csv("states_to_learn.csv")