from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.models import Task, Account, Progress, Status, Blocker, Blocker_Answer
from django.contrib import messages

# Create your views here.
@login_required(login_url = "login")
def intern_home(request):
    data = Progress.objects.filter(intern_id=request.user.user_id)
    # status = Progress.objects.filter(intern_id=request.user.user_id)
    return render(request,"intern_home.html",context={"data":data})

def progress_info(request):
    if request.user.user_type=="INTERN":
        tasks = Task.objects.filter(intern_id=request.user.user_id)
        li = []
        for i in Status.choices:
            li.append(i[0])
        return render(request,"progress.html",context={"tasks":tasks,"status":li})
    else:
        print("User not eligible")
    return render(request,"progress.html")

@login_required(login_url = "login")
def update_progress(request):
    if request.method=="POST" and request.user.user_type=="INTERN":
        task = Task.objects.get(task_id=request.POST.get("task"))
        intern_id = Account.objects.get(username=request.user.username)
        status = request.POST.get("value")
        data = Progress.objects.filter(progress_task_id_id=task.task_id)
        if data and intern_id and status:
            data[0].status = status
            data[0].save()
            # Progress.objects.create(progress_task_id=task, intern_id=intern_id,status=status)
            messages.success(request, "Progress Updated Successfully")
            return redirect("intern-home")
        else:
            Progress.objects.create(progress_task_id=task, intern_id=intern_id, status=status)
            print("Please enter info")
    return render(request,"progress.html")


def send_managers_info(request):
    if request.user.user_type=="INTERN":
        tasks = Task.objects.filter(intern_id=request.user.user_id)
        managers = Account.objects.filter(user_type="MANAGER")
        return render(request,"add_blocker.html",context={'managers':managers,"tasks":tasks})
    else:
        return render(request,"add_blocker.html")


@login_required(login_url='login')
def addblocker(request):
    manager = Account.objects.filter(username=request.POST.get("manager"))[0]
    intern_id = Account.objects.get(username=request.user.username)
    task = Task.objects.filter(task_id=request.POST.get("task"))[0]
    label = request.POST.get("label")
    query = request.POST.get("query")
    print(manager,id,task,label,query)
    if request.user and manager and task:
        Blocker.objects.create(manager_id=manager,intern_id=intern_id,blocker_task_id=task,label=label,query=query)
        messages.success(request, "Blocker Added Successfully")
        return redirect("intern-home")
    else:
        print("Please enter info")
    return render(request, "add_blocker.html")

@login_required(login_url='login')
def trackblockers(request):
    data = Blocker_Answer.objects.all()
    print(data)
    return render(request,"blockers.html",{"data":data})

