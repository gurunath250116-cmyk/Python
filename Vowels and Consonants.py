text = "Hello World"
vowels = "aeiou"
v_count = sum(1 for ch in text.lower() if ch in vowels)
c_count = sum(1 for ch in text.lower() if ch.isalpha() and ch not in vowels)
print(f"Vowels: {v_count}, Consonants: {c_count}") 