# Online Store API

This project is a simple CRUD (Create, Read, Update, Delete) API for an online store, built using Python and MongoDB.

## Features

- User registration and login
- Creating, updating, and deleting product categories
- Creating, updating, and deleting products

## Requirements

- Python 3
- MongoDB

## Installation

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/yourusername/onlinestore-api.git
    ```

2. Navigate to the project directory.

    ```bash
    cd onlinestore-api
    ```

3. Install the required Python packages.

    ```bash
    pip install -r requirements.txt
    ```

4. Make sure MongoDB is running on your machine.

## Usage

1. Start the Flask server.

    ```bash
    python app.py
    ```

2. The API endpoints can be accessed at `http://localhost:5000`.

## Endpoints

- `POST /register`: Register a new user
    - Request body: `{ "username": "user1", "password": "password1" }`

- `POST /login`: Log in a user
    - Request body: `{ "username": "user1", "password": "password1" }`

- `POST /categories`: Create a new category
    - Request body: `{ "name": "category1" }`

- `PUT /categories/<id>`: Update a category
    - Request body: `{ "name": "new_category_name" }`

- `DELETE /categories/<id>`: Delete a category

- `POST /products`: Create a new product
    - Request body: `{ "name": "product1", "amount_in_stock": 100, "price": 19.99 }`

- `PUT /products/<id>`: Update a product
    - Request body: `{ "name": "new_product_name", "amount_in_stock": 50, "price": 14.99 }`

- `DELETE /products/<id>`: Delete a product

## Future Improvements

- Implementing a shopping cart
- Adding user authorization and authentication
- Filtering and sorting products
- Pagination

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



