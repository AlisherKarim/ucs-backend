# from django.db import models

# from users.models import User


# class Tag(models.Model):
#   name = models.CharField(max_length=10)
  
#   def __str__(self):
#     return self.name
  
# class Reply(models.Model):
#   created_by = models.ForeignKey(User, related_name="replies", on_delete=models.CASCADE)
#   date_created = models.DateTimeField(auto_now_add=True)
#   text = models.CharField(max_length=200)
#   # reply_discussion = models.ForeignKey(Discussion)
#   # upvotes, downvotes
  
#   def __str__(self):
#     return self.text

# class Discussion(models.Model):
#   title = models.CharField(max_length=80)
#   body = models.CharField(max_length=200)
#   created_by = models.ForeignKey(User, related_name="discussions", on_delete=models.CASCADE)
#   date_created = models.DateTimeField(auto_now_add=True)
#   tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
#   replies = models.ForeignKey(Reply, on_delete=models.CASCADE)
  
#   def __str__(self):
#     return self.title
  