def space_remover(text):
    text = text.replace(" ", "")
    return text

texting = "integrated development environment"
print(f"{space_remover(texting)}")