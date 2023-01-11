import imp
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

# 기본적으로 AbstractUser를 쓰는데,

# AuthenticationForm
# SetPasswordform
# PasswordChangeForm
# AdminPasswordChangeForm
# User를 참조하는 form이 아니라, Custom user model을 사용해도 오류 안남.

# UserCreationForm
# UserChangeForm
# 이 두개는 Meta class에서 등록된 모델이 user(기본)이어서 반드시 커스텀을 해줘야함.