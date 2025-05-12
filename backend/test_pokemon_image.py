import requests

# Define the base URL for the PokeAPI
BASE_URL = "https://pokeapi.co/api/v2"

# Test fetching a Pokemon and extracting the image URL
pokemon_name = "pikachu"
url = f"{BASE_URL}/pokemon/{pokemon_name}"

print(f"Fetching data for Pokemon: {pokemon_name}")
response = requests.get(url)

if response.status_code == 200:
    pokemon_data = response.json()

    # Extract the image URL from the sprites
    image_url = pokemon_data.get("sprites", {}).get("front_default")

    print(f"Pokemon: {pokemon_data.get('name')}")
    print(f"Type: {pokemon_data['types'][0]['type']['name'] if pokemon_data.get('types') else 'unknown'}")
    print(f"Move: {pokemon_data['moves'][0]['move']['name'] if pokemon_data.get('moves') else 'unknown'}")
    print(f"Image URL: {image_url}")

    # Test downloading the image
    if image_url:
        print(f"Downloading image from {image_url}...")
        img_response = requests.get(image_url)
        if img_response.status_code == 200:
            print("Image downloaded successfully!")

            # Save the image to a file
            with open(f"{pokemon_name}.png", "wb") as f:
                f.write(img_response.content)
            print(f"Image saved to {pokemon_name}.png")
        else:
            print(f"Failed to download image: {img_response.status_code}")
    else:
        print("No image URL available.")
else:
    print(f"Failed to fetch Pokemon data: {response.status_code}")
