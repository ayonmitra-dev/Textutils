# I have created this - Ayon
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    variables = {'name': 'Ayon', 'place': 'Mars'}
    return render(request, 'index.html', variables)


def removepunc(request):

    # get data from index.html
    textdata = request.POST.get('text', 'default')
    remove_punc_val = request.POST.get('remove_punc_val', 'off')
    get_full_caps = request.POST.get('full_caps', 'off')
    get_char_count = request.POST.get('char_count', 'off')

    if remove_punc_val == "on" and get_full_caps == "on" and get_char_count == 'on':

        analyzed_text = ""
        punctuations = ''' ~!#$%^&*()_-"':;., '''
        for char in textdata:
            if char not in punctuations:
                analyzed_text = analyzed_text + char.upper()

        char_count_val = len(analyzed_text)

        # send the data
        params = {'purpose': 'Remove punctuations, full caps and char count',
                  'analyzed': analyzed_text, 'char_count_val': char_count_val}
        return render(request, 'about.html', params)

    elif remove_punc_val == "on" and get_full_caps == "on":
        analyzed_text = ""
        punctuations = ''' ~!#$%^&*()_-"':;., '''
        for char in textdata:
            if char not in punctuations:
                analyzed_text = analyzed_text + char.upper()

        # send the data
        params = {'purpose': 'Remove punctuations and full caps',
                  'analyzed': analyzed_text}
        return render(request, 'about.html', params)

    elif remove_punc_val == 'on' and get_char_count == 'on':
        analyzed_text = ""
        punctuations = ''' ~!#$%^&*()_-"':;., '''
        for char in textdata:
            if char not in punctuations:
                analyzed_text = analyzed_text + char

        char_count_val = len(analyzed_text)

        # send the data
        params = {'purpose': 'Remove punctuations and char count',
                  'analyzed': analyzed_text, 'char_count_val': char_count_val}
        return render(request, 'about.html', params)

    elif get_full_caps == 'on' and get_char_count == 'on':
        analyzed_text = ""

        for char in textdata:
            analyzed_text = analyzed_text + char.upper()

        char_count_val = len(analyzed_text)

        # send the data
        params = {'purpose': 'full caps and char count',
                  'analyzed': analyzed_text, 'char_count_val': char_count_val}
        return render(request, 'about.html', params)

    elif (get_full_caps != 'off'):
        analyzed_text = ""

        for char in textdata:
            analyzed_text = analyzed_text + char.upper()

        params = {'purpose': 'Full caps', 'analyzed': analyzed_text}

        return render(request, 'about.html', params)

    elif remove_punc_val != 'off':
        analyzed_text = ""
        punctuations = ''' ~!#$%^&*()_-"':;., '''
        for char in textdata:
            if char not in punctuations:
                analyzed_text = analyzed_text + char

        params = {'purpose': 'Remove punctuations', 'analyzed': analyzed_text}
        return render(request, 'about.html', params)

    elif get_char_count == 'on':
        analyzed_text = len(textdata)

        params = {'purpose': 'text length', 'char_count_val': analyzed_text}
        return render(request, 'about.html', params)

    else:
        return HttpResponse("You must select atleast one value")
