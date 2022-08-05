from django.shortcuts import redirect, render
from .models import Project
from .forms import ProjectForm

# Create your views here.

def projects(request):
    projects= Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request,'projects/projects.html',context)

def single_project(request,pk):
    return render(request,'projects/single_projects.html')


def createProject(request):
    form = ProjectForm()
    if request.method == "POST":
    #  print(request.POST) 
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, 'projects/projects_form.html',context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, 'projects/projects_form.html',context)

def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request,'projects/delete_object.html',context)