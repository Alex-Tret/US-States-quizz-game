import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
	answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
									prompt="What's another state name ?").title()

	if answer_state in all_states:
		guessed_states.append(answer_state)
		state_data = data[data.state == answer_state]

		turtle2 = turtle.Turtle()
		turtle2.penup()
		turtle2.hideturtle()
		turtle2.goto(int(state_data.x), int(state_data.y))
		turtle2.write(answer_state)

	elif answer_state == 'Exit':
		missed_states = [item for item in all_states if item not in guessed_states]
		df = pandas.DataFrame(missed_states)
		df.to_csv("states_to_learn.csv")
		break
