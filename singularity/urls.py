"""singularity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from singularity.views import home, nosotros,proyectos, contacto, singularity,singularity_import, import_acount, cart, coming_soon, checkout, product_detail, shop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name=" "),
    path('home/',home, name="home"),
    path('nosotros/',nosotros, name="nosotros"),
    path('proyectos/',proyectos, name="proyectos"),
    path('contacto/',contacto, name="contacto"),
    path('singularity/',singularity, name="singularity"),
    path('singularity_import/',singularity_import, name="singularity_import"),
    path('import_acount/',import_acount, name="import_acount"),
    path('cart/',cart, name="cart"),
    path('coming_soon/',coming_soon, name="coming_soon"),
    path('checkout/',checkout, name="checkout"),
    path('product_detail/',product_detail, name="product_detail"),
    path('shop/',shop, name="shop"),

    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
