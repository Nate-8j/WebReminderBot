import psycopg2
from psycopg2.extras import RealDictCursor


class DBRepository:
    def __init__(self, bsn):
        self.bsn = bsn

    def connect(self):
        return psycopg2.connect(self.bsn)

    def get_reminders(self, user_id):
        conn = self.connect()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM reminders WHERE user_id = %s", (user_id,))
        rows = cursor.fetchall()
        # data = [dict(row) for row in rows]
        conn.close()
        return list(rows)
