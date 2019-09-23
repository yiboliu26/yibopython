import pygal
from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()
results = [die_1.roll() + die_2.roll() +die_3.roll() for roll_num in range(1000)]
max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3, max_results+1)]

hist = pygal.Bar()
hist.title = "Results of rolling 3 D6 dice 1000 times."
hist.x_labels = [str(x) for x in range(3, max_results+3)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8 + D8', frequencies)    
hist.render_to_file('dice_visual.svg')