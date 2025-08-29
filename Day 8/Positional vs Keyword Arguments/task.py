def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()  # Combine names and convert to lowercase

    # Count occurrences of letters in "TRUE" and "LOVE"
    true_count = sum(combined_names.count(letter) for letter in "true")
    love_count = sum(combined_names.count(letter) for letter in "love")

    # Combine counts to form the love score
    love_score = int(f"{true_count}{love_count}")

    print(f"Your Love Score is {love_score}")

    return love_score