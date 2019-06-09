from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from llinked.models import Course
from django.http import HttpResponse, JsonResponse, Http404

def index(request):
    return render(request,'llinked/home.html')

def about(request):
    return render(request,'llinked/about.html')

def search(request):
 if request.method == 'GET':
    search_query = request.GET.get('search', None)
    if search_query is not None:
        query = User.objects.filter(username=search_query).first()
        if not query:
             raise Http404('This user does not exist')
        else:
                if query.DoesNotExist:
                        context = {
                                'first_name': query.first_name,
                                'last_name': query.last_name,
                                'username' : query.username,
                                'bio': query.profile.bio,
                                'usertype' : query.profile.usertype,
                                'image': query.profile.image.url,
                        }
                else:
                      context = {
                                'first_name': query.first_name,
                                'last_name': query.last_name,
                                'username' : query.username,
                                'bio': query.profile.bio,
                                'usertype' : query.profile.usertype,
                                'image': query.profile.image.url,
                                'dept': query.instructor.dept,
                                # 'alumni' : query.alumni.grad_date
                      }   
#  return render(request, 'llinked/account.html', context)
        return JsonResponse(query)