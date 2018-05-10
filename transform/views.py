from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FileForm
import tempfile
def get_file(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form=FileForm(request.POST,request.FILES)
        if form.is_valid():
             with tempfile.NamedTemporaryFile(dir='/tmp/', delete=False) as f:
                f.write(form['your_file'].value())#.encode("utf-8"))
                f.close
                filename = f.filename
                #output=pythonscript(filename)
                output='it read the file :)'
                f.close()
                context={'form': form,'output':output}
                return render(request, 'index.html', context)

        else:
            
            output="form was invalid"
            context={'form': form,'output':output}
            return render(request, 'index.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FileForm()
        output=''
        context={'form': form,'output':output}
        return render(request, 'index.html', context)

    
def get_post(request,form):
    return render(request, 'post.html',{'output':output})

