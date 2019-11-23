#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2019/11/14 0014 14:18

from django.utils.deprecation import MiddlewareMixin

#利用中间件实现登录验证功能
class AuthMD(MiddlewareMixin):
    """
    AuthMD中间件注册后，所有的请求都要走AuthMD的process_request方法。

访问的URL在白名单内或者session中有user用户名，则不做阻拦走正常流程；

如果URL在黑名单中，则返回This is an illegal URL的字符串；

正常的URL但是需要登录后访问，让浏览器跳转到登录页面。

注：AuthMD中间件中需要session，所以AuthMD注册的位置要在session中间的下方。
    """
    white_list = ['/login/','/admin/',]  # 白名单
    balck_list = ['/black/', ]  # 黑名单

    def process_request(self, request):
        from django.shortcuts import redirect, HttpResponse

        next_url = request.path_info
        # print(request.path_info, request.get_full_path())

        if next_url in self.white_list or request.session.get("is_login") =="1":
            return
        elif next_url in self.balck_list:
            return HttpResponse('骚年，离开吧！这不是你能来的地方！')
        else:
            return redirect("/login/?next={}".format(next_url))