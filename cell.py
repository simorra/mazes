class Cell:
    """A cell in a grid, with an id and a list of neighbouring cells."""
    def __init__(self, id: int) -> None:
        self.id = id
        self.neighbours = []
        self.visited = False

    def __repr__(self) -> str:
        return f'Cell({self.id})'