from sqlalchemy import Table, MetaData, Column, Integer, String, Boolean, Float, DateTime

HelloGithub = Table(
    'hello_github',
    MetaData(),
    Column('id', Integer(), primary_key=True, autoincrement=True),
    Column('repo_name', String(100)),
    Column('year', Integer()),
    Column('month', Integer()),
    Column('status', String(5)),
    mysql_engine='InnoDB',
)
VideoList = Table(
    'mwcy_video_list',
    MetaData(),
    Column('id', Integer(), primary_key=True, autoincrement=True),
    Column('video_id', Integer()),
    Column('video_name', String(255)),
    Column('video_img', String(500)),
    Column('video_description', String(800)),
    Column('status', Integer()),
    mysql_engine='InnoDB',
)
VideoLink = Table(
    'mwcy_video_link',
    MetaData(),
    Column('id', Integer(), primary_key=True, autoincrement=True),
    Column('video_id', Integer()),
    Column('video_index', String(100)),
    Column('video_link', String(500)),
    Column('status', Integer()),
)
OpenList = Table(
    'openlist',
    MetaData(),
    Column('id', Integer(), autoincrement=True, primary_key=True),
    Column('name', String(50)),
    Column('host', String(100)),
    Column('port', Integer()),
    Column('token', String(128)),
    Column('ssl', Boolean()),
    Column('enable', Boolean()),
    mysql_engine='InnoDB'
)
EmailList = Table(
    'email_list',
    MetaData(),
    Column('id', Integer(), autoincrement=True, primary_key=True),
    Column('username', String(100)),
    Column('email', String(100)),
    Column('password', String(100)),
    mysql_engine='InnoDB'
)
SteamUser = Table(
    'steam_user',
    MetaData(),
    Column('id', Integer(), autoincrement=True, primary_key=True),
    Column('username', String(100)),
    Column('email', String(100)),
    Column('password', String(100)),
    Column('resume_code', String(100)),
    Column('steam_id', String(100)),
    Column('created_at', DateTime()),
    Column('cat', String(100)),
    Column('hat', String(100)),
    Column('steam_index', Integer()),
    mysql_engine='InnoDB'
)
GithubUser = Table(
    'github_user',
    MetaData(),
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(100)),
    Column('password', String(200)),
    Column('email', String(200)),
    Column('totp', String(50)),
    mysql_engine='InnoDB',
)
SteamInventory = Table(
    'steam_inventory',
    MetaData(),
    Column('id', Integer(), autoincrement=True, primary_key=True),
    Column('game_id', String(100)),
    Column('item_name', String(100)),
    Column('item_name_id', String(100)),
    Column('color', String(20)),
    mysql_engine='InnoDB'
)
SteamMarketPrice = Table(
    'steam_market_price',
    MetaData(),
    Column('id', Integer(), autoincrement=True, primary_key=True),
    Column('game_id', String(100)),
    Column('item_name', String(100)),
    Column('high_price', String(100)),
    Column('low_price', String(100)),
    Column('year', Integer()),
    Column('month', Integer()),
    Column('day', Integer()),
    Column('hour', Integer()),
    Column('minute', Integer()),
    mysql_engine='InnoDB'
)
SteamMarketItem = Table(
    'steam_market_item',
    MetaData(),
    Column('id', Integer(), autoincrement=True, primary_key=True),
    Column('game_id', String(100)),
    Column('item_name', String(100)),
    Column('item_name_id', String(100)),
    mysql_engine='InnoDB'
)
ProxyPool = Table(
    'proxy_pool',
    MetaData(),
    Column('id', Integer(), autoincrement=True, primary_key=True),
    Column('ip', String(100)),
    Column('port', Integer()),
    Column('protocol', String(100)),
    Column('location', String(100)),
    Column('available', Boolean()),
    mysql_engine='InnoDB'
)
SteamMarketHistory = Table(
    'steam_market_history',
    MetaData(),
    Column('id', Integer(), autoincrement=True, primary_key=True),
    Column('trade_id', String(100)),
    Column('action', String(100)),
    Column('price', String(100)),
    Column('date', String(100)),
    Column('game_name', String(100)),
    Column('item_name', String(100)),
    Column('color', String(20)),
    Column('value', Float()),
    mysql_engine='InnoDB'
)
YesCaptchaUser = Table(
    'yes_captcha_user',
    MetaData(),
    Column('id', Integer(), autoincrement=True, primary_key=True),
    Column('username', String(100)),
    Column('password', String(100)),
    Column('email', String(100)),
    Column('api_key', String(100)),
)