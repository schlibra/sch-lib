def render_mermaid(graph: str, save_path: str):
    from ..logger import Logger
    logger = Logger("Mermaid")
    import base64
    try:
        import requests
    except (ImportError, ModuleNotFoundError):
        logger.error("sch-lib[request] is required to use this function.")
        exit(1)
    graph_string = base64.urlsafe_b64encode(
        graph.encode('utf-8')
    ).decode('ascii')
    url = f"https://mermaid.ink/img/{graph_string}"
    logger.info(f"Request mermaid graph from {url}")
    res = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(res.content)
        logger.info(f"Save mermaid graph to {save_path}")