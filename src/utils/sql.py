import config as cfg
import aiosqlite
import os
from datetime import datetime
from loguru import logger
import uuid
import aiofiles

# Creating a database if it does not exist
class init_db():
    async def __init__():
        if os.path.isfile(cfg.db_path):
            pass
        else:
            async with aiofiles.open(cfg.db_path, mode='a+') as f:
                await f.write()
            async with aiosqlite.connect(cfg.db_path) as db:
                await db.execute("CREATE TABLE IF NOT EXISTS loggers (id INTEGER PRIMARY KEY, logger_id TEXT)")
                await db.excute("CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, ip TEXT, logger_id TEXT, date TEXT)")
                await db.commit()
        

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