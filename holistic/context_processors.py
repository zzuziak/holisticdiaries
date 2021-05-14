from .models import Category

def add_variable_to_context(request):
    return {
        'cat_menu': Category.objects.all()
    }
