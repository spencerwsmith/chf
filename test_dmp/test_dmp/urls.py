from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_dmp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
          # the django_mako_plus controller handles every request - this line is the glue that connects Mako to Django
      url(r'^.*$', 'django_mako_plus.controller.router.route_request' ),
)
