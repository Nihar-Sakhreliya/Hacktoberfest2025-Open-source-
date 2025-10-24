# Filename: longest_substring.py

def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters
    using the sliding window technique.
    """
    # This dictionary stores the most recent index of each character found.
    char_index_map = {}
    
    # 'left' marks the starting index of the current substring (window).
    left = 0
    
    # 'max_length' stores the maximum length found so far.
    max_length = 0

    # 'right' is the ending index of the current window, which we expand.
    for right, char in enumerate(s):
        # Check if the character is already in our current window.
        # If char is in the map AND its last seen index is >= our window's start (left),
        # it means we have a repeat inside our current window.
        if char in char_index_map and char_index_map[char] >= left:
            # We must shrink the window by moving the left pointer
            # to the position right after the last occurrence of this character.
            left = char_index_map[char] + 1
            
        # Update the character's last seen index to the current position.
        char_index_map[char] = right
        
        # Calculate the length of the current valid window.
        current_length = right - left + 1
        
        # Update the max length if the current one is bigger.
        max_length = max(max_length, current_length)
        
    return max_length

# --- Example Usage ---
str1 = "abcabcbb"
print(f"The length of the longest substring in '{str1}' is: {length_of_longest_substring(str1)}")

str2 = "pwwkew"
print(f"The length of the longest substring in '{str2}' is: {length_of_longest_substring(str2)}")

str3 = "tmmzuxt"
print(f"The length of the longest substring in '{str3}' is: {length_of_longest_substring(str3)}")
