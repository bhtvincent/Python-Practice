from lecture26 import*
import sqlalchemy


engine = create_engine('sqlite:///cs122b.db')
metadata=MetaData(engine)
students = Table('students',metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name',String),
                 Column('grade'),Integer)

Session = sessionmaker(bind=engine)
session=Session()
metadata.create_all(engine)

ins = students.insert().values(id=10,name='Alex',grade=100)
print(ins)
