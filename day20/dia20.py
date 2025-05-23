def contando_vogais(text):
    vogais = "aeiou"
    count = 0 
    for char in text.lower():
        if char in vogais:
            count += 1
    return count

print(f"A palavra 'Python' contém", contando_vogais("python"), "vogal(is)")
print(f"A palavra 'salamandra' contém", contando_vogais("salamandra"), "vogal(is)")
print(f"A palavra 'livros' contém", contando_vogais("livros"), "vogal(is)")