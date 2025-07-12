from django.urls import path
from . import views
urlpatterns = [
    path('aindex',views.aindex,name='aindex'),
    path('profile',views.profile,name='profile'),
    path('calender',views.calender,name='calender'),
    path('chartist',views.chartist,name='chartist'),
    path('chartjs',views.chartjs,name='chartjs'),
    path('flot',views.flot,name='flot'),
    path('morris',views.morris,name='morris'),
    path('peity',views.peity,name='peity'),
    path('sparkline',views.sparkline,name='sparkline'),
    path('compose',views.compose,name='compose'),
    path('inbox',views.inbox,name='inbox'),
    path('read',views.read,name='read'),
    path('summernote',views.summernote,name='summernote'),
    path('element',views.element,name='element'),
    path('pickers',views.pickers,name='pickers'),
    path('validation',views.validation,name='validation'),
    path('wizard',views.wizard,name='wizard'),
    path('index2',views.index2,name='index2'),
    path('productadmin',views.productadmin,name='productadmin'),
    path('layout',views.layout,name='layout'),
    path('jqvmap',views.jqvmap,name='jqvmap'),
    path('error400',views.error400,name='error400'),    
    path('error403',views.error403,name='error403'),
    path('error404',views.error404,name='error404'),
    path('error500',views.error500,name='error500'),    
    path('error503',views.error503,name='error503'),    
    path('lockscreen',views.lockscreen,name='lockscreen'),    
    path('',views.alogin,name='alogin'),
    path('register',views.register,name='register'), 
    path('logout',views.logout,name='logout'), 
    path('otp',views.otp,name='otp'),
    path('fpassword',views.fpassword,name='fpassword'),    
    path('bootstrap',views.bootstrap,name='bootstrap'),
    path('fotp',views.fotp,name='fotp'),
    path('chpassword',views.chpassword,name='chpassword'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('enable/<int:xy>',views.enable,name='enable'),
    path('editproduct/<int:xy>',views.editproduct,name='editproduct'),
    path('disable/<int:xy>',views.disable,name='disable'),
    path('productdelete/<int:xy>',views.productdelete,name='productdelete'),
    path('usermanage/',views.usermanage,name='usermanage'),
    path('userview/<int:xy>',views.userview,name='userview'),
    path('enquiry/',views.enquiry,name='enquiry'),
    path('areview/',views.areview,name='areview'),
    

    
    
    


 
    
    
    
]

