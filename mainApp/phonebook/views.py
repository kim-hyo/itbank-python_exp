from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'my_html/test.html')

def pbook(request):
    return render(request, 'my_html/pbook.html')    

def testint(request, ids):
    print(f"my_id = {ids}")
    return render(request, 'my_html/pbook.html')    