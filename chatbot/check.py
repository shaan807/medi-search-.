import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = ''

# Test the API key by making a sample request
response = openai.Completion.create(
    engine="text-davinci-003",  # Use the appropriate GPT-3.5 engine
    prompt="What is the meaning of life?",
    max_tokens=50
)

# Print the response
print(response)
