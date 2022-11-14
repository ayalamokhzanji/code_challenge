from django.conf.urls import url
from django.urls import path

from codestar import views

urlpatterns = [
    url(r'^$',views.greetings),
    path('form/<int:id>',views.form),
    url(r'^user/$',views.createUser),
	url(r'^level-one/$',views.levelOne),
    url(r'^level-one/run$',views.levelOneRuncode),
    url(r'^level-two/$',views.levelTwo),
    url(r'^level-two/run$',views.levelTwoRuncode),
    url(r'^level-three/$',views.levelThree),
    url(r'^level-three/run$',views.levelThreeRuncode),

]
