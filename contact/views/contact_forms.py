from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q
from django.shortcuts import get_object_or_404 , render, redirect


from contact.models import Contact

# Create your views here.
def create(request):
    if request.method == 'POST':
        print()
        print(request.method)
        print(request.POST.get('first_name'))
        print(request.POST.get('last_name'))
        print()

    context = {

    }

    print()
    print(request.method)
    print()

    return render(
        request,
        'contact/create.html',
        context
    )