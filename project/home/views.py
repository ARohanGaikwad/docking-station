from django.shortcuts import redirect, render
from django.http import FileResponse, HttpResponse
from .models import UploadedFile
from django.conf import settings
# Create your views here.
from django.core.files.storage import FileSystemStorage
import os

MEDIA_PATH = 'media/'  # folder to store files

def home(request):
    files = os.listdir(settings.MEDIA_ROOT)  # List all files in media folder
    return render(request, 'home/index.html', {'files': files})

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        fs = FileSystemStorage(location=MEDIA_PATH)
        fs.save(file.name, file)
    return redirect('home')

def download_file(request, filename):
    filepath = os.path.join(MEDIA_PATH, filename)
    return FileResponse(open(filepath, 'rb'), as_attachment=True)

def delete_file(request, filename):
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    return redirect('home')