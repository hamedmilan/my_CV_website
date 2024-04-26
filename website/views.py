from django.shortcuts import render

def index_view(request):
    context = {'phone':'(+358) 046 683 5578','email':'hamed.milanchian@gmail.com','city_country':'Tampere/Finland'}
    return render(request, 'website/index.html', context)


def languages_view(request):
    return render(request, 'website/languages.html')


def education_view(request):
    context = {'BSc':'Mechanical Engineering','MSc':'Mechanical Engineering','PhD':'Electrical Engineering'}
    return render(request, 'website/education.html',context)

def skills_view(request):
    context = {'skill_1':'Mathematical Modeling','skill_2':'FEM','skill_3':'Mechanical Analysis',
               'skill_4':'Programming','skill_5':'Numerical Modeling','skill_6':'High Temperature Superconductors'}
    return render(request, 'website/skills.html', context)

def projects_view(request):
    return render(request, 'website/projects.html')


def contact_view(request):
    context = {'address':'Orivedenkatu 5 E 265'}
    return render(request, 'website/contact.html', context)
