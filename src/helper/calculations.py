from model.Location import Location


def get_middle_point(l1, l2):
    """
    Calculates a new location which is in the middle of two points.
    :return: New location
    """
    row = (l1.row + l2.row) / 2
    column = (l1.column + l2.column) / 2
    return Location(row, column)


def calculate_offset(location_1, location_2):
    """
    Calculates the offset between two points.
    :param location_1: First location on the board
    :param location_2: Second location on the board
    :return: Location containing the row and column offsets
    """
    row_offset = abs(location_1.row - location_2.row)
    column_offset = abs(location_1.column - location_2.column)
    return Location(row_offset, column_offset)
