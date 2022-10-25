from .models import Ad, Response


def navigate_context(request):
    category_type = Ad.TYPE
    current_user = request.user
    isaut = True if current_user.is_authenticated else False
    test = 'Оставь здесь свой отклик'
    responses = Response.objects.all()

    context = {
        'responses': responses,
        'vartest': test,
        'category_type': category_type,
        'current_user': current_user,
        'isaut': isaut,
    }

    return context


def get_user(request):
    return request.user
