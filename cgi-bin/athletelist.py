
class AthleteList(list):

    def __init__(self, a_name,a_ename, a_dob=None, a_movie=None):
        list.__init__([])
        self.name = a_name
        self.ename = a_ename
        self.dob = a_dob
        self.movie = a_movie

    @staticmethod
    def sanitize(time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return(time_string)
        (mins, secs) = time_string.split(splitter)
        return(mins + '.' + secs)

    @property
    def top3(self):
        return(sorted(set([self.sanitize(t) for t in self]))[0:3])

    @property
    def clean_data(self):
        return(sorted(set([self.sanitize(t) for t in self])))
