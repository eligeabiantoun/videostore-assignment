
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Video
from .forms import VideoForm

def video_list(request):
    q = request.GET.get('q','')
    qs = Video.objects.all()
    if q:
        qs = qs.filter(MovieTitle__icontains=q)
    return render(request, 'videos/video_list.html', {'videos': qs, 'q': q})

def video_detail(request, pk):
    v = get_object_or_404(Video, pk=pk)
    return render(request, 'videos/video_detail.html', {'video': v})

def video_create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'videos/video_form.html', {'form': form, 'is_create': True})

def video_update(request, pk):
    v = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=v)
        if form.is_valid():
            form.save()
            return redirect('video_detail', pk=v.pk)
    else:
        form = VideoForm(instance=v)
    return render(request, 'videos/video_form.html', {'form': form, 'is_create': False, 'video': v})

def video_delete(request, pk):
    v = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        v.delete()
        return redirect('video_list')
    return render(request, 'videos/video_confirm_delete.html', {'video': v})
