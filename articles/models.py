from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    # 유저 모델을 참조하는 경우
    # 방법1 (2번줄과 함께 사용하므로 권장하지 않음) : 클래스 이름이 바뀔경우, 가져오는 클래스가 달라지고, 인자 이름도 달라지므로)
    # user = models.ForeignKey(, on_delete=models.CASCADE)
    # 방법2 : settins.AUTH_USER_MODEL == 'accounts.User' (3번줄과 함께 사용)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 방법3 : get_user_model() == 'accounts.User' (4번줄과 함께 사용)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

