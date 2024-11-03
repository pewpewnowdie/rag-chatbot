from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM as Ollama
from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
You are a helpful assistant used by a customer for ISP JioFiber. Answer the following question based only on the provided context:

{context}

---

Question: {question}
Answer this question without mentioning about the context that you have read.
"""

def query_rag(query_text):
    embedding_function = get_embedding_function()
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding_function,
    )

    results = db.similarity_search_with_score(query_text, 5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    # print(prompt)

    model = Ollama(model="llama3", stream=True)
    response = []

    for token in model.stream(prompt):
        print(token, end='', flush=True)
        response.append(token)

    print()

    response_text = "".join(response)
    return response_text