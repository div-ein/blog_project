from django.shortcuts import render,get_object_or_404,redirect
from .models import Tisto
from django.utils import timezone
from .forms import CreateWrittingForm
# Create your views here.

def home(request):
  tistos = Tisto.objects
  return render(request, 'home.html', {'tistos':tistos})

def detail(request, tisto_id):
  tisto_detail = get_object_or_404(Tisto, pk=tisto_id)
  return render(request, 'detail.html', {'tisto_detail':tisto_detail})

def create(request):
  if request.method == "POST":
    form = CreateWrittingForm(request.POST)
    if form.is_valid():
      tisto = form.save(commit=False)
      tisto.sigan = timezone.datetime.now()
      tisto.save()
    return redirect('/detail/'+str(tisto.id))
  else :
    form = CreateWrittingForm()
  return render(request,'create.html',{'form':form})

def update(request, tisto_id):
  tisto = Tisto.objects.get(id=tisto_id)
  if request.method=="POST":
    form = CreateWrittingForm(request.POST, instance=tisto)
    if form.is_valid():
      tisto = form.save()
      return redirect('/detail/'+str(tisto.id))
  else:
    form = CreateWrittingForm(instance=tisto)
    return render(request, 'create.html', {'form':form})

def delete(request, tisto_id):
  tisto = Tisto.objects.get(id=tisto_id)
  tisto.delete()
  return redirect('home')