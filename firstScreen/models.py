from django.db import models

# Create your models here.
class Member(models.Model):
    BALLON_TYPE = (
        ('1', '左下'),
        ('2', '左上'),
        ('3', '右下'),
        ('4', '右上'),
    )
    FONT_SIZE = (
        ('1', '大'),
        ('2', '中'),
        ('3', '小'),
    )

    title = models.CharField(max_length=20)
    text = models.TextField(max_length=50, default='デフォルトのメッセージ')
    ballon_type = models.CharField(max_length=1, choices=BALLON_TYPE, default='1')
    font_size = models.CharField(max_length=1, choices=FONT_SIZE, default='2')
    # ballon_height = models.IntegerField()
    # ballon_wight = models.IntegerField()
    point_x = models.IntegerField()
    point_y = models.IntegerField()

    # painting_name = models.CharField(max_length=20, default='0_coverpage.png')

    #painting_number = models.IntegerField()

    def __str__(self):
        return self.title

""" class Painting(models.Model):
    title = models.CharField(max_length=10, blank=True, null=True)
    painting = models.CharField(max_length=100, blank=True, null=True)
    path = models.CharField(max_length=40, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    user_id = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_painting'  """