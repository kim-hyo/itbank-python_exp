from django.shortcuts import render

def blog_con(request, year, month):    
    print("\n\n")
    print(f"blog {year}year/{month}month is connected")
    print("\n\n")

def blogname(request):    
    return render(request, 'my_html/test.html')

def info(request):    
    return render(request, 'my_html/info.html')

def blognames(request):    
    return render(request, 'my_html/blogname.html')

def board(request):    
    return render(request, 'my_html/board.html')

def test_html(request):
    return render(request, 'my_html/html_excercise.html')