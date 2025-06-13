'''
File: dates.py
Author: venna mani abhiram reddy

Course: CSC 120, Spring 2025

Goal: A collection of dates and associated events are
 managed and processed by this program. 
In addition to normalizing date formats and enabling 
the addition of new events or 
the retrieval of events for particular dates, 
it reads dates and events from a file.
 On the identical moment, the program manages several 
events and prints them in a sorted order.
'''
class Date:
    '''
    The program handles dates through this class that
    both represents specific days and stores related events.
    The class contains a date formatted as YYYY-MM-DD
    together with a list of events linked to the date.
    The class holds an adaptive structure for events whereas
    it presents the sorted date events and their string
    representation through dynamic input methods.
    Attributes:
        date_str (str): The date in canonical format (YYYY-MM-DD).
        The events (list) contains strings which identify the
        particular events related to this date.
    '''
    def __init__(self, date_str, event):
        '''
        The function initializes a Date object by
        combining canonical date values with the initial event data.
        Args:
            date_str (str): The date in canonical format (YYYY-MM-DD).
            This statement initializes a Date object with
            parameters for the specified event and date (str).
        Returns:
            None.
    '''
        self.date_str = date_str
        self.events = []
        self.add_event(event)  # Add the initial event

    def add_event(self, event):
        '''
        Add an event to the list of events for this date.

        Args:
            event (str): The event to be added.

        Returns:
            None.
        '''
        # Add event (no sorting here)
        self.events.append(event)
    def __str__(self):
        '''
        The method should transform the Date object into a
        string presenting its events while using
        alphabetical order for listings.

        Returns:
            The function returns a string which
            displays the date followed by its events as
            separate lines.
            '''
        result = ""
        # Sort events alphabetically when retrieving
        for event in sorted(self.events):
            result += f"{self.date_str}: {event}\n"
        # Remove trailing newline
        return result.strip()
class DateSet:
    '''
    The class functions as a collection manager for Date objects.

    The class contains various Date objects stored in a
    dictionary format using canonical date
    strings (YYYY-MM-DD) as keys.
    The library enables event addition tools
    for particular dates.
    The class allows users to obtain
    events associated with a particular date.

    Attributes:
        This class utilizes dict as its data type
        which employs YYYY-MM-DD canonical strings
        as dictionary keys.
        values are Date objects.
    '''

    def __init__(self):
        '''
        The application needs to instantiate an
        object of the DateSet class to store
        various Date elements.

        Returns:
            None.
        '''
        # Dictionary to store Date objects
        self.dates = {}
    def add_date(self, date_str, event):
        '''
        The DateSet gets a new date entry
        which includes its linked event.
        The DateSet contains this date so the
        event adds to the existing Date object.
        Date object. The function establishes a
        new Date object when it fails to
        find the specified date.
        Args:
            date_str (str): The date in canonical format (YYYY-MM-DD).
            The program will log this date along with
            the mentioned event (str).

        Returns:
            None.
        '''
        if date_str not in self.dates:
            self.dates[date_str] = Date(date_str, event)
        else:
            self.dates[date_str].add_event(event)

    def __str__(self):
        '''
        Render a text representation of the DateSet containing
        chronological date sorting.

        Returns:
            The formatted string provides all dates alongside their
            linked events through separate lines.
        '''
        result = ""
        # Sort dates when retrieving
        for date in sorted(self.dates):
            result += str(self.dates[date]) + "\n"
        # Remove trailing newline
        return result.strip()


def canonicalize_date(date_str):
    '''
    This function transforms date strings of diverse
    formats into standardized YYYY-MM-DD format.

    Supported formats:
    - YYYY-MM-DD
    - MM/DD/YYYY
    - MonthName DD, YYYY (e.g., "October 5, 2023")
    The date string appears in the format of
    Abbreviated MonthName DD, YYYY (such as "Oct 5, 2023").

    Args:
        The input date string
        date_str takes the form of a string value.

    Returns:
        The function returns a canonical date
        format as YYYY-MM-DD yet returns None
        when it detects an invalid date format.
    '''
    # Remove leading/trailing whitespace
    date_str = date_str.strip()
    if '-' in date_str:
        parts = date_str.split('-')
        if len(parts) == 3:
            year, month, day = parts
            # Convert to canonical format
            return f"{int(year)}-{int(month)}-{int(day)}"
    elif '/' in date_str:
        parts = date_str.split('/')
        if len(parts) == 3:
            month, day, year = parts
            # Convert to canonical format
            return f"{int(year)}-{int(month)}-{int(day)}"
    else:
        parts = date_str.split()
        if len(parts) == 3:
            month_name, day, year = parts
            month_names = {
                'January': 1, 'February': 2, 'March': 3, 'April': 4,
                'May': 5, 'June': 6, 'July': 7, 'August': 8,
                'September': 9, 'October': 10, 'November': 11,
                'December': 12,
                'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
                'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
                'Nov': 11, 'Dec': 12
            }
            if month_name in month_names:
                # Convert to canonical format
                return f"{int(year)}-{month_names[month_name]}-{int(day)}"
    return None
def read_file(filename):
    '''
    The program reads files by processing
    their data to insert or fetch events.

    From every line the file contains a
    single entity which presents itself as either:
    The I (insert) instruction enables
    users to incorporate new events.
    The function supports displaying events
    through the 'R' (retrieve) command for a selected date.

    Args:
        The program processes file data from the specified string filename.

    Returns:
        None.
    '''
    # Create a DateSet to store events
    date_set = DateSet()
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    # loop through every line in the file
    for line in lines:
        line = line.strip()
        if line:
            # Insert operation
            if line[0] == 'I':
                if ':' in line:
                    date_part, event = line[1:].split(':', 1)
                    date_str = canonicalize_date(date_part.strip())
                    if date_str:
                        date_set.add_date(date_str, event.strip())
                    else:
                        print(f"Error - Illegal operation.")
                else:
                    print(f"Error - Illegal operation.")
            # Retrieve operation
            elif line[0] == 'R':
                date_str = canonicalize_date(line[1:].strip())
                if date_str and date_str in date_set.dates:
                    print(date_set.dates[date_str])
            else:
                print(f"Error - Illegal operation.")
def main():
    filename = input()
    read_file(filename)
main()