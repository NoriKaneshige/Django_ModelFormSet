from django.shortcuts import render, redirect
from .forms import PostCreateFormSet
from .models import Post


def add(request):
    formset = PostCreateFormSet(request.POST or None)
    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return redirect('app:index')

    # setting an initial state
    initial = [
        {'title': 'watched movie', 'text': 'it was fun'},
        {'title': 'ate sushi', 'text': 'it was tasty'},
        {'title': 'had a walk', 'text': 'it was refreshing'},
    ]
    formset = PostCreateFormSet(request.POST or None, initial=initial)

    # if you want to show only new form
    # formset = PostCreateFormSet(request.POST or None, queryset=Post.objects.none())
    
    context = {
        'formset': formset
    }

    return render(request, 'app/post_formset.html', context)
