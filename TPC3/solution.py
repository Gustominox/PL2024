import re

def on_off_dfa(text):
    state = 1  # Estado Inicial
    sum = 0    # Soma inicia a 0
    
    # Regex para capturar Alfabeto
    pattern = re.compile(r'(?:On|Off|\d+|=)', re.IGNORECASE) 
    
    for match in pattern.finditer(text):
        word = match.group()
        print(word)
        if word.lower() == 'on':
            if state == 2:
                state = 1
        elif word.lower() == 'off':
            if state == 1:
                state = 2
        elif word.isdigit():
            if state == 1:
                sum += int(word)
        elif word == '=':
            print("Output:", sum)
            
# Example usage:
text = "Onsdkedfsa10asdwsadwOffasdw=wdmxomv5sdsOnasdon20s30d40af=Off"
on_off_dfa(text)