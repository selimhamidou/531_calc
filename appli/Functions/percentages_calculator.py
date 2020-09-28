from appli.models import User
from appli import container
from appli.container import week1, week2, week3, week4

if User is not None:
    max_squat=User.objects.values_list('max_squat', flat=True).latest('id')
    max_deadlift=User.objects.values_list('max_deadlift', flat=True).latest('id')
    max_overhead=User.objects.values_list('max_overhead_press', flat=True).latest('id')
    max_bench=User.objects.values_list('max_bench_press', flat=True).latest('id')
else:
    max_squat=20
    max_deadlift=20
    max_overhead=20
    max_bench=20

def percentages_calculator(week):
    squat_week1=['Squat']
    deadlift_week1=['Deadlift']
    overhead_week1=['OverheadPress']
    bench_week1=['BenchPress']

    squat_week2=['Squat']
    deadlift_week2=['Deadlift']
    overhead_week2=['OverheadPress']
    bench_week2=['BenchPress']

    squat_week3=['Squat']
    deadlift_week3=['Deadlift']
    overhead_week3=['OverheadPress']
    bench_week3=['BenchPress']

    squat_seance4=['Squat']
    deadlift_week4=['Deadlift']
    overhead_week4=['OverheadPress']
    bench_week4=['BenchPress']

    reps_array_week1=[week1.reps_set1, week1.reps_set2, week1.reps_set3]
    percentages_array_week1=[week1.percentage_set1, week1.percentage_set2, week1.percentage_set3]

    reps_array_week2=[week2.reps_set1, week2.reps_set2, week2.reps_set3]
    percentages_array_week2=[week2.percentage_set1, week2.percentage_set2, week2.percentage_set3]

    reps_array_week3=[week3.reps_set1, week3.reps_set2, week3.reps_set3]
    percentages_array_week3=[week3.percentage_set1, week3.percentage_set2, week3.percentage_set3]

    reps_array_week4=[week4.reps_set1, week4.reps_set2, week4.reps_set3]
    percentages_array_week4=[week4.percentage_set1, week4.percentage_set2, week4.percentage_set3]

    if week=='week1':
        for i in [week1.percentage_set1, week1.percentage_set2, week1.percentage_set3]:
            squat_week1.append([reps_array_week1[percentages_array_week1.index(i)],float(max_squat)*i])
            deadlift_week1.append([reps_array_week1[percentages_array_week1.index(i)],float(max_deadlift)*i])
            overhead_week1.append([reps_array_week1[percentages_array_week1.index(i)],float(max_overhead)*i])
            bench_week1.append([reps_array_week1[percentages_array_week1.index(i)],float(max_bench)*i])        

        return (squat_week1, deadlift_week1, overhead_week1, bench_week1)

    if week=='week2':
        for i in [week2.percentage_set1, week2.percentage_set2, week2.percentage_set3]:
            squat_week2.append([reps_array_week2[percentages_array_week2.index(i)],float(max_squat)*i])
            deadlift_week2.append([reps_array_week2[percentages_array_week2.index(i)],float(max_deadlift)*i])
            overhead_week2.append([reps_array_week2[percentages_array_week2.index(i)],float(max_overhead)*i])
            bench_week2.append([reps_array_week2[percentages_array_week2.index(i)],float(max_bench)*i])
        return (squat_week2, deadlift_week2, overhead_week2, bench_week2)

    if week=='week3':
        for i in [week3.percentage_set1, week3.percentage_set2, week3.percentage_set3]:
            squat_week3.append([reps_array_week3[percentages_array_week3.index(i)],float(max_squat)*i])
            deadlift_week3.append([reps_array_week3[percentages_array_week3.index(i)],float(max_deadlift)*i])
            overhead_week3.append([reps_array_week3[percentages_array_week3.index(i)],float(max_overhead)*i])
            bench_week3.append([reps_array_week3[percentages_array_week3.index(i)],float(max_bench)*i])
            
        return (squat_week3, deadlift_week3, overhead_week3, bench_week3)

    if week=='week4':
        for i in [week4.percentage_set1, week4.percentage_set2, week4.percentage_set3]:
            squat_seance4.append([reps_array_week4[percentages_array_week4.index(i)],float(max_squat)*i])
            deadlift_week4.append([reps_array_week4[percentages_array_week4.index(i)],float(max_deadlift)*i])
            overhead_week4.append([reps_array_week4[percentages_array_week4.index(i)],float(max_overhead)*i])
            bench_week4.append([reps_array_week4[percentages_array_week4.index(i)],float(max_bench)*i])
            
        return (squat_seance4, deadlift_week4, overhead_week4, bench_week4)



            






















      
        
    


        
