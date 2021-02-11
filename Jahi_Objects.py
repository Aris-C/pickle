class Me:
    
    def __init__(self, name, school, grade):
        self.name = name
        self.school = school
        self.grade = grade
    def printMe(info):
        print ('My name is: ', info.name)
        print ('My school is: ', info.school)
        print ('Im in: ', info.grade)
    


yuh = Me("Aris", "BHS", "10th grade")
baba = Me("Baba", "HGP", "Elder")
yuh.printMe()
baba.printMe()


