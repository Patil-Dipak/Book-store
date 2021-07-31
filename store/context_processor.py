from .models import Category

# For return the all categories
def categories(request):
    return {
            'categories' : Category.objects.all()
           }