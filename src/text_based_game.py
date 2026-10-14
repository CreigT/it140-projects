# Terrence Creig
# IT 140 Project Two - Haunted House Escape
# Rooms and items follow the original Project One game_map.drawio.


def show_instructions():
    """Explain the goal and commands."""
    print('Haunted House Escape')
    print('Collect all six items before entering the Attic!')
    print('Commands: go north, go south, go east, go west')
    print('To collect an item: get item name (example: get flashlight)')


def show_status(current_room, inventory, rooms):
    """Display current location, inventory, and available item."""
    print('\nYou are in the', current_room)
    print('Inventory:', inventory)
    if 'item' in rooms[current_room]:
        print('You see a', rooms[current_room]['item'])
    print('--------------------')


def main():
    """Run the game until the player wins or loses."""
    rooms = {
        'Foyer': {'west': 'Kitchen', 'north': 'Attic'},
        'Kitchen': {'east': 'Foyer', 'north': 'Bedroom', 'item': 'Flashlight'},
        'Bedroom': {'south': 'Kitchen', 'north': 'Bathroom', 'east': 'Attic', 'item': 'Key'},
        'Bathroom': {'south': 'Bedroom', 'east': 'Library', 'item': 'Candle'},
        'Library': {'west': 'Bathroom', 'east': 'Basement', 'south': 'Attic', 'item': 'Book'},
        'Basement': {'west': 'Library', 'south': 'Garage', 'item': 'Rope'},
        'Garage': {'north': 'Basement', 'west': 'Attic', 'item': 'Crowbar'},
        'Attic': {'south': 'Foyer', 'west': 'Bedroom', 'north': 'Library', 'east': 'Garage'}
    }
    current_room = 'Foyer'
    inventory = []
    show_instructions()

    while True:
        show_status(current_room, inventory, rooms)
        command = input('Enter your move: ').strip().lower()
        if command.startswith('go '):
            direction = command[3:].strip()
            if direction in ('north', 'south', 'east', 'west') and direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                if current_room == 'Attic':
                    if len(inventory) == 6:
                        print('Congratulations! You collected all six items and escaped the Ghost!')
                    else:
                        print('GAME OVER! The Ghost caught you!')
                    print('Thanks for playing Haunted House Escape!')
                    break
            else:
                print('You cannot go that way!')
        elif command.startswith('get '):
            requested_item = command[4:].strip()
            room_item = rooms[current_room].get('item')
            if room_item is not None and requested_item == room_item.lower():
                inventory.append(room_item)
                del rooms[current_room]['item']
                print(room_item, 'added to your inventory!')
            else:
                print('That item is not available in this room!')
        else:
            print('Invalid command. Try go north or get flashlight.')


if __name__ == '__main__':
    main()
