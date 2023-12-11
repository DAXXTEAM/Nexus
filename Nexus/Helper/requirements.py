import asyncio
from os import path
import os
import pornhub_api
import yt_dlp
from Nexus.Helper.errors import FFmpegReturnCodeError, DurationLimitError
from typing import List, Dict, Union
from asyncio import Queue, QueueEmpty as Empty
from pyrogram.types import *



DURATION_LIMIT = 300

active = []


async def get_active_chats() -> list:
    return active

# ===================================================================================== #

admins: Dict[int, List[int]] = {}


def set_admins(chat_id: int, admins_: List[int]):
    admins[chat_id] = admins_


def get_admins(chat_id: int) -> Union[List[int], bool]:
    return admins.get(chat_id, False)

# ===================================================================================== #

def get_url(message_1: Message) -> Union[str, None]:
    messages = [message_1]

    if message_1.reply_to_message:
        messages.append(message_1.reply_to_message)

    text = ""
    offset = None
    length = None

    for message in messages:
        if offset:
            break

        if message.entities:
            for entity in message.entities:
                if entity.type == "url":
                    text = message.text or message.caption
                    offset, length = entity.offset, entity.length
                    break

    if offset is None:
        return None

    return text[offset:offset + length]

def get_file_name(audio: Union[Audio, Voice]):
    ext = audio.file_name.split(".")[-1] if not isinstance(audio, Voice) else "ogg"
    return f'{audio.file_unique_id}.{ext}'



# ===================================================================================== #


queues: Dict[int, Queue] = {}

async def put(chat_id: int, **kwargs) -> int:
    if chat_id not in queues:
        queues[chat_id] = Queue()
    await queues[chat_id].put({**kwargs})
    return queues[chat_id].qsize()

def get(chat_id: int) -> Dict[str, str]:
    if chat_id in queues:
        try:
            return queues[chat_id].get_nowait()
        except Empty:
            return None

def is_empty(chat_id: int) -> bool:
    if chat_id in queues:
        return queues[chat_id].empty()
    return True

def task_done(chat_id: int):
    if chat_id in queues:
        try:
            queues[chat_id].task_done()
        except ValueError:
            pass

def clear(chat_id: int):
    if chat_id in queues:
        if queues[chat_id].empty():
            raise Empty
        else:
            queues[chat_id].queue = []
    raise Empty


# ===================================================================================== #

async def get_audio_stream(link):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": True,
        "no_warnings": True,
    }
    x = yt_dlp.YoutubeDL(ydl_opts)
    info = x.extract_info(link, False)
    audio = os.path.join(
        "downloads", f"{info['id']}.{info['ext']}"
    )
    if os.path.exists(audio):
        return audio
    x.download([link])
    return audio



async def get_video_stream(link):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": True,
        "no_warnings": True,
    }
    x = yt_dlp.YoutubeDL(ydl_opts)
    info = x.extract_info(link, False)
    video = os.path.join(
        "downloads", f"{info['id']}.{info['ext']}"
    )
    if os.path.exists(video):
        return video
    x.download([link])
    return video


