import json
import requests
from django.shortcuts import render
from .forms import ApiRequestForm

def api_tester(request):
    response_data = None
    if request.method == 'POST':
        form = ApiRequestForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            method = form.cleaned_data['method']
            headers = form.cleaned_data['headers']
            body = form.cleaned_data['body']

            try:
                headers_dict = json.loads(headers) if headers else {}
            except json.JSONDecodeError:
                form.add_error('headers', 'Headers must be valid JSON.')
                return render(request, 'testapp/api_tester.html', {'form': form})

            try:
                data = json.loads(body) if body else None
            except json.JSONDecodeError:
                form.add_error('body', 'Body must be valid JSON.')
                return render(request, 'testapp/api_tester.html', {'form': form})

            try:
                resp = requests.request(method, url, headers=headers_dict, json=data)
                response_data = {
                    'status_code': resp.status_code,
                    'headers': dict(resp.headers),
                    'body': resp.text,
                }
            except Exception as e:
                response_data = {'error': str(e)}
    else:
        form = ApiRequestForm()

    return render(request, 'testapp/api_tester.html', {'form': form, 'response': response_data})
