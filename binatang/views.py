from django.shortcuts import render, redirect
from .models import Binatang
from .forms import BinatangForm

# Create your views here.
def daftar_binatang(request):
    return (render(request, 'daftar_binatang.html', {}))

def list_binatang(request):
    list_binatang = Binatang.objects.all()
    print(list_binatang)
    return render(request, 'daftar_binatang.html', {'Binatang': list_binatang})

def input_binatang(request):
    if request.method == "POST":
        form = BinatangForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect('list_binatang')
    else:
        form = BinatangForm()
    return render(request, 'input_binatang.html', {'form': form})