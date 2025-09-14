from .table import table
import datetime

HelloGithub = table(
    'hello_github',
    [
        ('id', int, True),
        ('repo_name', str, 100),
        ('year', int),
        ('month', int),
        ('status', str, 5),
    ]
)
VideoList = table(
    'mwcy_video_list',
    [
        ('id', int, True),
        ('video_id', int),
        ('video_name', str, 255),
        ('video_img', str, 500),
        ('video_description', str, 800),
        ('status', int),
    ]
)
VideoLink = table(
    'mwcy_video_link',
    [
        ('id', int, True),
        ('video_id', int),
        ('video_index', str, 100),
        ('video_link', str, 500),
        ('status', int),
    ]
)
OpenList = table(
    'openlist',
    [
        ('id', int, True),
        ('name', str, 50),
        ('host', str, 100),
        ('port', int),
        ('token', str, 128),
        ('ssl', bool),
        ('enable', bool),
    ]
)
EmailList = table(
    'email_list',
    [
        ('id', int, True),
        ('username', str, 100),
        ('email', str, 100),
        ('password', str, 100),
    ]
)
SteamUser = table(
    'steam_user',
    [
        ('id', int, True),
        ('username', str, 100),
        ('email', str, 100),
        ('password', str, 100),
        ('resume_code', str, 100),
        ('steam_id', str, 100),
        ('created_at', datetime),
        ('cat', str, 100),
        ('hat', str, 100),
        ('steam_index', int),
    ]
)
GithubUser = table(
    'github_user',
    [
        ('id', int, True),
        ('username', str, 100),
        ('password', str, 200),
        ('email', str, 200),
        ('totp', str, 50),
    ]
)
SteamInventory = table(
    'steam_inventory',
    [
        ('id', int, True),
        ('game_id', str, 100),
        ('item_name', str, 100),
        ('item_name_id', str, 100),
        ('color', str, 20),
    ]
)
SteamMarketPrice = table(
    'steam_market_price',
    [
        ('id', int, True),
        ('game_id', str, 100),
        ('item_name', str, 100),
        ('item_name_id', str, 100),
        ('high_price', str, 100),
        ('low_price', str, 100),
        ('year', int),
        ('month', int),
        ('day', int),
        ('hour', int),
        ('minute', int),
    ]
)
SteamMarketItem = table(
    'steam_market_item',
    [
        ('id', int, True),
        ('game_id', str, 100),
        ('item_name', str, 100),
        ('item_name_id', str, 100),
    ]
)
ProxyPool = table(
    'proxy_pool',
    [
        ('id', int, True),
        ('ip', str, 100),
        ('port', int),
        ('protocol', str, 100),
        ('location', str, 100),
        ('available', bool),
    ]
)
SteamMarketHistory = table(
    'steam_market_history',
    [
        ('id', int, True),
        ('trade_id', str, 100),
        ('action', str, 100),
        ('price', str, 100),
        ('date', str, 100),
        ('game_name', str, 100),
        ('item_name', str, 100),
        ('color', str, 20),
        ('value', float),
    ]
)
YesCaptchaUser = table(
    'yes_captcha_user',
    [
        ('id', int, True),
        ('username', str, 100),
        ('password', str, 100),
        ('email', str, 100),
        ('api_key', str, 100),
    ]
)