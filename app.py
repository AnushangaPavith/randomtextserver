from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Function to generate random JSON responses
def generate_random_response():
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

    response_type = random.choice([1, 2])

    if response_type == 1:
        output = []
        for item in data:
            item = {
                "Product": str(item["Product"]),
                "Price (USD)": str(item["Price (USD)"]),
                "Quantity": str(item["Quantity"]),
                "Category": str(item["Category"])
            }
            output.append(item)

    else:
        output = [
            {
                "Name": "First Name-CM16 M16 L16",
                "Institution ID": 136,
                "Cash Accounts": [
                    {
                        "number": "AS3431124124",
                        "currency": "USD",
                        "balance": 0.0,
                        "blockAmount": 0.0
                    }
                ]
            },
            {
                "Name": "Ravindu Senarathna",
                "Institution ID": 136,
                "Cash Accounts": [
                    {
                        "number": "AS3431124124",
                        "currency": "USD",
                        "balance": 0.0,
                        "blockAmount": 0.0
                    }
                ]
            }
        ]
    
    return {"output": {"output" : {"content": output, "type": "array"}}}


# Function to generate random steps for admin-assist
def generate_admin_assist_response():
    steps = [
        "Step 1: Do something",
        "Step 2: Do something else",
        "Step 3: More steps here",
        "Step 4: And another step"
    ]

    steps_as_string = "\n".join(steps)

    return {"output": {"content": steps_as_string, "type": "text"}}

# Function to generate response for "/task/invoke"
def generate_task_response():
    task_response = {
        "output": {
            "text": [
                {
                    "symbol": "APPL",
                    "order_side": "sell",
                    "qty": 20
                }
            ]
        },
        "callback_events": []
    }

    return task_response


@app.route('/dynamic-data-retrieve/invoke', methods=['POST'])
def random_response():
    # Accept JSON request
    request_data = request.get_json()

    # Generate random response
    response = generate_random_response()

    return jsonify(response)

@app.route('/admin-assist/invoke', methods=['POST'])
def admin_assist_response():
    # Accept JSON request
    request_data = request.get_json()

    # Generate random admin-assist response
    response = generate_admin_assist_response()

    return jsonify(response)

@app.route('/task/invoke', methods=['POST'])
def task_response():
    # Accept JSON request
    request_data = request.get_json()

    # Generate response for "/task/invoke"
    response = generate_task_response()

    return jsonify(response)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
