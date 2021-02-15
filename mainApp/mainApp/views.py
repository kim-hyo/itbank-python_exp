from django.shortcuts import render

def test_html(request):
    return render(request, 'my_html/tests.html')