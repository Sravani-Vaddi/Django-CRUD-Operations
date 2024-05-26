


from django.shortcuts import render, redirect, get_object_or_404
from .forms import MyForm
from .models import Mymodel

def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Retrieve all objects from the database
            data = Mymodel.objects.all()
            # Pass the retrieved data to the template context
            return render(request, 'testapp/success.html', {'data': data})
    else:
        form = MyForm()
    # Retrieve all objects from the database
    data = Mymodel.objects.all()
    return render(request, 'testapp/basic.html', {'form': form, 'data': data})
  
def update_view(request, pk):
    instance = get_object_or_404(Mymodel, pk=pk)
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            data = Mymodel.objects.all()
            return render(request, 'testapp/success.html', {'data': data})
    else:
        form = MyForm(instance=instance)
    return render(request, 'testapp/basic.html', {'form': form})


def delete_view(request, pk):
    instance = get_object_or_404(Mymodel, pk=pk)
    if request.method == 'POST':
        instance.delete()
        data = Mymodel.objects.all()
        return render(request, 'testapp/success.html', {'data': data})
    return render(request, 'testapp/delete.html', {'instance': instance})








# from django.shortcuts import render, redirect, get_object_or_404
# from .forms import MyForm
# from .models import Mymodel

# def my_form_view(request):
#     if request.method == 'POST':
#         form = MyForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Retrieve all objects from the database
#             data = Mymodel.objects.all()
#             # Pass the retrieved data to the template context
#             return render(request, 'testapp/success.html', {'data': data})
#     else:
#         form = MyForm()
#     # Retrieve all objects from the database
#     data = Mymodel.objects.all()
#     return render(request, 'testapp/basic.html', {'form': form, 'data': data})
  
# def update_view(request, pk):
#     instance = get_object_or_404(Mymodel, pk=pk)
#     form = MyForm(request.POST or None, instance=instance)
#     if form.is_valid():
#         form.save()
#         data = Mymodel.objects.all()
#         return render(request, 'testapp/success.html', {'data': data})
#     return render(request, 'testapp/basic.html', {'form': form})

# def delete_view(request, pk):
#     instance = get_object_or_404(Mymodel, pk=pk)
#     if request.method == 'POST':
#         instance.delete()
#         data = Mymodel.objects.all()
#         return render(request, 'testapp/success.html', {'data': data})
#     return render(request, 'testapp/delete.html', {'instance': instance})



