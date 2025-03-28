import fitz
import openai
from azure.search.documents import SearchClient
from azure.search.documents.models import SearchQuery
from azure.core.credentials import AzureKeyCredential

openai.api_key = "<SUA-API-KEY-DA-OPENAI>"
endpoint = "https://<SEU-ENDPOINT-AQUI>.search.windows.net"
api_key = "<SUA-CHAVE-AQUI>"
index_name = "<SEU-NOME-DO-ÍNDICE>"

search_client = SearchClient(endpoint=endpoint, index_name=index_name, credential=AzureKeyCredential(api_key))

def extrair_texto_pdf(caminho_pdf):
    documento = fitz.open(caminho_pdf)
    texto_completo = ""
    for pagina in documento:
        texto_completo += pagina.get_text()
    return texto_completo

def buscar_documento(query):
    results = search_client.search(query)
    documentos_encontrados = []
    for result in results:
        documentos_encontrados.append(result)
    return documentos_encontrados

def responder_duvida_sna(pergunta, contexto):
    prompt = f"Com base no seguinte contexto sobre Análise de Redes Sociais (SNA):\n{contexto}\n\nPergunta: {pergunta}\nResposta:"
    resposta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return resposta.choices[0].text.strip()

def fluxo_completo(caminho_pdf, pergunta):
    texto_pdf = extrair_texto_pdf(caminho_pdf)
    
    resultados_busca = buscar_documento("rede social análise")
    
    contexto_relevante = " ".join([doc['conteúdo'] for doc in resultados_busca])
    
    resposta_sna = responder_duvida_sna(pergunta, contexto_relevante)
    return resposta_sna

resposta = fluxo_completo("documento.pdf", "O que é centralidade em análise de redes sociais?")
print(resposta)
