from datetime import datetime, timedelta, timezone
from opentelemetry import trace

from lib.db import db
#tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run(cognito_user_id=None):
      results = db.query_wrap_array("""
      SELECT
        activities.uuid,
        users.display_name,
        users.handle,
        activities.message,
        activities.replies_count,
        activities.reposts_count,
        activities.likes_count,
        activities.reply_to_activity_uuid,
        activities.expires_at,
        activities.created_at
      FROM public.activities
      LEFT JOIN public.users ON users.uuid = activities.user_uuid
      ORDER BY activities.created_at DESC
      """)
      print(results)
      with pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(results)
          # this will return a tuple
          # the first field being the data
          json = cur.fetchone()
      #return json[0]
      return results
