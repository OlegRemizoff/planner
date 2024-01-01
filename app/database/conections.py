from sqlmodel import SQLModel, Session, create_engine


database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}
engine_url = create_engine(database_connection_string, echo=True, connect_args=connect_args)

def connect():
    '''создем bd, а также таблицу Events и сохраним сеанс в нашем приложении, get_session()'''
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session
