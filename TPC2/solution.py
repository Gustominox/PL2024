import sys
import re

def header_sub(match):
    level = len(match.group(1))  
    conteudo = match.group(2)        
    html = f'<h{level}>{conteudo.strip()}</h{level}>' 
    return html

def bold_sub(match):
    conteudo = match.group(1)        
    html = f'<b>{conteudo.strip()}</b>' 
    return html

def italic_sub(match):
    conteudo = match.group(1)        
    html = f'<i>{conteudo.strip()}</i>' 
    return html

def ordered_list_sub(match):
    itens = match.group(0).split('\n')
    print (match.groups())
    html = f'<ol>\n'
    for item in itens:
        if item != "":
            m = re.match(r'\d\. (.*)',item)
            conteudo = m.group(1)
            html+=f'<li>{conteudo}</li>\n'
    html+='</ol>\n'

    return html

def link_sub(match):
    texto = match.group(1)        
    url = match.group(2)        
    html = f'<a href="{url}">{texto}</a>' 
    return html

def img_sub(match):
    texto = match.group(1)        
    path = match.group(2)        
    html = f'<img src="{path}" alt="{texto}"/>' 
    return html

file = sys.stdin.read()

file = re.sub(r'^(#+)(.*)', header_sub, file, flags=re.MULTILINE)
file = re.sub(r'\*\*(.*)\*\*', bold_sub, file, flags=re.MULTILINE)
file = re.sub(r'\*(.*)\*', italic_sub, file, flags=re.MULTILINE)
file = re.sub(r'(?:\d\. (.*)\n)+', ordered_list_sub, file, flags=re.MULTILINE)
file = re.sub(r'!\[(.*)\]\((.*)\)', img_sub, file, flags=re.MULTILINE)
file = re.sub(r'\[(.*)\]\((.*)\)', link_sub, file, flags=re.MULTILINE)

print(file)