from pdf_utils import extract_text_from_pdf
from anthropic_client import AnthropicClient

def answer_question(pdf_path, question):
    pdf_text = extract_text_from_pdf(pdf_path)
    client = AnthropicClient()
    
    prompt = f"""
    Here's the content of a PDF document:

    {pdf_text}

    Based on the information in the document, please answer the following question:

    {question}

    If the answer is not found in the document, please say so.
    """

    answer = client.query_claude(prompt)
    return answer