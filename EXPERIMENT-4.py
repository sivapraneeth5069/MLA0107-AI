def is_possible_mapping(arr, s):
    def is_valid(mapping, word):
        return all(mapping[ch] != -1 for ch in word)
    def calculate_number(mapping, word):
        return int(''.join(str(mapping[ch]) for ch in word))
    def backtrack(index, mapping, used_digits):
        if index == len(unique_chars):
            sum_arr = sum(calculate_number(mapping, word) for word in arr[:-1])
            sum_s = calculate_number(mapping, arr[-1])
            return sum_arr == sum_s
        current_char = unique_chars[index]
        for digit in range(10):
            if digit not in used_digits:
                new_mapping = mapping.copy()
                new_mapping[current_char] = digit
                new_used_digits = used_digits.copy()
                new_used_digits.add(digit)
                if is_valid(new_mapping, arr[index]) and backtrack(index + 1, new_mapping, new_used_digits):
                    return True
        return False
    unique_chars = set(''.join(arr) + s)
    mapping = {ch: -1 for ch in unique_chars}
    return backtrack(0, mapping, set())
arr = ["SEND", "MORE"]
s = "MONEY"
result = is_possible_mapping(arr, s)
if result:
    print("Possible to map strings to S.")
else:
    print("Not possible to map strings to S.")
