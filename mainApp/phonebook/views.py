from django.shortcuts import render, redirect
from phonebook.models import phonebooks

# Create your views here.
def test(request):
    # print(f"GET userID:{request.GET.get('userID')}")
    # print(f"GET userPW:{request.GET.get('userPW')}")
    print(f"POST userID:{request.POST.get('userID')}")
    print(f"POST userPW:{request.POST.get('userPW')}")
    return render(request, 'my_html/test.html')

def pbook(request):
    all_users = phonebooks.objects.values('id', 'name', 'pnum')
    #print(type(all_users))
    context = {'pbook': all_users}

    return render(request, 'my_html/pbook.html', context)    

def testint(request, ids):
    print(f"my_id = {ids}")
    return render(request, 'my_html/pbook.html')    

def details(request, userid):
    user_info = phonebooks.objects.values('id', 'name', 'pnum', 'addr', 'birth').get(id=userid)   
    context = {'pbook': user_info}
    return render(request, 'my_html/details.html', context)

def add(request):
    if request.method == 'POST':
        # print("POST method")
        # print(f"Name: {request.POST.get('name')}")
        # print(f"Phone Number: {request.POST.get('pnum')}")
        # print(f"E-mail: {request.POST.get('email')}")
        # print(f"Address: {request.POST.get('addr')}")
        # print(f"Birthday: {request.POST.get('bir')}")

        table = phonebooks()
        table.name = request.POST.get('name')
        table.pnum = request.POST.get('pnum')
        table.email = request.POST.get('email')
        table.addr = request.POST.get('addr')
        table.birth = request.POST.get('bir')
        table.save()
        return redirect('PB:pb')
    else:
        print(f"GET method: {request.method}")
        return render(request, 'my_html/add.html')