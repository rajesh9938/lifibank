
from django.contrib import admin
from django.urls import path
from staf import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('coustuser/', include('coustuser.urls')),
    path('',views.home,name="home"),
    path('single/',views.single,name="single"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('features/',views.features,name="features"),
    path('faqs/',views.faqs,name="faqs"),

    path('signup/',views.Signup,name="signup"),
    path('login/',views.Login,name="login"),
    path('logout/',views.Logout,name="logout"),
    path('forget/',views.forget,name="forget"),

    path('apply/',views.apply,name="apply"),
    path('appled_user/',views.appled_user,name="appled_user"),
    path('aproved_user/',views.aproved_user,name="aproved_user"),
    path('aproved/<int:myid>/',views.aprove,name="aproved"),
    path('account_book/<int:myid>/',views.account_book,name="account_book"),
    path('gen_pdf/<int:myid>/',views.gen_pdf,name="gen_pdf"),
    path('Reject/',views.Reject,name="Reject"),
    path('aproved_msg/',views.aproved,name="aproved_msg"),
    path('coustlogin/',views.coustlogin,name="coustlogin"),
    
    path('apply_credit_card/',views.apply_credit_card,name="apply_credit_card"),
    path('applyed_credit_card/<int:myid>/',views.applyed_credit_card,name="applyed_credit_card"),
    path('aproved_credit_card/',views.aproved_credit_card,name="aproved_credit_card"),




]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()