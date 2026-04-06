import requests

def fetch_from_openfoodfacts(barcode):
    # Ensure the name below matches the import exactly
    url = f"https://world.openfoodfacts.net/api/v2/product/{barcode}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == 1:
                prod = data.get("product", {})
                return {
                    "product_name": prod.get("product_name", "Unknown"),
                    "brand": prod.get("brands", "Unknown"),
                    "ingredients": prod.get("ingredients_text", "N/A")
                }
    except Exception as e:
        print(f"Connection Error: {e}")
    return None