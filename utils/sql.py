import config as cfg
import aiosqlite
from datetime import datetime
from loguru import logger
import uuid
class init_db():
    async def init(self):
        self.super()

class Logger():
    # Adding a log to the database
    async def addLog(user_ip: str, logger_id: str) -> bool:
        async with aiosqlite.connect(cfg.db_path) as db:
            async with db.execute("SELECT count(*) FROM loggers WHERE id = ?", (logger_id,)) as data:
                data = data.fetchone()
                if(data[0] > 0):
                    await db.execute("INSERT INTO logs (ip, logger_id, date) VALUES (?, ?, ?)", (user_ip, logger_id, datetime.now()))
                    return True
                else:
                    return False
    # Removing the logger from the database
    async def removeLogger(logger_id: str) -> bool:
        async with aiosqlite.connect(cfg.db_path) as db:
            try:
                await db.execute("DELETE * FROM logs WHERE logger_id = ?", (logger_id,))
                await db.commit()
                return True
            except Exception as e:
                logger.error(e)
                return False
    # Getting information about the logger from the database
    async def getLogs(logger_id: str) -> list or bool:
        async with aiosqlite.connect(cfg.db_path) as db:
            async with db.execute("SELECT * FROM logs WHERE logger_id = ?", (logger_id,)) as data:
                data = data.fetchall()
                if(len(data) > 0):
                    return data
                else:
                    return False
    # Creating a logger and adding it to the database
    async def createLogger() -> str:
        async with aiosqlite.connect(cfg.db_path) as db:
            logger_id = uuid.uuid4()
            await db.execute("INSERT INTO loggers (logger_id) VALUES (?)", (logger_id,))
            await db.commit()
            return logger_id