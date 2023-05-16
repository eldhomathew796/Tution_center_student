from unicodedata import name
from django.urls import include, path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('usercreate',views.usercreate,name="usercreate"),
    path('logout',views.logout,name="logout"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('product/',views.product,name="product"),
    
    path('profile',views.profile,name="profile"),
    path('profileuser',views.profileuser,name="profileuser"),
    path('deletedetails/<int:pk>',views.deletedetails,name='deletedetails'),
    path('addimage',views.addimage,name="addimage"),
    path('add',views.add,name="add"),
    path('gallery',views.gallery,name="gallery"),
    path('addcategory',views.addcategory,name="addcategory"),
    path('add_category',views.add_category,name="add_category"),
    path('showimage/<int:pk>',views.showimage,name="showimage"),
    path('show',views.show,name="show"),
    path('cartitem/<int:pk>/<int:k>/',views.cartitem,name='cartitem'),
    path('loadcartitems/<int:pk>',views.loadcartitems,name="loadcartitems"),
    path('addTutors',views.addTutors,name="addTutors"),
    path('showTutors',views.showTutors,name="showTutors"),
    
    path('delete_tutors/<int:pk>',views.delete_tutors,name="delete_tutors"),
    path('edit_tutor_page/<int:pk>',views.edit_tutor_page,name="edit_tutor_page"),
    path('edit_tutor_data/<int:pk>',views.edit_tutor_data,name="edit_tutor_data"),
   



    path('up',views.up,name="up"),
    path('mn/<int:pk>',views.mn,name="mn"),
    path('students',views.students,name="students"),

    ]