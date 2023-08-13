from typing import Any
from django.db import models



class File(models.Model):
    file_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self) -> str:
        return super().__str__()
