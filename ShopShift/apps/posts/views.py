from django.shortcuts import render, redirect
from .forms import ProductCreationForm
from .models import Product


# Create your views here.
def main(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})


def create_product(request):
    if request.method == 'POST':
        form = ProductCreationForm(request.POST)
        if form.is_valid():
            # Сохранение продукта в базе данных
            product = form.save(commit=False)
            product.user = request.user  # Присвоение текущего пользователя как автора объявления
            product.save()
            return redirect('main')  # Перенаправление на страницу успешного создания объявления
    else:
        form = ProductCreationForm()

    return render(request, 'create_product.html', {'form': form})
