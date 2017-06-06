from django.http import HttpResponse
def index(request):
    html = """
            <h1>Atividade Tarefa LPC</h1>
            """
    return HttpResponse(html)
