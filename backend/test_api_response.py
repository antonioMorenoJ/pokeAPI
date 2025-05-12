import requests

# Test the API endpoint to check if it returns the image_url
pokemon_name = "bulbasaur"
url = f"http://localhost:5000/pokemon/{pokemon_name}"

print(f"Testing API endpoint for Pokemon: {pokemon_name}")
try:
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("API Response:")
        print(data)
        
        # Check if image_url is in the response
        if "image_url" in data:
            print(f"✅ image_url is present: {data['image_url']}")
        else:
            print("❌ image_url is missing from the response")
            
        # Check other fields
        expected_fields = ["pokemon", "type", "generation", "move"]
        for field in expected_fields:
            if field in data:
                print(f"✅ {field} is present: {data[field]}")
            else:
                print(f"❌ {field} is missing from the response")
    else:
        print(f"Failed to get response: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"Error: {e}")