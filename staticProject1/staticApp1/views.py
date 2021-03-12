from django.shortcuts import render
def view1(request):
    myName="RAMYASHREE"
    favPlayer="virat"
    favSubject="python"
    favAnimal="Tiger"
    d={'name':myName,'player':favPlayer,'animal':favAnimal,'subject':favSubject}
    return render(request,'staticApp1/1.html',d)

# Create your views here.
