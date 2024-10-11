str = "thequickbrownfoxjumpsoverthelazydog"
counts = {}

for ch in str:
    if ch in counts:
        counts[ch] += 1
    else:
        counts[ch] = 1

for key in list(counts.keys()):
    if counts[key] == 1:
        counts.pop(key)

print(f"Repeating Characters:")
for key, value in counts.items():
    print(f"{key}: {value}")
