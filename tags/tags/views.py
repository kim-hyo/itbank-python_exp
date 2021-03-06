from django.shortcuts import render

def test_html(request):
    context = {'ki': 'valve', 
                'ka': 'steam',
                'list1': ['list_value_0', 'list_value_1', 'list_value_2'],
                'dict1': {'a': 'dict_value_a', 'b': 'dict_value_b', 'c': 'dict_value_c'},
                'num_1': 300,
                'num_2': 200
    }
    return render(request, 'my_html/html_excercise.html', context)

def login(request):
    return render(request, 'my_html/info.html')

def tempcode(request):
    temp_dict = {
        'dict_key': [ [1, 2, 3, 4, 5], ['yuk', '7', 'pal', 'goo', '10'], [11, 12, 13, 14, 15] ]
    }
    return render(request, 'my_html/tempcode.html', temp_dict)

def worldcup(request):
    points = {
        'group': {
            'korea': [4, 1, 2, 9, 7],
            'iran': [5, 2, 0, 6, 0],
            'siria': [2, 2, 3, 2, 3]
        }
    }
    return render(request, 'my_html/worldcup.html', points)