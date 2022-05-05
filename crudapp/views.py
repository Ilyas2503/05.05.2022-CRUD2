from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import CommentForm
from .models import Comment
from .utils import check_bad_words

# Create your views here.

BAD_WORDS = ['bakyt', 'adilet', 'mat']


def retrieve(request):
    context = {}  # dict
    show_msg = Comment.objects.all()  # Show comments
    context['comments'] = show_msg
    return render(request, 'comment.html', context)


def retrieve_detail(request, username):
    context = {}  # dict
    show_msg = Comment.objects.get(author=username)  # Show comments
    context['comments'] = show_msg
    return render(request, 'comment_detail.html', context)


def create(request):
    context = {}
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() and check_bad_words(form.instance.message, BAD_WORDS):
            form.save()
            return HttpResponse('SUCCESS')
        else:
            return HttpResponse('Bad word is detected', form.instance.message)
    form = CommentForm()
    context['form'] = form
    return render(request, 'create.html', context)


def update(request, pk):
    context = {}
    obj = get_object_or_404(Comment, pk=pk)
    form = CommentForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponse('SUCCESS')
    context['form'] = form
    return render(request, 'create.html', context)


def delete(request, pk):
    context = {}
    obj = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return HttpResponse('Succesfuly deleted')
    context['comments'] = obj
    return render(request, 'delete.html', context)
