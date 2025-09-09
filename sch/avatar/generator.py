import os

from .enum import Algo
import uuid
from .constants import avatar_algo_functions
from ..logger import Logger

def generate_avatar(code: str=None, algo: Algo=Algo.SHA512, filename: str=None, output_dir: str=None, _return=False):
    """
    根据传入的字符串生成哈希头像，每次的图标都是唯一的
    Args:
        code: 字符串，用于生成哈希头像，如果不传入则默认使用uuid生成随机字符串
        algo: 哈希算法，默认使用SHA512，可选MD5、SHA1、SHA224、SHA256、SHA384、SHA512
        filename: 输出文件名，默认使用{output_dir}/{algo.value}/{source}.png，可自定义
        output_dir: 输出目录，默认使用output，可自定义
    """
    logger = Logger("AvatarGenerator")
    try:
        from PIL import Image, ImageDraw
    except (ModuleNotFoundError, ImportError):
        logger.error('sch-lib[image] is required to use this function.')
        exit(1)
    logger.info(f"Generating avatar for code: {code} with algorithm: {algo.value}")
    if code is None:
        source = uuid.uuid4().hex
    else:
        source = code
    logger.info(f"Source: {source}")
    if output_dir is None:
        output_dir = "output"
    if not output_dir == ".":
        os.makedirs(f"{output_dir}/{algo.value}", exist_ok=True)
    if filename is None:
        filename = f"{output_dir}/{algo.value}/{source}.png"
    else:
        filename = f"{output_dir}/{filename}.png"
    logger.info(f"Output file: {filename}")
    md5 = avatar_algo_functions[algo.value](source.encode("utf-8")).hexdigest()
    logger.info(f"MD5: {md5}")
    size = 10
    image = Image.new("RGB", (size * 5, size * 5))
    draw = ImageDraw.Draw(image)
    for idx in range(15):
        x1 = idx % 3
        x2 = 4 - x1
        y = idx // 3
        color = f"#{md5[:6]}" if int(md5[idx], 16) % 2 else "white"
        draw.rectangle((x1 * size, y * size, (x1 + 1) * size, (y + 1) * size), fill=color, width=0)
        draw.rectangle((x2 * size, y * size, (x2 + 1) * size, (y + 1) * size), fill=color, width=0)
    if _return:
        return image
    else:
        image.save(filename)
        logger.info(f"Avatar saved")
        return None