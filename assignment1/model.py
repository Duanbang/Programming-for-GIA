import tkinter
import random
import operator
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation
import matplotlib
import requests
import bs4

matplotlib.use('TkAgg')

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []

f = open('in.txt', newline='') 
environment = []
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:				# A list of rows
    parsed_row = row
    rowlist = []
    for value in parsed_row:				# A list of value
        rowlist.append(value)
    environment.append(rowlist)
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.

matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()

for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, 20, agents, y, x))
    
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5


"""# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents,neighbourhood,x,y))"""

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbourhoods()

"""matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)"""

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
"""for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,10)])"""

carry_on = True	
def update(frame_number):
    
    fig.clear()   
    global carry_on
    
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbourhoods(neighbourhood)
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        matplotlib.pyplot.imshow(environment)
        
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 10) & (carry_on) :
        yield a			
        a = a + 1

carry_on = True

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop()




