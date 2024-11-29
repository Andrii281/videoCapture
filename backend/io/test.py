import logging
from main import sio

logger = logging.getLogger(__name__)

@sio.on("connect")
async def connect(sid, env):
    print("new connect", str(sid))

@sio.on("msg")
async def sendMessage(sid):
    print("msg", str(sid))
    logger.info(f"msg: {str(sid)}")