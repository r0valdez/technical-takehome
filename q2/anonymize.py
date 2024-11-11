import re

common_names = {"alice", "bob", "charlie", "dave", "eve"}

def anonymize_names_parta(text: str):
    """
    Anonymizes names in the given text by replacing them with 'ANON'. Assume names are capitalized, and no other words are.

    Examples:
        anonymize_names_parta("Alice and Bob are talking to Charlie.") 
        -> "ANON and ANON are talking to ANON."
        
        anonymize_names_parta("Alice, Bob, and Charlie went to the park.") 
        -> "ANON, ANON, and ANON went to the park."
        
        anonymize_names_parta("Dr. Alice visited Prof. Bob at the university.") 
        -> "ANON ANON visited ANON ANON at the university."

    Args:
        text (str): The input text containing names.
 
    Returns:
        str: The text with names anonymized.
    """
    anonymized_text = re.sub(r'\b[A-Z][a-zA-Z]*\b', 'ANON', text)
    return anonymized_text
 
def anonymize_names_partb(text: str):
    """
    Anonymizes names in the given text by replacing them with 'ANON'. Names can take any shape or form.
 
    Examples: (Note: Examples not provided as implementation depends on heuristics)
 
    Args:
        text (str): The input text containing names.
 
    Returns:
        str: The text with names anonymized.
    """
    # Placeholder implementation: This needs heuristics to identify names
    words = text.split()
    anonymized_words = []

    for word in words:
        word_cleaned = re.sub(r'[^\w\s]', '', word).lower()
        
        if word_cleaned in common_names:
            anonymized_words.append("ANON")
        else:
            anonymized_words.append(word)
    
    return ' '.join(anonymized_words)
 
 
if __name__ == '__main__':
    # Example usage
    parta_input_text = "Alice and Bob are talking to Charlie."
    print("Part A")
    print(f"{parta_input_text} -> {anonymize_names_parta(parta_input_text)}")
    print()


    # Example strings- you can add more test strings. No expectation that these all
    # pass!
    partb_test_strings = [
        "Alice and Bob are talking to Charlie about going to New York City.",
        "alice and bob are discussing with Charlie about visiting Los Angeles.",
        "Bob and Eve are planning a trip to paris next summer.",
        "Charlie and Alice met with Dave in San Francisco last week.",
        "eve and Charlie were excited about the event in Chicago.",
        "Charlie and Bob are thinking of moving to Tokyo soon.",
        "Alice and Dave went to see a show in London.",
        "Alice and Bob had dinner with Eve in Madrid.",
        "bob and Eve are going to Sydney for a conference.",
        "Charlie and Alice took a vacation in Rome.",
        "Charlie and Dave are considering a job offer in Berlin.",
        "eve and Charlie are visiting their friend in Amsterdam.",
        "Charlie and Bob are attending a wedding in Bangkok.",
        "Alice and Dave spent their holidays in Barcelona.",
        "Bob and Eve are looking for apartments in Vienna.",
        "Charlie and Dave are organizing an event in Prague.",
        "alice and Charlie are exploring opportunities in Dubai.",
        "Bob and Charlie are discussing their plans in Dublin.",
        "Alice and Bob are thinking about a trip to Vancouver.",
        "Charlie and Eve are preparing for a move to Montreal."
    ]
    print("Part B")
    for input_text in partb_test_strings:
        print(f"{input_text} -> {anonymize_names_partb(input_text)}")