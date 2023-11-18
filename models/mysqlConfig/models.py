from django.db import models


# Create your models here.
# 创建数据库中表对应的类，会自动生成 数据库表 和 字段名

# 创建好以后执行下面命令
# ```
# python manage.py makemigrations
# python manage.py migrate
# ```
# 第一个命令`makemigrations`用于生成数据库迁移文件，它会检测你的模型定义是否有变化。第二个命令`migrate`用于应用这些迁移文件，它会创建或更新数据库中的表结构。

class Movies(models.Model):
    # 在Django中，每个模型都会自动创建一个名为id的主键字段，它是一个自增的整数。
    # 因此，在上面的模型定义中，id字段会自动创建，并且不需要显式地定义。
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=50)
    score = models.FloatField(null=True)
    descr = models.CharField(max_length=50, null=True)
    directer = models.CharField(max_length=255, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "movies"
