from .models import Category

# if you want something to appear on every page ypu use content procrssor
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)