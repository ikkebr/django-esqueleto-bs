from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'base.views.index', name='index'),
    url(r'^cadastro$', 'base.views.cadastro', name='cadastro'),
    url(r'^perfil$', 'base.views.perfil', name='perfil'),
    # url(r'^blog/', include('blog.urls')),

)
