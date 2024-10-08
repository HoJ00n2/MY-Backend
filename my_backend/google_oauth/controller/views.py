from urllib import parse
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from google_oauth.serializer.google_oauth_url_serializer import GoogleOauthUrlSerializer
from google_oauth.serializer.google_oauth_access_token_serializer import GoogleOauthAccessTokenSerializer
from google_oauth.service.google_oauth_service_impl import GoogleOauthServiceImpl


class GoogleOauthView(viewsets.ViewSet):
    googleOauthService = GoogleOauthServiceImpl.getInstance()

    def googleOauthURI(self, request):
        url = self.googleOauthService.googleLoginAddress()
        print(f"url:", url)
        serializer = GoogleOauthUrlSerializer(data={'url': url})
        serializer.is_valid(raise_exception=True)
        print(f"validated_data: {serializer.validated_data}")
        return Response(serializer.validated_data)

    def googleAccessTokenURI(self, request):
        serializer = GoogleOauthAccessTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data
        code = parse.unquote(code['code'])
        print(f"code: {code}")
        try:
            accessToken = self.googleOauthService.requestAccessToken(code)
            print(f"accessToken: {accessToken}")
            return JsonResponse({'accessToken': accessToken})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def googleUserInfoURI(self, request):
        accessToken = request.data.get('access_token')
        try:
            user_info = self.googleOauthService.requestUserInfo(accessToken)
            return JsonResponse({'user_info': user_info})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
