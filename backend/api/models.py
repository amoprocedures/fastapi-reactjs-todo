from uuid import uuid4
from tortoise.models import Model
from tortoise.fields import (
    CharField, UUIDField, BooleanField, DatetimeField
)


class Todo(Model):
    id = UUIDField(pk=True, default=uuid4)
    title = CharField(max_length=100, null=False)
    done = BooleanField(null=False, default=False)
    created_at = DatetimeField(null=True, auto_now_add=True)

    class Meta:
        table = 'todos'  # table name on the db
        ordering = ['-created_at']  # order by c_at DESC
