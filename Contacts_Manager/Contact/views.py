from django.shortcuts import render, redirect
from Contact.models import Contacts
from django.http import HttpResponse

# Create your views here.
def show(request):
    if request.method == 'GET':
        leng = len(Contacts.objects.values())
        info = list(Contacts.objects.values())
        ctx = {'info': info, 'leng' : leng}
        return render(request, 'Notes_home.html', ctx)
    if request.method == 'POST':
        cinfo = Contacts()
        cinfo.name = request.POST.get('cname')
        cinfo.Mobnum = request.POST.get('cnum')
        cinfo.Company = request.POST.get('compname')
        cinfo.save()
        info = list(Contacts.objects.values())
        leng = len(Contacts.objects.values())
        ctx = {'info': info, 'leng' : leng}
        return render(request, 'Notes_home.html', ctx)

def add(request):
    return render(request, 'Notes_add.html')

def edit(request, cid):
    cinfo = Contacts.objects.filter(pk=cid)
    cinfo.delete()
    info = list(Contacts.objects.values())
    leng = len(Contacts.objects.values())
    ctx = {'info': info, 'leng' : leng}
    return render(request, 'Notes_home.html', ctx)

def modify(request, cid):
    info = Contacts.objects.filter(pk = cid).values()
    ctx = {
        'name' : info[0]['name'],
        'Mobnum' : info[0]['Mobnum'],
        'Company' : info[0]['Company'],
        'id' : cid,
    }
    return render(request, 'Edit_Contact.html', ctx)

def alter(request, cid):
    if request.method == 'POST':
        info = Contacts.objects.filter(pk = cid)
        info.update(name=request.POST['cname'])
        info.update(Mobnum=request.POST['cnum'])
        info.update(Company=request.POST['compname'])
        info = Contacts.objects.values()
        leng = len(info)
        ctx = {'info': info, 'leng' : leng, 'id' : cid}
        return render(request, 'Notes_home.html', ctx)
