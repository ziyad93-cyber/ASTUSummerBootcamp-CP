input()
rooms = ['0'] * 10

for x in input():
    if x == 'L':
        rooms[rooms.index('0')] = '1'
    elif x == 'R':
        rooms[9 - rooms[::-1].index('0')] = '1'
    else:
        rooms[int(x)] = '0'

print("".join(rooms))
