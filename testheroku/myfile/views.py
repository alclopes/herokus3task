from __future__ import absolute_import, unicode_literals
import os
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import MyFile
from django.conf import settings

def myfile(request):

    myfiles = MyFile.objects.first()

    # Apaga registro BD de imagens que não existem
    if myfiles:
        if settings.USE_S3:
            path = os.path.join(settings.MEDIA_URL, str(myfiles.file))
            # Aqui devemos questionar para apagar pois pode apenas não ter conexão no momento.
        else:
            path = os.path.join(settings.MEDIA_ROOT, str(myfiles.file))
            ok = os.path.isfile(path)
            if not ok:
                MyFile.objects.all().delete()
                myfiles = {}

    if request.method == 'POST':
        # recuperando os dados do arquivo
        description_param = request.POST.get('description_file')
        file_up = request.FILES['file_up']
        # salvando na base
        myfile = MyFile()
        myfile.description = description_param
        myfile.file = file_up
        myfile.save()
        return redirect(reverse('myfile:index'))
    else:
        if myfiles:
            file_url = os.path.join(settings.MEDIA_ROOT, myfiles.file.url)
            file_url = myfiles.file.url
            return render(request, 'myfile/index.html', {'file_url': file_url})
        else:
            return render(request, 'myfile/index.html')


# view to delete all register and files
def exclude_files(request):
    context = {}
    MyFile.objects.all().delete()
    myimages = {}
    context['myimages'] = myimages
    return render(request, 'myfile/index.html', context)

