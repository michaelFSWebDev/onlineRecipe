from django.db import models
import re 
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



# Create your models here.
class UserManager(models.Manager):
    
    def validate(self, postData):
        errors = {}
        if len(postData['first_name']) < 4:
            errors['first_name'] = 'First name must be at least 4 characters!'
        if len(postData['last_name']) < 4:
            errors['last_name'] = 'Last name must be at least 4 characters!'

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invaild Email Address'
        
        email_check = self.filter(email=postData['email'])
        if email_check:
            errors['email'] = "Email already used!!"
        
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be 8 characters!!'
        if postData['password'] != postData['confirm']:
            errors['password'] = 'Passwords do not match!'

        return errors

    def authenticate(self, email, password):
        users = self.filter(email=email)
        if not users:
            return False
        
        user = users[0]
        return bcrypt.checkpw(password.encode(), 
        user.password.encode())

    def register(self, postData):
        pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name = postData['first_name'],
            last_name = postData['last_name'],
            email = postData['email'],
            password = pw,
        )



class User(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    # unique makes sure no other email is the same
    # in the database
    email = models.EmailField(unique=True)

    # password is hashed in UserManager by bcrypt
    password = models.CharField(max_length=255)

    # Auto time feild to track
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<User object: {self.first_name} ({self.id})"

    objects = UserManager()