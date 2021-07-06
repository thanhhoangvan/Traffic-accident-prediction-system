#----------------------------------------------
# Author: Thanh HoangVan 
# Email: thanh.hoangvan051199@gmail.com
# Ha Noi University of Science and Technology
#----------------------------------------------

# import library
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Account for login
Accounts={
    "admin": "admin",
    "thanhhoangvan": "admin"
}

# Check login infor
def Verify(username, password):
    if (username in Accounts.keys()) and (password == Accounts[username]):
        return True
    else:
        return False

# Processing login request
def login(request):
    if request.method == "POST":
        usr = request.POST["username"]
        passwd = request.POST["password"]
        if Verify(usr, passwd):
            return render(request, "databoard/index.html")
        else:
            return render(request, "login/index.html")
    elif request.method == "GET":
        return render(request, "login/index.html")

# Input page
def InputData(request):
        return render(request, "input/index.html")

def ResultAnalysis(request):
    today = date.today()
    hh = int(today.strftime("%H"))
    if request == 'post':
        if 'hour' in request.POST:
            hour = request.POST['hour']

            return render(request, "result/index.html")

    return render(request, "result/index.html")

# Analysis page
def Analysis(request):
    if request.method == "POST":

        # Time input
        day = request.POST['day']
        month = request.POST['month']
        year = request.POST['year']

        # Weather input
        Weather = request.POST['Weather']
        return render(request, "result/index.html")

    else:
        today = date.today()
        dd = int(today.strftime("%d"))
        mm = int(today.strftime("%m"))
        yyyy = int(today.strftime("%Y"))
        return render(request, "analysis/index.html", {'day': dd, 'month': mm, 'year': yyyy})

# Databoard page
def Databoard(request):
    return render(request, "databoard/index.html")