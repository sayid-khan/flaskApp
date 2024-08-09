from sqlalchemy import create_engine, text
from dotenv import load_dotenv      #just to secure the database details
import os                           #just to secure the database details


def configure():                    #just to secure the database details
    load_dotenv()

configure()

db_connection_str = os.getenv('DB_CONNECTION_STR')      #just to secure the database details



engine = create_engine(db_connection_str, connect_args={
             "ssl": {
                 "ssl_ca": "/etc/ssl/isrgrootx1.pem"
             }
         })

# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
#     result.all = result.all()
#     print(type(result.all))
#     print(result.all)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
  result_all = result.all()
  column = result.keys()
  result_dicts = []
  for row in result_all:
     result_dicts.append(dict(zip(column, row)))
  return result_dicts  
