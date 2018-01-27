import os

filepath = os.path.join(".", "paragraph_1.txt")

unique_word_count = {}
total_word_count = 0

with open(filepath) as text:
    
    for row in text:
        words = row.split()
        for word in words:
            total_word_count = total_word_count + 1
            if word in unique_word_count:
                unique_word_count[word] = unique_word_count[word] + 1
            else:
                unique_word_count[word] = 1
            



#remove all characters except letters
removespaces = row.replace(' ', '')
removecommas = removespaces.replace(',', '')
lettersonly = removecommas.replace('.', '')      


# Print Summary
print("Paragraph Analysis")
print("----------------------------")
# # Approximate word count
print(f"Approximate Word Count: {total_word_count}")
print(f"Approximate Unique Word Count: {len(unique_word_count)}")
# Approximate sentence count
print(f"Approximate Sentence Count: {row.count('.')}")
# Approximate letter count (per word)
print(f"Average Letter Count: {len(lettersonly)/(total_word_count)}")
# # Average sentence length (in words)
print(f"Average Sentence Length: {(total_word_count)/(row.count('.'))}")

# Export Summary Data
textpath = "PyParagraph Summary.txt"
with open(textpath, "w", newline="") as text_file:
    text_file.write(f"Paragraph Analysis\n")
    text_file.write(f"___________________\n")
    text_file.write(f"Approximate Word Count: {total_word_count}\n")
    text_file.write(f"Approximate Unique Word Count: {len(unique_word_count)}\n")
    text_file.write(f"Approximate Sentence Count: {row.count('.')}\n")
    text_file.write(f"Average Letter Count (Per Word): {len(lettersonly)/(total_word_count)}\n")
    text_file.write(f"Average Sentence Length (In Words): {(total_word_count)/(row.count('.'))}\n")
    text_file.close()
