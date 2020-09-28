from django import forms

class Formulaire(forms.Form):
    choix_max_squat={}
    for poids in range(0,200,5):
        choix_max_squat[poids,poids]=(
            (poids,poids),
        )

    choix_max_deadlift={}
    for poids in range(0,200,5):
        choix_max_deadlift[poids,poids]=(
            (poids,poids),
        )

    choix_max_bench={}
    for poids in range(0,200,5):
        choix_max_bench[poids,poids]=(
            (poids,poids),
        )

    choix_max_overhead={}
    for poids in range(0,200,5):
        choix_max_overhead[poids,poids]=(
            (poids,poids),
        )

    max_squat=forms.ChoiceField(choices=choix_max_squat)
    max_deadlift=forms.ChoiceField(choices=choix_max_deadlift)
    max_bench=forms.ChoiceField(choices=choix_max_bench)
    max_overhead=forms.ChoiceField(choices=choix_max_overhead)





