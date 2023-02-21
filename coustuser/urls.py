from django.contrib import admin
from django.urls import path
from coustuser import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.coustmer_signup,name="coustmer_signup"),
    path('verify/',views.verify_otp,name="verify"),
    path('login/',views.coustmer_login,name="coustmer_login"),
    path('logout/',views.coustmer_logout,name="coustmer_logout"),
    path('coustmer_home/',views.coustmer_home,name="coustmer_home"),
    path('coustmer_dashboard/',views.coustmer_dashboard,name="coustmer_dashboard"),
    path('coustmer_withdraw/',views.coustmer_withdraw,name="coustmer_withdraw"),
    path('coustmer_success/',views.coustmer_success,name="coustmer_success"),
    path('coustmer_transaction/',views.coustmer_transaction,name="coustmer_transaction"),
    path('credit_card/',views.credit_card,name="credit_card"),
    path('apply1_credit_card/',views.apply1_credit_card,name="apply1_credit_card"),
    path('creadit_card/',views.creadit_card,name="creadit_card"),
    path('cardwithdraw/',views.cardwithdraw,name="cardwithdraw")


    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)