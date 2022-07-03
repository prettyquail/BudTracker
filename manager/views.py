from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TaskForm
from django.contrib import messages
from core.models import Account, Task, Progress, Blocker_Answer, Blocker
from collections import defaultdict

# Create your views here.
@login_required(login_url='login')
def manager_home(request):
    data = Progress.objects.filter(status="COMPLETED")
    li = defaultdict(list)
    for temp in data:
        li[temp.intern_id].append(temp.points)

    dic = {}
    for key,value in li.items():
        dic[key] = sum(value)/len(value)
    context = {
        "data":data,
        "dic":dic,
    }
    for temp in dic:
        print(dic[temp])
    return render(request,"manager_home.html",context)

def send_interns_info(request):
    interns = Account.objects.filter(user_type="INTERN")
    return render(request,"create_task.html",context={'interns':interns})

@login_required(login_url='login')
def create_task(request):
    manager = Account.objects.get(username=request.user.username)
    intern_id = Account.objects.filter(username=request.POST.get("intern"))[0]
    deadline = request.POST.get("deadline")
    task_name = request.POST.get("taskname")
    description = request.POST.get("desc")
    print(request.user.user_type,intern_id,deadline)
    if intern_id and deadline and task_name:
        Task.objects.create(manager_id=manager,intern_id=intern_id,deadline=deadline,task_name=task_name,description=description)
        messages.success(request, "Task Created Successfully")
        return redirect("create_task")
    else:
        print("Please enter info")
    return render(request, "create_task.html")

@login_required(login_url='login')
def show_blockers(request):
    data = Blocker.objects.all()
    print(data)
    return render(request,"manager_blockers.html",{"data":data})

def sendqueries(request):
    if request.user.user_type=="MANAGER":
        data = Blocker.objects.filter(manager_id=request.user.user_id)
        return render(request,"resolve_queries.html",context={'data':data})

@login_required(login_url='login')
def solvequeries(request):
    if request.method=="POST" and request.user.user_type=="MANAGER":
        ques = Blocker.objects.filter(blocker_id=request.POST.get("question"))[0]
        answer = request.POST.get("answer")
        check = Blocker_Answer.objects.filter(blocker=ques)
        print(check)
        if check:
            check[0].answer = answer
            check[0].save()
        elif ques and answer:
            Blocker_Answer.objects.create(blocker=ques,answer=answer)
            messages.success(request, "Answer submitted Successfully")
            return redirect("intern-home")
        else:
            print("Please enter info")
    return render(request,"resolve_queries.html")

