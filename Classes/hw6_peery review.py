# ----------------------------------------------------------------------
# Name:        homework_6
# Purpose:     Define the movie class
#
# Date:        3/2/19
# ----------------------------------------------------------------------
"""
Module containing a Movie class definition.

__getitem__ to access individual scenes, like scene selection.
__len__ to return the number of minutes in the movie.
__init__ to initialize instances.
__str__ to return a readable representation of the movie.
__add__ to return the information of both movies
add_scene adds a scene and description to the movie scene dict
from_tuple class method to create a movie object from a tuple


"""


class Movie(object):
    """
    Represent a movie

    Arguments:
    director (string): the director's name
    title (string): the movie title
    duration (int): the length of the movie in minutes

    Attributes:
    director (string): the director's name
    title (string): the movie title
    duration (int): the length of the movie in minutes
    scenes (dictionary):  keys are scene names, values are descriptions
    of the scene
    """

    medium = 'Film'  # class variable

    def __init__(self, director, title, duration):
        self.director = director
        self.title = title
        self.duration = duration
        self.scenes = {}

    def __str__(self):
        movie_info = [f'{self.title} Directed by: {self.director}'
                      f' Medium: {self.medium}\nDuration: '
                      f'{self.duration} min\n']

        for each_scene in self.scenes:
            movie_info.append(f'{each_scene}\n{self.scenes[each_scene]}\n')
        return '\n'.join(movie_info)

    def __lt__(self, other):
        return self.duration < other.duration

    def __eq__(self, other):
        return self.title == other.title and self.director == \
               other.director and self.duration == other.duration and \
               self.scenes == other.scenes

    def __add__(self, other):
        if self == other:
            return self
        if self.director == other.director:
            new_dir = self.director
        else:
            new_dir = self.director + ' & ' + other.director
        if self.title == other.title:
            new_title = self.title
        else:
            new_title = self.title + ' & ' + other.title
        new_dur = self.duration + other.duration
        new_movie = Movie(new_dir, new_title, new_dur)
        for scene_name in self.scenes:
            new_movie.add_scene(scene_name, self.scenes[scene_name])
        for scene_name in other.scenes:
            new_movie.add_scene(scene_name, other.scenes[scene_name])
        return new_movie

    def __len__(self):
        return self.duration

    def __getitem__(self, item):
        return getattr(self, item)

    def add_scene(self, scene_name, description):
        """
        Add the given scene as a new scene at the end of the movie.
        :param scene_name: (string) name of scene to be added
        :param description: (string) description of the scene
        :return: None
        """
        self.scenes[scene_name] = description

    @classmethod
    def from_tuple(cls, movie_tuple):
        """
        Creates a movie object from a tuple
        :param movie_tuple: (tuple) Tuple containing director name,
        title, and movie duration
        :return: (Movie) new movie object
        """
        (mov_dir, mov_title, mov_dur) = movie_tuple
        movie = cls(mov_dir, mov_title, mov_dur)
        return movie


def main():
    lotr = Movie("Peter Jackson", "Lord of the Rings", 178)
    lotr.add_scene("Fellowship of the Ring", "They start walking to Mordor")
    lotr.add_scene("Two Towers", "Mary and Pippin get lost in the woods")
    lotr.add_scene("Return of the King", "Frodo throws away the ring")

    rtol = Movie("Peter Jackson", "Lord of the Rings", 178)
    rtol.add_scene("Fellowship of the Ring", "They start walking to Mordor")
    rtol.add_scene("Two Towers", "Mary and Pippin get lost in the woods")
    rtol.add_scene("Return of the King", "Frodo throws away the ring")

    potter = Movie("Mike Newell", "Goblet of Fire", 157)
    potter.add_scene("Quidditch World Cup", "Two teams play quidditch")
    potter.add_scene("Voldemort Returns", "Harry accidentally brings "
                                          "Voldemort back to life")

    print(lotr)
    print("\n----------------------end----------------------\n")
    print(rtol)
    print("\n----------------------end----------------------\n")
    print(potter)
    print("\n----------------------end----------------------\n")

    print("lotr == rtol: ")  # True
    print(lotr == rtol)

    print("lotr < rtol: ")  # False
    print(lotr < rtol)

    print("potter == lotr: ")  # False
    print(potter == lotr)

    print("potter < lotr ")  # True
    print(potter < lotr)

    forr_gump = Movie.from_tuple(("Robert Zemeckis", "Forrest Gump", 144))
    print(forr_gump)

    print("len(potter)")    # 157
    print(len(potter))

    print("forr_gump['title']")  # Forrest Gump
    print(forr_gump["title"])

    print("forr_gump + potter") 
    comb_movie = forr_gump + potter
    print(comb_movie)
    print("\n----------------------end----------------------\n")

    print("lotr + rtol")
    comb_lotr = lotr + rtol
    print(comb_lotr)
    print("\n----------------------end----------------------\n")

    print("lotr + potter")
    print(lotr + potter)
    print("\n----------------------end----------------------\n")


if __name__ == "__main__":
    main()

