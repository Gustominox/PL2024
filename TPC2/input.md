# Titulo 1

## Titulo 2

### Titulo 3

#### Titulo 4

- Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"

In: `# Exemplo`

Out: `<h1>Exemplo</h1>`

- Bold: pedaços de texto entre "**":
  
In: Este é um `**exemplo**`

Out: Este é um `<b>exemplo</b>`

- Itálico: pedaços de texto entre "*":
  
In: Este é um `*exemplo*`

Out: Este é um `<i>exemplo</i>`

- Lista numerada:

In:

```Markdown
1. Primeiro item
2. Segundo item
3. Terceiro item
```

Out:

```html
<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>
```

- Link: [texto](endereço URL)

In:

```Markdown
Como pode ser consultado em [página da UC](http://www.uc.pt)
```

Out:

```html
Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>
```

- Imagem: ![texto alternativo](path para a imagem)

In: Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
Out: Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/>