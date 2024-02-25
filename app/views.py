from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import File
from .forms import LoginForm
from app.common.utils import upload_user_data
from django.contrib.auth.models import User


# Create your views here.
def login_page(request):
    # show login page to the user
    context = {}
    return render(request, 'upload_page.html')


# def login_user(request):
#     # check user credentials and send to the next page
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         # check whether it's valid:
#         print('form>', form)
#         if form.is_valid():
#             user_name = form.cleaned_data["username"]
#             pass_word = form.cleaned_data["username"]
#             print('User entered details', user_name, pass_word)
#         return redirect('app:upload')
#     return redirect('app:login_page')


def query_result(request):
    pass


@login_required
def upload_page(request):
    # to send the upload page html
    # messages.success(request, 'You are on upload page')
    if request.method == 'POST':
        file = request.FILES['file'].read()
        fileName = request.POST['filename']
        existingPath = request.POST['existingPath']
        end = request.POST['end']
        nextSlice = request.POST['nextSlice']
        if not fileName.endswith('.csv'):
            res = JsonResponse({'data': 'Please select csv file only.'})
            return res

        if file == "" or fileName == "" or existingPath == "" or end == "" or nextSlice == "":
            res = JsonResponse({'data': 'Invalid Request'})
            return res
        else:
            if existingPath == 'null':
                path = 'media/' + fileName
                with open(path, 'wb+') as destination:
                    destination.write(file)
                FileFolder = File()
                FileFolder.existingPath = fileName
                FileFolder.eof = end
                FileFolder.name = fileName
                FileFolder.save()
                if int(end):
                    try:
                        upload_user_data(path)
                        res = JsonResponse({'data': 'Uploaded Successfully', 'existingPath': fileName})
                    except KeyError:
                        res = JsonResponse({'data': 'Please check key and data in file.'})

                else:
                    res = JsonResponse({'existingPath': fileName})

                # here at end will upload data in database

                return res

            else:
                path = 'media/' + existingPath
                model_id = File.objects.get(existingPath=existingPath)
                if model_id.name == fileName:
                    if not model_id.eof:
                        with open(path, 'ab+') as destination:
                            destination.write(file)
                        if int(end):
                            model_id.eof = int(end)
                            model_id.save()
                            try:
                                upload_user_data(path)
                                res = JsonResponse({'data': 'Uploaded Successfully',
                                                    'existingPath': model_id.existingPath})
                            except KeyError:
                                res = JsonResponse({'data': 'Please check key and data in file and upload file again..'})
                        else:
                            res = JsonResponse({'existingPath': model_id.existingPath})
                        return res
                    else:
                        res = JsonResponse({'data': 'EOF found. Invalid request'})
                        return res
                else:
                    res = JsonResponse({'data': 'No such file exists in the existingPath'})
                    return res
    return render(request, 'upload_page.html')


@login_required
def query_page(request):
    # here will ask for query result
    # messages.success(request, 'You are on query page')
    return render(request, 'query_page.html')


@login_required
def user_page(request):
    # to show the user page to add new user
    # messages.success(request, 'You are on user page')
    users = User.objects.all()
    context = {
        'object': users
    }
    return render(request, 'user_page.html', context)

