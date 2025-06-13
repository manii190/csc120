"""
venna mani abhiram reddy 
cs-120 battle ship project
This code implements a Battleship game where ships are placed on a
 10x10 grid based on a placement file, and guesses from a guess file 
 determine hits, misses, or sunk ships. It validates ship placements
 , processes guesses, and outputs results, stopping when
   all ships are sunk or an error occurs.
"""
class GridPos:
    """Represents a single position on the Battleship game board."""
    def __init__(self, x, y):
        """Initialize a grid position with coordinates and default state.
        
        Args:
            x (int): X-coordinate (0-9).
            y (int): Y-coordinate (0-9).
        """
        self.x = x
        self.y = y
        self.ship = None
        self.guessed = False
    
    def __str__(self):
        """Return string representation of the grid position.
        
        Returns:
            str: '.' for empty, 'X' for guessed, or ship kind if occupied.
        """
        if self.ship is None:
            return "."
        if self.guessed:
            return "X"
        return self.ship.kind

class Ship:
    """Represents a ship in the Battleship game."""
    def __init__(self, kind, positions):
        """Initialize a ship with its kind and occupied positions.
        
        Args:
            kind (str): Ship type ('A', 'B', 'S', 'D', 'P').
            positions (list): List of (x, y) tuples occupied by the ship.
        """
        self.kind = kind
        self.size = {"A": 5, "B": 4, "S": 3, "D": 3, "P": 2}[kind]
        self.positions = positions
        self.hits = 0
    
    def __str__(self):
        """Return string representation of the ship.
        
        Returns:
            str: The ship's kind.
        """
        return self.kind

class Board:
    """Represents the Battleship game board with ships and grid positions."""
    def __init__(self):
        """Initialize a 10x10 game board with empty grid positions."""
        self.ships = []
        self.grid = []
        for x in range(10):
            row = []
            for y in range(10):
                row.append(GridPos(x, y))
            self.grid.append(row)
    
    def add_ship(self, kind, x1, y1, x2, y2, line):
        """Add a ship to the board with validation.
        
        Args:
            kind (str): Ship type ('A', 'B', 'S', 'D', 'P').
            x1 (int): X-coordinate of first endpoint.
            y1 (int): Y-coordinate of first endpoint.
            x2 (int): X-coordinate of second endpoint.
            y2 (int): Y-coordinate of second endpoint.
            line (str): Original input line for error reporting.
        
        Returns:
            bool: True if ship was added successfully, False if invalid.
        """
        # Check if ship kind is valid and unique
        if kind not in ["A", "B", "S", "D", "P"]:
            print("ERROR: fleet composition incorrect")
            return False
        for ship in self.ships:
            if ship.kind == kind:
                print("ERROR: fleet composition incorrect")
                return False
        
        # Check if ship is within bounds
        if not (0 <= x1 <= 9 and 0 <= y1 <= 9 \
                and 0 <= x2 <= 9 and 0 <= y2 <= 9):
            print("ERROR: ship out-of-bounds: " + line)
            return False
        
        # Check if ship is horizontal or vertical
        if not (x1 == x2 or y1 == y2):
            print("ERROR: ship not horizontal or vertical: " + line)
            return False
        
        # Calculate ship positions
        positions = []
        if x1 == x2:
            start = min(y1, y2)
            end = max(y1, y2)
            if end - start + 1 != {"A": 5, "B": 4, "S": 3,
                                    "D": 3, "P": 2}[kind]:
                print("ERROR: incorrect ship size: " + line)
                return False
            for y in range(start, end + 1):
                positions.append((x1, y))
        else:
            start = min(x1, x2)
            end = max(x1, x2)
            if end - start + 1 != {"A": 5, "B": 4, "S": 3,\
                                    "D": 3, "P": 2}[kind]:
                print("ERROR: incorrect ship size: " + line)
                return False
            for x in range(start, end + 1):
                positions.append((x, y1))
        
        # Check for overlap
        for x, y in positions:
            if self.grid[x][y].ship is not None:
                print("ERROR: overlapping ship: " + line)
                return False
        
        # Place ship
        ship = Ship(kind, positions)
        for x, y in positions:
            self.grid[x][y].ship = ship
        self.ships.append(ship)
        return True
    
    def process_guess(self, x, y):
        """Process a guess and return if game is over.
        
        Args:
            x (int): X-coordinate of guess.
            y (int): Y-coordinate of guess.
        
        Returns:
            bool: True if all ships are sunk, False otherwise.
        """
        # Check if guess is legal
        if not (0 <= x <= 9 and 0 <= y <= 9):
            print("illegal guess")
            return False
        
        pos = self.grid[x][y]
        was_guessed = pos.guessed
        pos.guessed = True
        
        if pos.ship is None:
            if not was_guessed:
                print("miss")
            else:
                print("miss (again)")
            return False
        
        # Handle ship hit
        if was_guessed:
            print("hit (again)")
        else:
            pos.ship.hits += 1
            if pos.ship.hits < pos.ship.size:
                print("hit")
            else:
                print(f"{pos.ship.kind} sunk")
        
        # Check if all ships are sunk
        for ship in self.ships:
            if ship.hits < ship.size:
                return False
        print("all ships sunk: game over")
        return True
    
    def __str__(self):
        """Return string representation of the game board.
        
        Returns:
            str: Board layout with rows from y=9 to y=0.
        """
        result = []
        for y in range(9, -1, -1):
            row = []
            for x in range(10):
                row.append(str(self.grid[x][y]))
            result.append(" ".join(row))
        return "\n".join(result)

def main():
    """Main function to run the Battleship game."""
    # Read placement file
    placement_file = input()
    board = Board()
    ship_count = 0
    valid_fleet = True
    
    file = open(placement_file, "r")
    for line in file:
        parts = line.strip().split()
        if len(parts) != 5:
            print("ERROR: fleet composition incorrect")
            valid_fleet = False
            break
        kind = parts[0]
        x1 = int(parts[1])
        y1 = int(parts[2])
        x2 = int(parts[3])
        y2 = int(parts[4])
        if not board.add_ship(kind, x1, y1, x2, y2, line.strip()):
            valid_fleet = False
            break
        ship_count += 1
    file.close()
    
    # Only process guesses if fleet is valid and complete
    if not valid_fleet or ship_count != 5:
        if valid_fleet:
            print("ERROR: fleet composition incorrect")
        return
    
    # Read guess file
    guess_file = input()
    file = open(guess_file, "r")
    for line in file:
        parts = line.strip().split()
        if len(parts) != 2:
            print("illegal guess")
            continue
        x = int(parts[0])
        y = int(parts[1])
        if board.process_guess(x, y):
            break
    file.close()
main()