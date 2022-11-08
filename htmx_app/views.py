from .models import Empresas, Regioes
from django.views.generic import CreateView, ListView
from .forms import EmpresasForm, RegiaoForm
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

# Create your views here.




def empresa(request):
    template_name = 'htmx.html'
    form = EmpresasForm(request.POST or None)

    empresas = Empresas.objects.all()

    context = {'object_list': empresas, 'form': form}
    return render(request, template_name, context)




@require_http_methods(['POST'])
def empresa_create(request):
    form = EmpresasForm(request.POST or None)

    if form.is_valid():
        expense = form.save()

    context = {'object': expense}
    return render(request, 'htmx.html', context)


from django.shortcuts import render
from .models import Contact
from django.views.generic.list import ListView

def create_contact(request):
    name = request.POST.get('contactname') # get data from form where name="contactname"
    phone_number = request.POST.get('phone_number') # get data from form where name="phone_number"
    
    # add contact
    contact = Contact.objects.create(name=name, phone_number=phone_number) # add contact to databse
    contacts = Contact.objects.all()
    return render(request, 'contact-list.html', {'contacts': contacts}) # display the list of contacts in contact-list.html

class ContactList(ListView):
    template_name = 'contact.html' # html file to display the list of contacts
    model = Contact
    context_object_name = 'contacts' # used in the HTML template to loop through and list contacts

def create_regiao(request):
    regiao = request.POST.get('regiao')

    reg = Regioes.objects.create(regiao=regiao)
    regioes = Regioes.objects.all()
    return render(request, 'regioes-list.html', {'regioes': regioes})

class RegioesList(ListView):
    template_name = 'regiao.html'
    model = Regioes
    context_object_name = 'regioes'