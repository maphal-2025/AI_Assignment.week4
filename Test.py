from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# 1. Load a pretrained code-summarization model
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("Salesforce/codet5-small")

# 2. Example function to summarize
code = """
def calculate_tax(income, threshold=35000):
    \"""
    Calculates tax owed: 0% up to threshold, 
    20% above threshold.
    \"""
    if income <= threshold:
        return 0
    return (income - threshold) * 0.2
"""

# 3. Tokenize: wrap code in a prompt
inputs = tokenizer("summarize: " + code, return_tensors="pt")

# 4. Generate summary tokens
summary_ids = model.generate(**inputs, max_length=50)

# 5. Decode to text
print(tokenizer.decode(summary_ids[0], skip_special_tokens=True))


Line-by-Line

We pick CodeT5, a lightweight Seq2Seq model fine-tuned on code summarization.

Provide the raw Python function.

Prefix with "summarize:" so the model knows the task.

Generate a concise summary (max 50 tokens).

Convert tokens back to human text: voilà, instant docstring!

5. Demo 3: Generating Unit Tests with a Language Model
5.1 Scenario

You want to auto-generate pytest tests for new features.

python

import openai                                   # pip install openai

openai.api_key = "YOUR_API_KEY"

def generate_tests(code_snippet: str) -> str:
    """
    Send the code to Codex and ask for pytest tests.
    """
    prompt = f"Write pytest tests for this code:\n\n{code_snippet}\n\n# tests\n"
    response = openai.Completion.create(
        engine="code-davinci-002",               # GPT-3 variant tuned for code
        prompt=prompt,
        max_tokens=200,
        temperature=0.2,
        n=1,
        stop=["# end"]
    )
    return response.choices[0].text.strip()

sample = """
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
"""

print(generate_tests(sample))
