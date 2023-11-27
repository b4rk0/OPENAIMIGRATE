from openai import OpenAI

client = OpenAI(api_key="your-api-key")

# Set up your OpenAI API key


# Provide a prompt for image generation
prompt = "Draw me a liger having tea with a lion and a tiger"

# Use OpenAI's DALL-E to generate an image based on the prompt
response = client.completions.create(engine="image-alpha-001", prompt=prompt, n=1, stop=None)

# Extract the generated image URL from the response
image_url = response["choices"][0]["image"]["url"]

# Display or use the generated image as needed
print("Generated Image URL:", image_url)
