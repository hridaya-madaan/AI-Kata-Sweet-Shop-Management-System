from .database import SessionLocal
from .models import User, Product
from .utils import hash_password

db = SessionLocal()

admin = User(username="admin", password=hash_password("admin123"), role="ADMIN")
db.add(admin)

products = [
    Product(name="Gulab Jamun", price=250, stock=50, description="Classic sweet"),
    Product(name="Rasgulla", price=200, stock=40, description="Soft & juicy")
]

db.add_all(products)
db.commit()
