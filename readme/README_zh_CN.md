<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:52:11
 * @FilePath: /xy_django_model/readme/README_zh_CN.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_model

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)


## 说明

Django模型的一些工具.

## 源码仓库

- <a href="https://github.com/xy-web-service/xy_django_model.git" target="_blank">Github地址</a>  
- <a href="https://gitee.com/xy-web-service/xy_django_model.git" target="_blank">Gitee地址</a>

## 安装

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

##### 运行 [样例工程](../samples/xy_web_server_demo)

> 运行 xy_web_server -w django start 后
> 访问 http://127.0.0.1:8401/admin/ 进行验证（用户名: root, 密码: 1)
> 保存图片后可以在样例工程找寻图片存在路径进行验证

> 样例工程具体使用方式请移步 <b style="color: blue">xy_web_server.git</b> 下列仓库
> - <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github地址</a>  
> - <a href="https://gitee.com/xy-web-service/xy_web_server.git" target="_blank">Gitee地址</a>

## 许可证
xy_django_model 根据 <木兰宽松许可证, 第2版> 获得许可。有关详细信息，请参阅 [LICENSE](../LICENSE) 文件。

## 捐赠

如果小伙伴们觉得这些工具还不错的话，能否请咱喝一杯咖啡呢?  

![Pay-Total](./Pay-Total.png)


## 联系方式

```
微信: yuyangiit
邮箱: yuyangit.0515@qq.com
```