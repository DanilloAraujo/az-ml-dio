import openai
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import QueryType

search_endpoint = "https://<YOUR_SEARCH_SERVICE_NAME>.search.windows.net"
search_api_key = "<YOUR_SEARCH_API_KEY>"
index_name = "<YOUR_INDEX_NAME>"

openai.api_key = "<YOUR_OPENAI_API_KEY>"

search_client = SearchClient(
    endpoint=search_endpoint,
    index_name=index_name,
    credential=AzureKeyCredential(search_api_key)
)

def query_azure_search(query):
    results = search_client.search(
        query,
        query_type=QueryType.SIMPLE,
        top=5 
    )
    documents = [result['content'] for result in results]
    return documents

def generate_response(query, documents):
    prompt = f"Você é um assistente amigável e paciente especializado em Análise de Redes Sociais (SNA). Responda de forma clara, simples e amigável à seguinte dúvida sobre SNA:\n\nPergunta: {query}\n\nDocumentos:\n" + "\n".join(documents) + "\n\nResposta:"

    response = openai.Completion.create(
        model="gpt-4o",
        prompt=prompt,
        max_tokens=200,
        temperature=0.8 
    )
    return response.choices[0].text.strip()

def chatbot(query):
    documents = query_azure_search(query)
    
    response = generate_response(query, documents)
    
    return response

if __name__ == "__main__":
    user_query = input("Digite sua pergunta sobre Análise de Redes Sociais (SNA): ")
    response = chatbot(user_query)
    print("\nResposta do chatbot:")
    print(response)
