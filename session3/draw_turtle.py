from turtle import *
color_list = [
    'red', # 3
    'blue', 
    'yellow', 
    'green', 
    'gray', 
    'purple', 
    'brown'
]
speed(-1)
for color_index in range(len(color_list)):
    color(color_list[color_index])
    for j in range(color_index + 3):
        forward(100)
        left(360/(color_index + 3))
# for i in range(len(color_list)):
#     color(color_list[i])
    
mainloop()
