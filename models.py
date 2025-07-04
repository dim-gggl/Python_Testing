from flask import flash


__all__ = ['Club', 'Competition', 'CompetitionPlace']


class Club:

    def __init__(self, name, email, points):
        self.name = name
        self.email = email
        self.points = int(points)
        self.competition_places = []

    def has_maximum_competition_places_for_competition(self, competition):
        """
        Check if the club has the maximum number of places (12) 
        for a competition
        """
        total_places = 0
        for place in self.competition_places:
            if place.competition.name == competition.name:
                total_places += place.number
        return total_places >= 12

    def add_competition_place(self, competition_place, number):
        """
        Add places for a competition with maximum verification
        """
        if isinstance(competition_place, CompetitionPlace):
            current_places = 0
            for place in self.competition_places:
                if place.competition.name == competition_place.competition.name:
                    current_places += place.number
            
            if current_places + number > 12:
                print(
                    f"Cannot add {number} places. "
                    f"The club already has {current_places} places for this "
                    f"competition. "
                    f"Maximum allowed: 12"
                )
                return
            
            self.competition_places.append(competition_place.add_number(number))
        else:
            print(
                "competition_place must be an instance of CompetitionPlace"
            )
            return
    
    def get_places_for_competition(self, competition_name):
        """Return the total number of places for a competition"""
        total_places = 0
        for place in self.competition_places:
            if place.competition.name == competition_name:
                total_places += place.number
        return total_places
    
    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "points": self.points
        }

    def get_competition_places(self):
        return self.competition_places

    def __str__(self):
        return (
            f"Club: {self.name}, Email: {self.email}, "
            f"Points: {self.points}"
        )

    def __repr__(self):
        return f"<Club name: {self.name}>"


class Competition:

    def __init__(self, name, date, number_of_places):
        self.name = name
        self.date = date
        self.number_of_places = int(number_of_places)

    @property
    def is_complete(self):
        return self.number_of_places == 0
    
    def to_dict(self):
        return {
            "name": self.name,
            "date": self.date,
            "number_of_places": self.number_of_places
        }

    def __str__(self):
        return (
            f"Competition: {self.name}, Date: {self.date}, "
            f"Number of places: {self.number_of_places}"
        )
    
    def __repr__(self):
        return f"<Competition name: {self.name}>"


class CompetitionPlace:

    def __init__(self, competition):
        self.competition = competition
        self.number = 0
    
    def add_number(self, number):
        """Add a number of places to this instance"""
        self.number = number
        return self
    
    def to_dict(self):
        return {
            self.competition.name : self.number
        }

    def __str__(self):
        return f"Competition place for: {self.competition.name}"
    
    def __repr__(self):
        return f"<CompetitionPlace for: {self.competition.name}>"