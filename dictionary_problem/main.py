def first_non_repeating_char(s):
    counts = {}
    for i in s:
        counts[i] = counts.get(i, 0) + 1

    for i in s:
        if counts[i] == 1:
            return i

    return None

# Quick test
if __name__ == "__main__":
    print(first_non_repeating_char("Whathat"))        
    print(first_non_repeating_char("testbe"))    
    print(first_non_repeating_char("ttwwoo"))          