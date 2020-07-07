from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .models import usuario



def delete_addres(request, id):
    end = usuario.objects.get(id=id)
    end.delete()  
    return redirect('/')


def cadastrar_end(request):
    end_id = request.GET.get('id')
    if end_id:
        end = usuario.objects.get(id=end_id)
        
        return render(request, 'cadastrar.html', {'end':end})
        
    return render(request, 'cadastrar.html')

def tabela_ends(request):
    end = usuario.objects.all()
    #print(end.query)
    return render(request, 'tabela.html', {'end':end})
    

@csrf_protect
def submit_cadastrar(request):
    if request.POST:
        inputAddress = request.POST.get('rua')
        inputDistric = request.POST.get('bairro')
        inputNumber = request.POST.get('numero')
        inputCity = request.POST.get('cidade')
        inputUf = request.POST.get('uf')
        inputCEP = request.POST.get('cep')
        inputComplemento=request.POST.get('complemento')
        inputDescricao = request.POST.get('descrição')
        inputId = request.POST.get('id')
        if inputId :
            end = usuario.objects.get(id=inputId)
            if( inputAddress or inputDistric or inputNumber or inputCity or inputUf or inputCEP != ''):
                end.address = inputAddress
                end.district = inputDistric
                end.number = inputNumber
                end.city = inputCity
                end.uf = inputUf 
                end.zipcode = inputCEP 
                end.description = inputDescricao
                end.complement = inputComplemento
                end.save()
            else:
                messages.error(request, ' Campos não prenchidos.')
                return redirect('/cadastrar/')
        else :
            if( inputAddress or inputDistric or inputNumber or inputCity or inputUf or inputCEP != ''):
                ends = usuario.objects.create(address = inputAddress, district = inputDistric, 
                                                number = inputNumber, city = inputCity,
                                                uf = inputUf , zipcode = inputCEP, description = inputDescricao, 
                                                complement = inputComplemento )
            else:
                messages.error(request, ' Campos não prenchidos.')
                return redirect('/cadastrar/')
    return redirect('/tabela/')

       
