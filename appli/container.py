#Definition of the big four exercises
class Exercise:
    def __init__(self, name):
        self.name=name

squat=Exercise(name='Squat')
deadlift=Exercise(name='Deadlift')
overhead=Exercise(name='Overhead Press')
bench=Exercise(name='Bench Press')

#Max definition for the big four exercises
class Max:
    def __init__(self, name, value):
        self.name=name
        self.value=value

max_squat=Max(name='Squat', value=100)
max_deadlift=Max(name='Deadlift', value=100)
max_overhead=Max(name='Overhead Press', value=100)
max_bench=Max(name='Bench Press', value=100)


#Definition of the weekly routine
class Week:
    def __init__(self, number, percentage_set1, reps_set1, percentage_set2, reps_set2, percentage_set3, reps_set3):
        self.number=number
        self.percentage_set1=percentage_set1
        self.reps_set1=reps_set1
        self.percentage_set2=percentage_set2
        self.reps_set2=reps_set2
        self.percentage_set3=percentage_set3
        self.reps_set3=reps_set3


week1=Week(number=1, percentage_set1=0.65, reps_set1=5, percentage_set2=0.75,reps_set2=5, percentage_set3=0.85,reps_set3=5)
week2=Week(number=2, percentage_set1=0.70,reps_set1=3, percentage_set2=0.80,reps_set2=3, percentage_set3=0.90,reps_set3=3)
week3=Week(number=3, percentage_set1=0.75,reps_set1=5, percentage_set2=0.85,reps_set2=3, percentage_set3=0.95,reps_set3=1)
week4=Week(number=4, percentage_set1=0.50,reps_set1=5, percentage_set2=0.55,reps_set2=5, percentage_set3=0.60,reps_set3=5)


