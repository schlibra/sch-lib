from sch.util.mermaid import render_mermaid

if __name__ == '__main__':
    data = open('charts/1.mermaid', 'r', encoding='utf-8').read()
    render_mermaid(data, '1.jpg')

