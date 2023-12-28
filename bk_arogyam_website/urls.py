from django.contrib import admin
from django.urls import path, include
from first_app.views import index
from first_app.views import about
from first_app.views import events
from first_app.views import events_detail
from first_app.views import blogs
from first_app.views import blogs_details
from first_app.views import gallery
from first_app.views import career
from first_app.views import videos
from first_app.views import contactus
from first_app.views import download
from first_app.views import diseases
from first_app.views import allopath_ayurveda, ayurveda_allopath
# ==============================
from first_app.views import product


from django.urls import path
from django.conf import settings
# from django.views.static import serve
from django.conf.urls.static import static

# ----------------Doctor------------------
from first_app.views import doctor_login
from first_app.views import doctor_diseases
from first_app.views import doctor_profile

# ----------------Employee------------------
from first_app.views import employee_login
from first_app.views import employee_dashboard

#testing
from first_app.views import testing
#end testing
# Admin Site Config
admin.sites.AdminSite.site_header = 'Bk Arogyam'
admin.sites.AdminSite.site_title = 'Bk Arogyam'
admin.sites.AdminSite.index_title = 'Bk Arogyam'


urlpatterns = [
        path('testingapp',testing),
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('about',about, name='about'),
    path('events',events, name='events'),
    path('events_detail/<str:e_id>',events_detail, name='events_detail'),
    path('events_detail',events_detail, name='events_detail'),
    path('blogs',blogs, name='blogs'),

    path('blogs_details',blogs_details, name='blogs_details'),
    path('blogs_details/<str:b_id>',blogs_details, name='blogs_details'),
    path('gallery',gallery, name='gallery'),
    path('career',career, name='career'),
    path('videos',videos, name='videos'),
	path("contact",contactus, name="contact"),
    path('download',download, name='download'),
    path('diseases',diseases, name='diseases'),
    path('product',product, name='product'),
    path('allopath_ayurveda',allopath_ayurveda, name='allopath_ayurveda'),
    path('ayurveda_allopath',ayurveda_allopath, name='ayurveda_allopath'),

# --------------------Doctor---------------------------------
    path('doctor_login',doctor_login, name='doctor_login'),
    path('doctor_diseases',doctor_diseases, name='doctor_diseases'),
    path('doctor_profile/<int:id>',doctor_profile, name='doctor_profile'),

# --------------------Employee---------------------------------
    path('employee_login',employee_login, name='employee_login'),
    path('employee_dashboard',employee_dashboard, name='employee_dashboard'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)





