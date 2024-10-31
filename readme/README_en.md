<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:52:22
 * @FilePath: /xy_django_model/readme/README_en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_model

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## Description

Some tools for Django models.

## Source Code Repositories

- <a href="https://github.com/xy-web-service/xy_django_model.git" target="_blank">Github</a>  
- <a href="https://gitee.com/xy-web-service/xy_django_model.git" target="_blank">Gitee</a>

## Installation

```bash
# bash
pip install xy_django_model
```

## How to use

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


##### Run [Sample Project](../samples/xy_web_server_demo)

> For detailed usage of the sample project, please go to the following repository <b style="color: blue">xy_web_server.git</b> 
> - <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github</a>  
> - <a href="https://gitee.com/xy-web-service/xy_web_server.git" target="_blank">Gitee</a>


## License
xy_django_model is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![Pay-Total](./Pay-Total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```