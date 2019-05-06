from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('users.urls')),

    path('passwordreset/',
        auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'),
        name = "password_reset"), #html_email_template_name = 'users/custom_email.html')
    path('passwordreset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'),name = "password_reset_confirm"),
    path('passwordreset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'),name = "password_reset_done"),
    path('passwordreset_complete',auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'),name = "password_reset_complete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
