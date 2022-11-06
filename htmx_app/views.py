from django.shortcuts import render , redirect
from .models import Empresas
from django.views.generic import CreateView, ListView
# Create your views here.




class tabela(ListView):
    template_name = 'htmx.html'
    model = Empresas


def cadastro(request):
    if request.method == 'POST':
        print('ok')
        projeto = request.POST['projeto']
        empresa = request.POST['empresa']
        cnpj = request.POST['cnpj']
        print(projeto, empresa, cnpj)

        obj = Empresas.objects.create(empresa=empresa,cnpj=cnpj)
        obj.save()

        print('Empresa salva')
    return redirect('tabela')
