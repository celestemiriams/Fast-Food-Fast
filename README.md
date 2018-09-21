# Fast-Food-Fast
This is a food delivery service app for a restaurant

[![Build Status](https://travis-ci.org/celestemiriams/Fast-Food-Fast.svg?branch=orders)](https://travis-ci.org/celestemiriams/Fast-Food-Fast)

[![Maintainability](https://api.codeclimate.com/v1/badges/e441ca5a5b9aaeb9d6ba/maintainability)](https://codeclimate.com/github/celestemiriams/Fast-Food-Fast/maintainability)

##   Project Title
    Fast-Food-Fast is an application that provides food delivery services for its users

### Features
- A user can make an order
- A user can get a list of orders
- A user can get a specific order
- A user can update order status

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequistes
Things you need to install and configure the software include: 
- Virtualenv
- Python3
- Flask
- pytest

### Development setup
    
#### Create a virtual environment and activate it
```
 virtualenv venv
 source /env/bin/activate
```

#### Install dependencies
pip3 install -r requirements.txt

#### Run the application
```
cd Fast-Food-Fast
python run.py
```

#### You can access the application End points:
| End Point                    | Verb   | Use                            |
|:---------------------------- |:------:|:------------------------------ |
|/api/v1/orders/               |  GET	| Gets a list of all orders      |
|/api/v1/orders/<int:order_id>/|  GET	| Gets a specific specific order |
|/api/v1/orders/               |  POST  | Posting an order               |
|/api/v1/orders/<int:order_id>/|  PUT	| Updates the status of an order |

###  Running the Tests
```
    To run the tests run:
    pytest test_orders.py
```

###  Versioning
        For versions available check [tags on this repo](https://github.com/celestemiriams/Fast-Food-Fast)

###   Authors
        *Nanteza Miriam

###   Acknowledgments
        kampala Bootcamp 12 fellows