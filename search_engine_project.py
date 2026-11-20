text = input()
word = input()

def search(text, word):
  split_text = text.split(" ")
  if word in split_text:
    return "Word found"
  return "Word not found"

print(search(text, word))