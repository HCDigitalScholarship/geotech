from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FileForm
import tempfile
def get_file(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form=FileForm(request.POST,request.FILES)
        if form.is_valid():
             with tempfile.NamedTemporaryFile(suffix='.txt', dir='/tmp/transform.csv', delete=False) as f:
                f.write(form['your_file'].value().read())#.encode("utf-8"))
                f.close
                filename = '/tmp/transform.txt'
                #output=pythonscript(filename)
                output='it read the file :)'
                f.close()
                form=FileForm(request.POST['your_file'])
                context={'form': form,'output':output}
                return render(request, 'index.html', context)

        else:
            
            output="form was invalid"
            context={'form': form,'output':output}
            return render(request, 'index.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        errors=0
        form = FileForm()
        output=''
        context={'form': form,'output':output}
        return render(request, 'index.html', context)

    
def get_post(request,form):
    return render(request, 'post.html',{'output':output})

