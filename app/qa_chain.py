from transformers import pipeline

class QAGenerator:
    def __init__(self):
        self.model = pipeline("text2text-generation", model="google/flan-t5-small", max_length=512)

    def generate_answer(self, question, context):
        prompt = f"""Answer the question using the following context.
If you don't know the answer, say "I don't know".

Context:
{context}

Question:
{question}
"""
        response = self.model(prompt)
        return response[0]['generated_text']
