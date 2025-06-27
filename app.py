import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
#Add page title
ui.page_opts(title="App with Plot",fillable=True)

#Add bar with a slider input
with ui.sidebar():
    ui.input_slider("select_number_of_bins", "Bins", 0, 100, 40)


@render.plot(alt="A histogram of random data")
def histogram():
    count_of_points: int=437
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(count_of_points)
    plt.hist(x,
             bins=input.select_number_of_bins(),
             density= True,
             color="Yellow",
             edgecolor="green"
            )
