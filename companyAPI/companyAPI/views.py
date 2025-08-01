from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("Home Page requested")
    friends = [
        'Rijjit',
        'Dead guy',
        'Langra',
        'Chotu'
    ]
    #return HttpResponse("<h1>This is home page</h1>")
    
    return JsonResponse(friends, safe=False)