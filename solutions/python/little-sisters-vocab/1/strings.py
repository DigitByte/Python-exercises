"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word: str) -> str:
    """Take the given word and add the 'un' prefix."""
    return "un" + word


def make_word_groups(vocab_words: list[str]) -> str:
    """Transform a list containing a prefix and words into a prefixed string."""
    prefix = vocab_words[0]
    # Apply prefix to each remaining word
    prefixed_words = [prefix + word for word in vocab_words[1:]]
    # Join with ' :: ' including the original prefix at start
    return " :: ".join([prefix] + prefixed_words)


def remove_suffix_ness(word: str) -> str:
    """Remove the suffix 'ness' from the word while keeping spelling rules in mind."""
    if word.endswith("ness"):
        base = word[:-4]  # remove 'ness'
        # Handle special case where 'y' changes to 'i' (e.g., "happiness" -> "happy")
        if base.endswith("i"):
            return base[:-1] + "y"
        return base
    return word


def adjective_to_verb(sentence: str, index: int) -> str:
    """Change the adjective at the given index in the sentence to a verb by adding 'en'."""
    words = sentence.rstrip(".").split()
    return words[index] + "en"
