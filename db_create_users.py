from SchoolPortal import db
from models import User

# insert data
db.session.add(User("trust", "trustmub@gmail.com", "admin"))
db.session.add(User("admin", "ad@min.com", "admin"))
db.session.add(User("test", "test@test.com", "test"))

# commit the changes
db.session.commit()