import datetime
import os
import peewee as pw

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(APP_ROOT, 'weasley-clock.db')

db = pw.SqliteDatabase(DB_FILE)


class BaseModel(pw.Model):
    id = pw.PrimaryKeyField()
    created_at = pw.DateTimeField(default=datetime.datetime.now)
    updated_at = pw.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


class Phone(BaseModel):
    mac_address = pw.CharField(unique=True)
    device_name = pw.CharField()
    ipv4_address = pw.CharField()


def setup():
    db.create_tables([Phone], safe=True)
