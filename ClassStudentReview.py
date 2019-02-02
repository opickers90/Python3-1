class Student:
  
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = [] # type: List
    self.attendance = {}  # type: Dict
  
  def __repr__(self):
    return "{0} is in year {1}. This student's grades are {2}.".format(self.name, self.year, self.grades)
      
  def add_grade(self, grade):
    self.grade = grade
    if type(self.grade) == Grade: 
      self.grades.append(self.grade.score) # attribute from Grade
  
  def get_average(self):
    return "{0}'s average is {1}.".format(self.name, sum(self.grades) / len(self.grades))
  
  
class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
    
  def is_passing(self):
    return self.score >= self.minimum_passing
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

for i in range(95, 101):
    pieter.add_grade(Grade(i))

pieter.attendance["2019-01-08"] = True
pieter.attendance["2019-01-07"] = False

print(roger)
print(sandro)
print(pieter)
thumbs_up = Grade(99)
thumbs_down = Grade(64)

print(pieter.get_average()) # use get_average() vice get_average
# print(pieter.get_average) # uncomment this to see what prints
print(thumbs_up.is_passing()) # True for this example
print(thumbs_down.is_passing())

print(pieter.attendance)


