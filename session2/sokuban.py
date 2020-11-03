map = [ 
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', 'D', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
]

player_x = 0
player_y = 1
box_x = 2
box_y = 3
while True:
    map[player_y][player_x] = 'P'
    map[box_y][box_x] = 'B'
    for y in map:
        x_axis = ''
        for x in y:
            x_axis += x + ' '
        print(x_axis)

    move = input('your move')
    map[player_y][player_x] = '-'
    if move == 'w':
        if map[player_y - 1][player_x] == 'B':
            map[box_y][box_x] = '-'
            box_y = box_y - 1
        player_y = player_y - 1
    elif move == 's':
        if map[player_y + 1][player_x] == 'B':
            map[box_y][box_x] = '-'
            box_y = box_y + 1
        player_y = player_y + 1
    elif move == 'a':
        if map[player_y][player_x - 1] == 'B':
            map[box_y][box_x] = '-'
            box_x = box_x - 1
        player_x = player_x - 1
    elif move == 'd':
        if map[player_y][player_x + 1] == 'B':
            map[box_y][box_x] = '-'
            box_x = box_x + 1
        player_x = player_x + 1
# player_x = 1
# player_y = 1

# playing = True
# while playing:
#     for y in range(5):
#         map = ''
#         for x in range(5):
#             if x == player_x and y == player_y:
#                 map = map + 'P '
#             elif x == 3 and y == 0:
#                 map = map + 'B '
#             else:
#                 map = map + '- '
#         print(map)

#     move = input('your move? (w,a,s,d)')
#     if move == 'w':
#         player_y = player_y - 1
#     elif move == 's':
#         player_y = player_y + 1
#     elif move == 'a':
#         player_x = player_x - 1
#     elif move == 'd':
#         player_x = player_x + 1
