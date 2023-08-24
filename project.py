class Match:
    def __init__(self, date, team1, team2, location):
        self.date = date
        self.team1 = team1
        self.team2 = team2
        self.location = location

class MatchDatabase:
    def __init__(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def list_matches_by_team(self, team_name):
        matches_of_team = [match for match in self.matches if team_name in [match.team1, match.team2]]
        return matches_of_team

    def list_matches_by_location(self, location):
        matches_at_location = [match for match in self.matches if match.location == location]
        return matches_at_location

    def list_matches_by_timing(self, timing):
        matches_at_timing = [match for match in self.matches if timing in match.date]
        return matches_at_timing

def main():
    match_db = MatchDatabase()

    # Add sample match data
    match_db.add_match(Match("2023-08-25 18:00", "Team A", "Team B", "Stadium X"))
    match_db.add_match(Match("2023-08-26 15:30", "Team C", "Team D", "Stadium Y"))
    # Add more matches...

    while True:
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            team_name = input("Enter the team name: ")
            matches_of_team = match_db.list_matches_by_team(team_name)
            for match in matches_of_team:
                print(f"{match.team1} vs {match.team2} on {match.date} at {match.location}")

        elif choice == "2":
            location = input("Enter the location: ")
            matches_at_location = match_db.list_matches_by_location(location)
            for match in matches_at_location:
                print(f"{match.team1} vs {match.team2} on {match.date} at {match.location}")

        elif choice == "3":
            timing = input("Enter the timing: ")
            matches_at_timing = match_db.list_matches_by_timing(timing)
            for match in matches_at_timing:
                print(f"{match.team1} vs {match.team2} on {match.date} at {match.location}")

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
