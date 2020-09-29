from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from appli import models
from django.db.models import Q
from appli.Functions.percentages_calculator import percentages_calculator
from appli import container
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from appli.forms import Formulaire
import datetime
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.http import JsonResponse
from appli.models import Daily_record, User
import datetime



def home_view(request):
    return render(request, 'appli/homeview.html', {})

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('login')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(home_view) 
    else:
        return render(request, 'registration/login_view.html', {})
    return render(request, 'registration/login_view.html', {})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            User.objects.create(username=username)
            return redirect(home_view)
        else:
            print(form.is_valid())
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def options(request):
    if request.method == 'POST':
        form = Formulaire(request.POST)
        if form.is_valid():
            #getting form results
            max_squat=form.cleaned_data.get('max_squat')
            max_deadlift=form.cleaned_data.get('max_deadlift')
            max_overhead=form.cleaned_data.get('max_overhead')
            max_bench=form.cleaned_data.get('max_bench')
            user_save=User(username=request.user, max_squat=max_squat, max_deadlift=max_deadlift, max_overhead_press=max_overhead, max_bench_press=max_bench)
            user_save.save()
            program_save=Program(user=user_save)
            program_save.save()                        
            context={
                'max_squat':max_squat,  'max_deadlift':max_deadlift, 'max_bench':max_bench,  'max_overhead':max_overhead, 'programme':programme} 
            return redirect(options)
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = Formulaire()

    return render(request, 'appli/options.html', {'form':form})


def program(request): 
    third_set_possibilities=range(0,20)
    name_reps_array=[]
    test=[1,2,3,4,5]
    #print(test)        
    if request.method=='POST':
        if 'last_serie' in request.POST :
            #Récupérer toutes les valeurs de la dernière série(même celles qui sont nulles, puis ne garder que la seule valeur non nulle(celle qui nous intéresse))
            reps_last_serie_array=request.POST.getlist('nombre_reps')
            name_exo_array=request.POST.getlist('name_exo')
            #print(reps_last_serie_array, name_exo_array)
            for i in range(len(reps_last_serie_array)):
                name_reps_array.append([reps_last_serie_array[i], name_exo_array[i]])
            #print(name_reps_array)
            for i in name_reps_array:
                if i[0]=='0':
                    continue
                else:
                    reps_number=i[0]
                    name_exo=i[1]
            weight=request.POST.get('last_serie')
            weight=float(weight)
            reps_number=int(reps_number)
            max_of_the_day=(weight/(1.0278-0.0278*reps_number))
            #print(User.objects.all())
            if User is not None:
                current_user=User.objects.filter(username=request.user).latest('id')
            else:
                current_user='testuser'
            data_to_save=Daily_record(id=None, user=current_user, date=datetime.date.today(), exercise=name_exo, reps_number=reps_number, weight=weight, max_of_the_day=max_of_the_day)
            data_to_save.save()
            #print(Daily_record.objects.all())
        return redirect(home_view)
        
    return render(request, 'appli/programme_force.html', {
        'program_week1':percentages_calculator(week='week1'), 
        'program_week2':percentages_calculator(week='week2'),
        'program_week3':percentages_calculator(week='week3'),
        'program_week4':percentages_calculator(week='week4'),
        'third_set_possibilities':third_set_possibilities,
        })

def history(request):
    if Daily_record is not None:
        queryset=Daily_record.objects.filter(user__username=request.user).values_list('user__username', 'date', 'exercise', 'reps_number', 'weight', 'max_of_the_day')
    else:
        queryset=['testuser']
    legend_array=['Username', 'Date', 'Exercise', 'Number of reps', 'Weight lifted', '1RM']
    return render(request, 'appli/history.html', {'all_perfs': queryset, 'legend_table':legend_array})


def chart_view(request):
    return render(request, 'appli/chart_view.html')


def line_chart(request):
    dates_array=[]
    if Daily_record is not None:
        find_date_queryset=Daily_record.objects.filter(user__username=request.user).values_list('date', flat=True)
    else:
        find_date_queryset=datetime.now()
    #dates_array
    for date in find_date_queryset:
        dates_array.append(date)
    
    #providers
    providers=['Squat', 'Deadlift', 'Overhead Press', 'Bench Press']
    
    #data_for_chart_array
    if Daily_record is not None:
        find_squat_queryset=Daily_record.objects.filter(user__username=request.user).filter(exercise='Squat').values_list('max_of_the_day', flat=True)
        find_deadlift_queryset=Daily_record.objects.filter(user__username=request.user).filter(exercise='Deadlift').values_list('max_of_the_day', flat=True)
        find_overhead_queryset=Daily_record.objects.filter(user__username=request.user).filter(exercise='Overhead Press').values_list('max_of_the_day', flat=True)
        find_bench_queryset=Daily_record.objects.filter(user__username=request.user).filter(exercise='Bench Press').values_list('max_of_the_day', flat=True)
    else:
        find_squat_queryset=[20]
        find_bench_queryset=[20]
        find_overhead_queryset=[20]
        find_bench_queryset=[20]


    squat_array=[]
    deadlift_array=[]
    overhead_array=[]
    bench_array=[]
    for max_of_the_day_squat in find_squat_queryset:
        squat_array.append(max_of_the_day_squat)

    for max_of_the_day_deadlift in find_deadlift_queryset:
        deadlift_array.append(max_of_the_day_deadlift)

    for max_of_the_day_overhead in find_overhead_queryset:
        overhead_array.append(max_of_the_day_overhead)

    for max_of_the_day_bench in find_bench_queryset:
        bench_array.append(max_of_the_day_bench)
    
    data_for_chart_array=[squat_array, deadlift_array, overhead_array, bench_array]
    print(data_for_chart_array)

    return JsonResponse(data={
        'labels':dates_array,
        'data':data_for_chart_array,
        'providers':providers,
    })

    

        






    
   