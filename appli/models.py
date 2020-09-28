from django.db import models
import datetime
#Définition des max pour pouvoir les stocker et les réutiliser
class User(models.Model):
    username=models.CharField(max_length=100)
    max_squat=models.FloatField(default=20)
    max_deadlift=models.FloatField(default=20)
    max_overhead_press=models.FloatField(default=20)
    max_bench_press=models.FloatField(default=20)

    def __str__(self):
        return '%s'%(self.username)

class Program(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    program_name=models.CharField(max_length=200)

    def __str__(self):
        return '%s'%(self.program_name)

class Daily_record(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateField(default=datetime.datetime.now())
    week_number=models.IntegerField(default=1)
    exercise=models.CharField(max_length=200)
    reps_number=models.IntegerField(default=1)
    weight=models.FloatField(default=20)
    max_of_the_day=models.FloatField(default=20)

    def __str__(self):
        return '%s %s %s %s %s'%(self.user, self.date, self.reps_number, self.weight, self.max_of_the_day)


#Définition de la routine hebdomadaire(week_number : numéro de semaine, utile pour un programme du type 531)
class Weekly_routine(models.Model):
    week_number=models.IntegerField(default=1)
    rest_time=models.IntegerField(default=3)
    number_sets=models.IntegerField(default=3)
    number_reps_set1=models.IntegerField(default=10)
    number_reps_set2=models.IntegerField(default=10)
    number_reps_set3=models.IntegerField(default=10)



                





    

    
    

    




    





    









