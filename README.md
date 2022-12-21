# myAuction
Simple bidding website made with Flask, Flask-sqlalchemy, Bootstrap

## Directory Structure

```
📦 
├─ requirements.txt
├─ LICENSE
├─ Procfile
├─ README.md
├─ main.py
├─ controllers
│  ├─ __init__.py
│  ├─ bidding.py
│  ├─ create_listing.py
│  ├─ delete_product.py
│  ├─ home.py
│  ├─ my_bid.py
│  ├─ profile.py
│  ├─ signin.py
│  ├─ signup.py
│  └─ update.py
├─ models
│  ├─ __init__.py
│  ├─ product.py
│  └─ user.py
└─ views
   ├─ static
   │  └─ css
   │     └─ style.css
   └─ templates
      ├─ No_bid_yet.html
      ├─ No_product.html
      ├─ add_product.html
      ├─ bid.html
      ├─ home.html
      ├─ layout.html
      ├─ my_bidding.html
      ├─ navbar.html
      ├─ profile.html
      ├─ signin.html
      └─ signup.html
```

## Run locally

```
pip install -r requirements.txt
python main.py
```
