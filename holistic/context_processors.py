from .models import Category, Notification

def add_variable_to_context(request):
    return {
        'cat_menu': Category.objects.all(),
        'notifications': Notification.objects.filter(read=False)
    }
