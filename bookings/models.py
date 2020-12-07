from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        ordering = ('first_name', )

class Booking(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creation_date = models.DateTimeField(default="2000-01-01")
    booking_date = models.DateTimeField(default="2000-01-01")
    name = models.TextField()
    address = models.TextField(default='')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ('created', )
