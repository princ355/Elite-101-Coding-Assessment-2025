
# ------------------------------------------------------------------------------------
# The following 2D lists mimic a restaurant seating layout, similar to a grid.
# 
# - Row 0 is a "header row":
#     - The first cell (index 0) is just a row label (0).
#     - The remaining cells are table labels with capacities in parentheses,
#       e.g., 'T1(2)' means "Table 1" has capacity 2.
#
# - Rows 1 through 6 each represent a distinct "timeslot" or "seating period":
#     - The first cell in each row (e.g., [1], [2], etc.) is that row's label (the timeslot number).
#     - Each subsequent cell shows whether the table (from the header row) is
#       free ('o') or occupied ('x') during that timeslot.
#
# In other words, restaurant_tables[row][column] tells you the status of a
# particular table (column) at a particular timeslot (row).
# ------------------------------------------------------------------------------------

# Shows the structure of the restaurant layout with all tables free ("o" = open).
restaurant_tables = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'o',      'o',      'o',      'o',      'o',      'o'],
    [2,        'o',      'o',      'o',      'o',      'o',      'o'],
    [3,        'o',      'o',      'o',      'o',      'o',      'o'],
    [4,        'o',      'o',      'o',      'o',      'o',      'o'],
    [5,        'o',      'o',      'o',      'o',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'o',      'o']
]

# ------------------------------------------------------------------------------------
# This second layout serves as a test case where some tables ('x') are already occupied.
# Use this for testing your logic to:
#   - Find free tables (marked 'o')
#   - Check if those tables meet a certain capacity (from the header row, e.g. 'T1(2)')
#   - Potentially combine adjacent tables if one alone isn't enough for a larger party.
# ------------------------------------------------------------------------------------

restaurant_tables2 = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'x',      'o']
]

start
def level_1 (tables, timeslot):
    """
    Level 1 
   Goal: List all tables that are currently free (‘o’ in the chosen timeslot)
   Output: A list of table IDs (or the entire table object) representing free tables.
    """
    #initialize output
    output = []
    #get header row in table
    header = tables[0]
    #run through each table in timeslot row
    timeslot_row= tables[timeslot]
    for i in range(1, len(timeslot_row)):
        #check for empty tables
        if timeslot_row[i] == 'o':
            #if found, store in output
            output.append(header[i])
    
    #return output
    return output

def level_2 (party_size, tables):
    """
    Goal: Given a party size (e.g., 2, 3, 4 people), find one table that can seat at least that many people (i.e., capacity >= party_size) and is free.
    Output: Return a single table (or table ID) that fits the requirement.
    """
    #initialize output
    output = []
    #get header row
    header = tables[0]
    #loop through each table in header
    for table in header:
        #check if each table capacity is greater than or equal to party size
        if int( table[table.index("(")+1 : table.index(")")] ) >= party_size:
            #add table to output
            output.append(table)
    #return output
    return output

def level_3 (tables, party_size, timeslot):
    """
    Goal: Given a party size, return all tables that can seat that many people and are free.
    """
    #initialize output
    output = []
    #get all tables that are free in timeslot into list 1
    list_one = level_1(tables, timeslot)
    #get all tables with capacity greater than or equal to capacity size into list 2
    list_two = level_2 (party_size, tables)
    #look through each table in list one
    for table in list_one:
        #if the table is in list 2
        if table in list_two:
            #add table to output
            output.append(table)
    #return output
    return output

def level_4 ()
    """
    Goal: Some restaurants can combine two adjacent tables if one table alone isn’t big enough.
    If a single table can’t seat the group, check if two adjacent tables combined have enough capacity.
    Output: A list of all table combinations (single or adjacent pairs) that can seat the party.
    """
    #initialize output
    output = []
    #get header row
    header = tables[0]
    #intialize past capacity
    past_capacity = 0
    #loop through each table in header
    for table in header:
        #check if each table capacity is greater than or equal to party size
        capacity = int( table[table.index("(")+1 : table.index(")")] )
        if capacity >= party_size:
            #add table to output
            output.append(table)
        else: 
            #if past capacity plus current capacity  greater than or equal to party size
            if past_capacity + capacity >= party_size:
                #add table to output
                output.append(table)
        #update past capacity with current capacity 
        past_capacity = capacity
    #return output
    return output
