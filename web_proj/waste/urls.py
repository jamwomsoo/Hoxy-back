from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('select_waste_type/', csrf_exempt(views.select_waste_type), name="waste_type_db"),
    path('select_waste_type_top5/', csrf_exempt(views.select_waste_type_top5), name="select_waste_type_top5"),
    path('insert_waste_apply_info/', csrf_exempt(views.insert_waste_apply_info), name="insert_waste_apply_info"),
    path('select_waste_apply_info/', csrf_exempt(views.select_waste_apply_info), name="select_waste_apply_info"),
    path('insert_board/', csrf_exempt(views.insert_board), name="insert_board"),
    path('select_board_title/', csrf_exempt(views.select_board_title), name="select_board_title"),
    path('select_board/', csrf_exempt(views.select_board), name="select_board"),
    path('update_board/', csrf_exempt(views.update_board), name="update_board"),
    path('delete_board/', csrf_exempt(views.delete_board), name="delete_board"),
    path('insert_board_review/', csrf_exempt(views.insert_board_review), name="insert_board_review"),
    path('select_board_review/', csrf_exempt(views.select_board_review), name="select_board_review"),
    path('insert_user_info/', csrf_exempt(views.insert_user_info), name="insert_user_info"),
    path('KakaoPay/',csrf_exempt(views.KakaoPay), name="KakaoPay"),
    path('KakaoPaySuccess/',csrf_exempt(views.KakaoPaySuccess), name="KakaoPaySuccess"),
    path('test/', csrf_exempt(views.test), name="test"),
    path('get_image/', csrf_exempt(views.get_image), name="get_image")

    
    #path('index/', csrf_exempt(views.index), name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)