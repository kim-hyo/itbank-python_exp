from django.shortcuts import render
from phonebook.models import phonebooks

# Create your views here.
def test(request):
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