<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:51:56
 * @FilePath: /xy_django_model/readme/README.zh-hant.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_model

- [简体中文](../README.md)
- [繁體中文](README.zh-hant.md)
- [English](README.en.md)

## 說明

Django模型的一些工具.

## 程式碼庫

- <a href="https://github.com/xy-web-service/xy_django_model.git" target="_blank">Github位址</a>  
- <a href="https://gitee.com/xy-opensource/xy_django_model.git" target="_blank">Gitee位址</a>  
- <a href="https://gitcode.com/xy-opensource/xy_django_model.git" target="_blank">GitCode位址</a>  

## 安裝

```bash
# bash
pip install xy_django_model
```

## 使用

```python
# models.py


import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models

from xy_django_model.model import gen_upload_to


# 图片存储路径为 <MEDIA_ROOT>/Resource/images/<图片文件名>.<图片文件后缀>
@gen_upload_to
def images(instance=None, filename=None):
    pass


# 图片存储路径为 <MEDIA_ROOT>/Resource/mini/thumbnail/<图片文件名>.<图片文件后缀>
# 根据函数命名来设置图片存储路径,将替换函数名中的"__"两行底杠为文件路径的斜杠"/"
@gen_upload_to
def mini__thumbnail(instance=None, filename=None):
    pass


class MImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_at = models.DateTimeField(
        verbose_name=_("创建时间"),
        auto_now_add=True,
        editable=True,
    )
    update_at = models.DateTimeField(
        verbose_name=_("更新时间"),
        auto_now_add=True,
        editable=True,
    )
    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        default=uuid.uuid4,
        editable=True,
        unique=True,
        null=True,
    )
    is_active = models.BooleanField(
        verbose_name=_("是否启用"),
        null=True,
        blank=True,
        default=False,
    )
    image = models.ImageField(
        verbose_name=_("图片"),
        upload_to=images,
        null=True,
        blank=True,
        default=None,
        help_text=_("图片"),
    )
    mini_thumbnail = models.ImageField(
        verbose_name=_("迷你缩略图"),
        upload_to=mini__thumbnail,
        null=True,
        blank=True,
        default=None,
        help_text=_("迷你缩略图"),
    )

    class Meta:
        verbose_name = _("图片")
        verbose_name_plural = _("图片")
        app_label = "Resource"

    def __str__(self):
        return f"{self.id}. {self.identifier}"

```


##### 運轉 [範例工程](../samples/xy_web_server_demo)

> 執行 xy_web_server -w django start 後
> 造訪 http://127.0.0.1:8401/admin/ 進行驗證（使用者名稱: root, 密碼: 1)
> 儲存圖片後可以在範例工程找尋圖片存在路徑進行驗證

> 範例工程具體使用方式請移步 <b style="color: blue">xy_web_server.git</b> 下列倉庫
> - <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github位址</a>  
> - <a href="https://gitee.com/xy-opensource/xy_web_server.git" target="_blank">Gitee位址</a>  
> - <a href="https://gitcode.com/xy-opensource/xy_web_server.git" target="_blank">GitCode位址</a>  


## 許可證
xy_django_model 根據 <木蘭寬鬆許可證, 第2版> 獲得許可。有關詳細信息，請參閱 [LICENSE](../LICENSE) 文件。

## 捐贈

如果小夥伴們覺得這些工具還不錯的話，能否請咱喝一杯咖啡呢?  

![Pay-Total](./Pay-Total.png)

## 聯繫方式

```
微信: yuyangiit
郵箱: yuyangit.0515@qq.com
```