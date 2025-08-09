from turtle import Turtle,Screen

# Turner is the object and Turtle is the class from the module turtle
# turner = Turtle()
# print(turner)
# turner.shape("turtle")
# turner.color("DarkSeaGreen2")
# turner.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# Now I will Learn how to use the many available external Python libraries.
# Like the ones from the Python Package Index or PyPI for short.

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)