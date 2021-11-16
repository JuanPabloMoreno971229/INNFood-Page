
from django.contrib import admin
from django.urls import path
from core import views as core_views
from portfolio import views as portfolio_views
from contact import views as contact_views
from blog import views as blog_views
from django.conf import settings

urlpatterns = [
    path('', core_views.home, name="home"),
    path('about-us/', core_views.aboutus, name="about"),
    path('products/', portfolio_views.portfolio, name="products"),
    path('blog/', blog_views.blog, name="blog"),
    path('blog/<int:id>', blog_views.blog_detail, name="blog_detail"),
    path('contact/', contact_views.contact, name="contacto"),
    path('admin/', admin.site.urls),
]

admin.site.site_header = "Administrador de INNFood"
admin.site.site_title = "INNFood portal Administrador"
admin.site.index_title = "Bienvenido al gestor de contenido de INNFood  "

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
