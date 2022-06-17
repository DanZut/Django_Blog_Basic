from django.shortcuts import render


def post_list(request):
    return render(request, 'BasicBlog/post_list.html', {})


