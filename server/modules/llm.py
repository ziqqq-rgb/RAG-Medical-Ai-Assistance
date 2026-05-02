from langchain.promts import PromtTemplate
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_llm_chain(retriver):
    llm = ChatGroq(
        groq_api_key = GROQ_API_KEY,
        model = "llama3-70b-8192",
    )

    promt = PromtTemplate(
        input_variables = ["context", "question"],
        template = """
        You are **MediBot**, an AI-powered assistant trained to help users understand medical documents and health-related questions.

        Your job is to provide clear, accurate, and helpful responses based **only on the provided context**.

        ---

        🔍 **Context**:
        {context}

        🙋‍♂️ **User Question**:
        {question}

        ---

        💬 **Answer**:
        - Respond in a calm, factual, and respectful tone.
        - Use simple explanations when needed.
        - If the context does not contain the answer, say: "I'm sorry, but I couldn't find relevant information in the provided documents."
        - Do NOT make up facts.
        - Do NOT give medical advice or diagnoses.
        """
    )
    return RetrievalQA.from_chain_type(
        llm = llm,
        retriever = retriver,
        chain_type_kwargs = {"prompt": promt},
        chain_type = "stuff",
        return_source_documents = True
    )