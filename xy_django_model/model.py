# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "model"
"""
  * @File    :   model.py
  * @Time    :   2023/04/27 21:07:47
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
"""

from django.contrib.contenttypes.models import ContentType
import os
from functools import wraps


def default_upload_to(instance, path, filename):
    if path == None:
        path = ""
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "{app_label}/{class_name}{path}/{filename}".format(
        app_label=ContentType.objects.get_for_model(instance).app_label,
        path=path,
        class_name=instance.__class__.__name__,
        filename=filename,
    )


def gen_upload_to(func):
    path = ""
    if func:
        path = os.path.join("/", "/".join(func.__name__.split("__")))

    @wraps(func)
    def decorated(instance, filename):
        return default_upload_to(instance=instance, path=path, filename=filename)

    return decorated


def related_name(extension="related"):
    return f"%(app_label)s_%(class)s_{extension}"
