# Terrence Creig
# IT 140 Project Two - Haunted House Escape
# Collect six items before entering the Attic to escape the Ghost.


def show_instructions():
    """Explain the objective and available commands."""
    print('Haunted House Escape')
    print('Collect all 6 items before entering the Attic!')
    print('Move: go north, go south, go east, go west')
    print('Collect: get item name (example: get flashlight)')


def show_status(current_room, inventory, rooms):
    """Display the player's current location and collected items."""
    print('\nYou are in the', current_room)
    print('Inventory:', inventory)
    if 'item' in rooms[current_room]:
        print('You see a', rooms[current_room]['item'])
    print('--------------------')


def main():
    """Run the game until the player wins or loses."""
    # Rooms and items follow the Project One storyboard.
    # Connections form a safe path to all six items before the Attic.
    rooms = {
        'Living Room': {'east': 'Kitchen', 'north': 'Bedroom'},
        'Kitchen': {'west': 'Living Room', 'item': 'Flashlight'},
        'Bedroom': {'south': 'Living Room', 'east': 'Bathroom', 'item': 'Key'},
        'Bathroom': {'west': 'Bedroom', 'north': 'Garage', 'item': 'Map'},
        'Garage': {'south': 'Bathroom', 'east': 'Basement', 'item': 'Rope'},
        'Basement': {'west': 'Garage', 'north': 'Study', 'item': 'Battery'},
        'Study': {'south': 'Basement', 'east': 'Attic', 'item': 'Crowbar'},
        'Attic': {'west': 'Study'}
    }
    current_room = 'Living Room'
    inventory = []
    required_items = 6
    show_instructions()

    while True:
        show_status(current_room, inventory, rooms)
        command = input('Enter your move: ').strip().lower()

        if command.startswith('go '):
            direction = command[3:].strip()
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                if current_room == 'Attic':
                    if len(inventory) == required_items:
                        print('Congratulations! You collected all six items and escaped the Ghost!')
                    else:
                        print('NOM NOM...GAME OVER! The Ghost caught you!')
                    print('Thanks for playing Haunted House Escape!')
                    break
            else:
                print('You cannot go that way!')
        elif command.startswith('get '):
            item_name = command[4:].strip()
            room_item = rooms[current_room].get('item')
            if room_item and item_name == room_item.lower():
                inventory.append(room_item)
                del rooms[current_room]['item']
                print(room_item, 'added to your inventory!')
            else:
                print('That item is not available in this room!')
        else:
            print('Invalid command. Try go north or get flashlight.')


if __name__ == '__main__':
    main()
