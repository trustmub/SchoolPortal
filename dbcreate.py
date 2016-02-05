from SchoolPortal import db
from models import BlogPost

# create the database and the database tables
db.create_all()

# inserts

# db.session.add(BlogPost("Good", "I\'m good."))
# db.session.add(BlogPost("Well", "I\'m well."))
# db.session.add(BlogPost("wonderful", "I\'m wonderful."))

# db.session.add(Students("","Tichaona","","Midzi"))


# commit the changes

db.session.commit()