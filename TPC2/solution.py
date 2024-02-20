import sys
import re

def header_sub(match):
    print(match)
    level = len(match.group(1))  
    conteudo = match.group(2)        
    html = f'<h{level}>{conteudo.strip()}</h{level}>' 
    return html

def bold_sub(match):
    print(match)
    conteudo = match.group(1)        
    html = f'<b>{conteudo.strip()}</b>' 
    return html

def italic_sub(match):
    print(match)
    conteudo = match.group(1)        
    html = f'<i>{conteudo.strip()}</i>' 
    return html

file = sys.stdin.read()

file = re.sub(r'^(#+)(.*)', header_sub, file, flags=re.MULTILINE)
file = re.sub(r'\*\*(.*)\*\*', bold_sub, file, flags=re.MULTILINE)
file = re.sub(r'\*(.*)\*', italic_sub, file, flags=re.MULTILINE)
print(file)