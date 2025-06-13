"""
Author: mani abhiram reddy
Date: 03-04-2025
processes team data from a file, 
calculates win ratios for teams and conferences, 
and identifies the conferences with 
the highest average win ratio
"""

class Team:
    def __init__(self, line):
        """
        Initializes a Team instance.
        Parameters:
            line (str): A string containing the team's
            data (name, conference, wins, and losses).
        Returns: None.
        """
        data = self.extract_data(line)
        self.name, self.conference, self.wins, self.losses = data

    def extract_data(self, line):
        """
        Extracts team name, conference, wins, and
        losses from the input line.
        Parameters:
            line (str): A string containing the team's data.
        Returns:
            tuple: (team_name, conference, wins, losses).
        """
        words = line.split()
        conference_words = []
        i = len(words) - 1
        while i >= 0:
            if ')' in words[i]:
                break
            i -= 1
        # Now, move backward to find the start of the conference
        while i >= 0:
            conference_words.insert(0, words[i])
            if '(' in words[i]:
                break
            i -= 1
        # Join the conference words and remove parentheses
        conference = ' '.join(conference_words)[1:-1]
        # Remove conference words from the list to get the team name
        for word in conference_words:
            words.remove(word)
        wins = int(words[-2])
        losses = int(words[-1])
        team_name = ' '.join(words[:-2])
        return team_name, conference, wins, losses
    
    def win_ratio(self):
        """
        Calculates the win ratio of the team.
        Parameters: None.
        Returns:
            float: The win ratio (wins divided by total games)
            Returns 0 if no games have been played.
        """
        total_games = self.wins + self.losses
        if total_games > 0:
            return self.wins / total_games
        else:
            return 0
        
    def __str__(self):
        return f"{self.name} : {self.win_ratio():.3f}"

class Conference:

    def __init__(self, conf):
        """
        Initializes a Conference instance.
        Parameters:
            conf (str): The name of the conference.
        Returns: None.
        """
        self.name = conf
        self.teams = []
    
    def add(self, team):
        """
        Adds a team to the conference.
        Parameters:
            team (Team): An instance of the Team class.
        Returns: None.
        """
        self.teams.append(team)
    
    def win_ratio_avg(self):
        """
        Calculates the average win ratio 
        of all teams in the conference.
        Parameters: None.
        Returns:
            float: The average win ratio.
            Returns 0 if there are no teams.
        """
        if not self.teams:
            return 0
        
        total_ratio = 0
        # Loop through each team in the conference
        for team in self.teams:
            total_ratio += team.win_ratio()
        
        return total_ratio / len(self.teams)
    
    def __contains__(self, team):
        """
        Checks if a team is in the conference.
        Parameters:
            team (Team): An instance of the Team class.
        Returns:
            bool: True if the team is in the conference,
            otherwise False.
        """
        return team in self.teams
    
    def __str__(self):
        return f"{self.name} : {self.win_ratio_avg()}"

class ConferenceSet:
    def __init__(self):
        self.conferences = {}
    
    def add(self, team):
        """
        Adds a team to the appropriate 
        conference in the ConferenceSet.
        Parameters:
            team (Team): An instance of 
            the Team class.
        Returns: None.
        """
        if team.conference not in self.conferences:
            self.conferences[team.conference] = Conference(team.conference)
        self.conferences[team.conference].add(team)
    
    def best(self):
        """
        Finds the conferences with the highest average win ratio.
        Parameters:conferences with the highest average win ratio.
        Returns:
            list: A list of Conference instances with the
            highest average win ratio, sorted alphabetically.
        """
        if not self.conferences:
            return []
        # Find the maximum average win ratio
        max_ratio = 0
        # Loop through each conference in the ConferenceSet
        for conf in self.conferences.values():
            ratio = conf.win_ratio_avg()
            if ratio > max_ratio:
                max_ratio = ratio
        best_confs = []
        # Loop through each conference again
        for conf in self.conferences.values():
            if conf.win_ratio_avg() == max_ratio:
                best_confs.append(conf)
        def get_conference_name(conf):
            return conf.name
        best_confs.sort(key=get_conference_name)
        return best_confs
def main():
    """
    Main function to read team data from a 
    file and print the best conferences.
    Parameters:  Reads team data from a file,
    processes it, and prints the best conferences
    Returns: best conferences
    """
    filename = input()
    conference_set = ConferenceSet()
    # Open the file manually
    file = open(filename, "r")
    # Read and process each line
    for line in file:
        line = line.strip()
        if line.startswith('#') or not line:
            continue
        team = Team(line)
        conference_set.add(team)
    file.close()
    # Find and print the best conferences
    best_conferences = conference_set.best()
    for conf in best_conferences:
        print(conf)
main()