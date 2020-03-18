from django.shortcuts import render

# Create your views here.
def dworld(request):

    books = [
        {'id': 0,
        'title': 'A Fire Upon the Deep',
        'author': 'Vernor Vinge',
        'first_sentence': 'The coldsleep itself was dreamless.',
        'video_url': 'videos1.mp4',
        'year_published': '1992'},
        {'id': 1,
        'title': 'The Ones Who Walk Away From Omelas',
        'author': 'Ursula K. Le Guin',
        'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
                'video_url': 'videos2.mp4',
        'published': '1973'},
        {'id': 2,
        'title': 'Dhalgren',
        'author': 'Samuel R. Delany',
        'first_sentence': 'to wound the autumnal city.',
         'video_url': 'videos3.mp4',
        'published': '1975'},
         {'id': 4,
        'title': 'Dhalgren 2131',
        'author': 'Samuel R. Delany',
        'first_sentence': 'to wound the autumnal city.',
         'video_url': 'videos4.mp4',
        'published': '1975'},
        {'id': 5,
        'title': 'A Fire Upon the Deep',
        'author': 'Vernor Vinge',
        'first_sentence': 'The coldsleep itself was dreamless.',
        'video_url': 'videos5.mp4',
        'year_published': '1992'},
        {'id': 6,
        'title': 'The Ones Who Walk Away From Omelas',
        'author': 'Ursula K. Le Guin',
        'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
                'video_url': 'videos2.mp4',
        'published': '1973'},
        {'id': 7,
        'title': 'Dhalgren',
        'author': 'Samuel R. Delany',
        'first_sentence': 'to wound the autumnal city.',
         'video_url': 'videos3.mp4',
        'published': '1975'},
         {'id': 8,
        'title': 'Dhalgren 2131',
        'author': 'Samuel R. Delany',
        'first_sentence': 'to wound the autumnal city.',
         'video_url': 'videos3.mp4',
        'published': '1975'}
    ]
    context = {
            'projects': books
    }
    return render(request, 'hello_world.html', context)