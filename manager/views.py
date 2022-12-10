from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TaskForm
from django.contrib import messages
from core.models import Account, Task, Progress, Blocker_Answer, Blocker, Points_Assign
from collections import defaultdict

# Create your views here.
@login_required(login_url='login')
def manager_home(request):
    data = Points_Assign.objects.all()
    li = defaultdict(list)
    dic = {}
    for temp in data:
        dic[temp.intern_id] = temp.points_assigned
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
    li = []

    for i in range(len(data)):
        li.append(data[i].blocker_id)
    blocker_ans_data = Blocker_Answer.objects.all()

    li_blocker_ans = []
    for i in range(len(blocker_ans_data)):
        li_blocker_ans.append(blocker_ans_data[i].blocker.blocker_id)
    set1 = set(li)
    set2 = set(li_blocker_ans)

    ids = list(set1-set2)
    data = (Blocker.objects.filter(blocker_id__in = (ids)))
    if data:
        return render(request,"manager_blockers.html",{"data":data})
    else:
        messages.warning(request,"No Blockers exists")
    return render(request,"manager_blockers.html")

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


def send_interns_info_points(request):
    if request.user.user_type=="MANAGER":
        interns = Account.objects.filter(user_type="INTERN")
        return render(request,"add_points.html",context={'interns':interns})
    else:
        return render(request,"add_points.html")

@login_required(login_url = "login")
def give_points(request):
    if request.method=="POST" and request.user.user_type=="MANAGER":
        manager_id = Account.objects.get(username=request.user.username)
        intern_id = Account.objects.filter(username=request.POST.get("intern"))[0]
        points_assigned = request.POST.get("points")
        print(intern_id,manager_id,points_assigned)
        data = Points_Assign.objects.filter(manager_id=manager_id,intern_id=intern_id)
        if data:
            messages.error(request, "Points already given")
            return redirect("send-interns-info")
        else:
            Points_Assign.objects.create(manager_id=manager_id, intern_id=intern_id,points_assigned=points_assigned)
            messages.success(request, "Points Assigned Successfully")
            return redirect("send-interns-info")
    return render(request,"add_points.html")

@login_required(login_url='login')
def show_progress(request):
    data = Progress.objects.all()
    length = len(data)
    return render(request,"show_progress_interns.html",{"data":data,"length":length})