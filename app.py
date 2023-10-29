from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import markovify

app = Flask(__name__)
CORS(app) 

# Function to generate random JSON responses
def generate_random_response():
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen", "Ivy", "Jack", "Kate", "Liam", "Mia", "Noah", "Olivia", "Sophia", "Thomas", "Victoria", "William", "Zoe"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "San Francisco", "Miami", "Seattle", "Boston", "Denver", "Atlanta", "Dallas", "Philadelphia", "Phoenix", "Detroit", "Las Vegas"]
    data = [
    {
        "Product": "Laptop",
        "Price (USD)": 800,
        "Quantity": 10,
        "Category": "Electronics"
    },
    {
        "Product": "T-shirt",
        "Price (USD)": 20,
        "Quantity": 50,
        "Category": "Clothing"
    },
    {
        "Product": "Coffee Maker",
        "Price (USD)": 50,
        "Quantity": 8,
        "Category": "Appliances"
    },
    {
        "Product": "Running Shoes",
        "Price (USD)": 75,
        "Quantity": 20,
        "Category": "Footwear"
    },
    {
        "Product": "Smartphone",
        "Price (USD)": 600,
        "Quantity": 15,
        "Category": "Electronics"
    },
    {
        "Product": "Headphones",
        "Price (USD)": 30,
        "Quantity": 25,
        "Category": "Electronics"
    }
    ]

    response_type = random.choice(["text", "array"])
    if response_type == "text":
        with open("corpus.txt", "r") as f:
            text_model = markovify.Text(f, state_size=2)

        random_sentence = text_model.make_sentence()

        content = "".join(random_sentence)
    else:
        content = []

        random_value = random.randint(1, 4)
        if random_value == 1:
            for i in range(4):
                item = {
                    "Customer ID": str(62591 + i),
                    "Number": f"ASI{random.randint(100000000, 999999999)}",
                    "Name": str(names[i]),
                    "Display Name": str(names[i]),
                    "Institution ID": "136",
                }
                content.append(item)
        
        elif random_value == 2:
            for i in range(5):
                item = {
                    "Name": str(names[i * -1]),
                    "Age": str(random.randint(20, 60)),
                    "City": str(cities[random.randint(0, len(cities) - 1)])
                }
                content.append(item)
        
        else:
            for item in data:
                item = {
                    "Product": str(item["Product"]),
                    "Price (USD)": str(item["Price (USD)"]),
                    "Quantity": str(item["Quantity"]),
                    "Category": str( item["Category"])
                }
                content.append(item)


    return {"type": response_type, "content": content}

@app.route('/random_response', methods=['POST'])
def random_response():
    # Accept JSON request
    request_data = request.get_json()

    # Generate random response
    response = generate_random_response()

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
