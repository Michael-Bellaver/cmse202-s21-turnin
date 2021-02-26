# The Student class (you'll edit and expand on this)
class Student():
    '''
    This class is designed to include information about individual students.
    Currently this class has the following attributes:
    
    name : this is the student's name
    gpa : this is the student's curret gpa
    '''
    
    def __init__(self, name='', gpa=0.0, year=0):
        self.name = name
        self.gpa = gpa
        self.year = year
        
    def get_name(self):
        '''
        This function prints the name of the student
        '''
        return "My name is", self.name 
    
    def enroll(self, courses=[]):
        self.courses = courses
        return
    
    def display_courses(self):
        return "I am enrolled in", self.courses
    
    def years_until_graduation(self):
        return ("I will graduate in", 4.0-self.year, 'years')
    
class Spartan(Student):
    
    def __init__(self, name):
        self.name = name
        return
    def set_motto(self, motto):
        self.motto = motto
        return
    def school_spirit(self):
        return 'My name is', self.name, 'I am a Spartan. My motto is', self.motto