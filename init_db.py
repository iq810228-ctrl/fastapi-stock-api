from models import Base
from database import engine

Base.metadata.create_all(engine)
print("資料表建立完成！")