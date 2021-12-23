from django.shortcuts import render, redirect
from lab3_web.models import Articles
from.forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import RegisterForm

def main (request):
    return render(request, 'flower/flowermarket.html',{})

def second (request):
    header = "Team members"
    user1 = {"name": "Aliya", "surname": "Beishenaly" }
    user2 = {"name": "Maral", "surname": "Zhakypova"}
    data = {"header": header, "user1": user1, "user2": user2}
    return render(request, 'flower/2nd.html',context=data)

def third (request):
    header = "Developers’ contacts:"
    address = "Street Manasa 34A, Almaty"
    user1 = {"name": "Aliya", "surname": "Beishenaly", "phone": "+7 701 013 04 02", "mail":"aliya.beishenaly@mail.ru", "hours":"9:00-18:00"}
    user2 = {"name": "Maral", "surname": "Zhakypova", "phone": "+7 707 993 35 65", "mail":"msjakyp@mail.ru", "hours":"9:00-18:00"}
    data = {"header": header, "adress":address, "user1": user1, "user2": user2}
    return render(request, 'flower/3rd.html',context=data)

def fourth (request):
    listOfFlowers = (
        {'img':'/static/images/buket22.jpg', 'text':'Букет из белых роз и пион «Любимая» 14000₸'},
        {'img':'/static/images/buket23.jpg', 'text':'Букет из 25 розовых роз  25000₸'},
        {'img':'/static/images/buket45.jpg', 'text':'Букет «Аромат» 11500₸'}
    )
    listOfFlowers1 = (
        {'img': '/static/images/buket4.jpg', 'text': 'Букет в коробочке из хризонтем и роз «Мама»  21000₸'},
        {'img': '/static/images/buket11.jpg', 'text': 'Букет из разноцветных роз «Мистика»  7500₸'},
        {'img': '/static/images/buket12.jpg', 'text': 'Букет «Букет «Моя» 14300₸'}
    )
    listOfFlowers2 = (
        {'img': '/static/images/buket13.jpg', 'text': 'Букет из голландских, кустовых желтых роз и лилии «Желтые лучи» 12500₸'},
        {'img': '/static/images/buket14.jpg', 'text': 'Букет из роз и лилии «Нежность» 10500₸'},
        {'img': '/static/images/buket9.jpg', 'text': 'Букет из пионовидных роз «Милашка» 14000₸'}
    )
    return render(request, 'flower/flowermarket.html', context={'flowers':listOfFlowers, 'flowers1':listOfFlowers1, 'flowers2':listOfFlowers2})

def fifth (request):
    flower=Articles.objects.all()
    return render(request, 'flower/flowers.html', context={'flowers':flower})

def sixth (request):
    return render(request, 'flower/contactus.html',{})

def seven (request):
    return render(request, 'registration/login.html', {})

def eight (request):
    return render(request, 'flower/payment.html',{})

def nine (request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flowermarket')
    else:
        form = RegisterForm()

    return render(request, 'flower/registr.html', {"form": form})

def ten (request):
    return render(request, 'flower/cart.html',{})

class ArticlesDetailed(DetailView):
    model = Articles
    template_name = 'flower/detail_art.html'
    context_object_name = 'flower'

class ArticlesUpdate(UpdateView):
    def get_success_url(self):
        return '/flowers'
    model = Articles
    template_name = 'flower/create_art.html'
    form_class = ArticlesForm

class ProductsDelete(DeleteView):
    model = Articles
    success_url = '/flowers'
    template_name = 'flower/delete_art.html'


def create_prod(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('flowers')
        else:
            error = "something gone wrong..."
    form = ArticlesForm()

    data = {
        'form':form,
        'error':error
    }
    return render(request, 'flower/create_art.html', data)


def flowers(request):
    new = Articles.objects.all()
    return render(request, 'flower/flowers.html, new')

