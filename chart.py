import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

#create the figure and axis globally
fig, ax = plt.subplots(figsize=(3, 3))

#data for the bar chart
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]

#draw chart function
def draw_chart(canvas):
    
    #create the bar chart with the data
    ax.clear()  # Clear previous chart
    ax.bar(fruits, counts)

    #set chart labels and title
    ax.set_ylabel('Fruit Supply')
    ax.set_title('Fruit Supply by Kind')

    #draw the chart into the provided canvas
    figure_canvas = FigureCanvasTkAgg(fig, canvas.TKCanvas)
    add_toolbar(canvas, figure_canvas)
    figure_canvas.draw()
    figure_canvas.get_tk_widget().pack(side='top', fill='both', expand=False)

#dunction to zoom in the chart by adjusting the axis limits
def zoom_in():
    #get axis
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()

    #apply zoom
    ax.set_xlim(x_min + 0.5, x_max - 0.5)
    ax.set_ylim(y_min + 0.5, y_max - 0.5)
    fig.canvas.draw()

#function to zoom out the chart by adjusting the axis
def zoom_out():
    #get current axis limits
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()

    #apply zoom out by adjusting limits
    ax.set_xlim(x_min - 0.5, x_max + 0.5)
    ax.set_ylim(y_min - 0.5, y_max + 0.5)
    fig.canvas.draw()

def add_toolbar(canvas, fig_canvas_agg):#toolbar functionality.
    """ Add Matplotlib Navigation Toolbar to the canvas """
    toolbar = NavigationToolbar2Tk(fig_canvas_agg, canvas.TKCanvas)
    toolbar.update()
    toolbar.pack(side='top', fill='x')