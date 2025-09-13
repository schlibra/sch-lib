from ..logger import Logger
def html_to_markdown(html):
    logger = Logger("Markdown")
    try:
        from markdownify import markdownify as md
    except (ImportError, ModuleNotFoundError):
        logger.error("sch-lib[markdown] is required to use this function.")
        exit(1)
    return md(html)

def markdown_to_html(markdown):
    logger = Logger("Markdown")
    try:
        from markdown import markdown as md
    except (ImportError, ModuleNotFoundError):
        logger.error("sch-lib[markdown] is required to use this function.")
        exit(1)
    return md(markdown)
