from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    user_data = request.GET['textdata']
    # print(f"userdaya: {user_data}")
    words = user_data.split()
    total = len(words)

    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    max_words = sorted(word_frequency.items(),
                       key=lambda item: item[1], reverse=True)

    return render(request, 'count.html', {'total': total, 'user_data': user_data, 'word_frequency': word_frequency, 'max_words': max_words})
