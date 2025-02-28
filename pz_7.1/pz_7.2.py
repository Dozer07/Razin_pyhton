def replace_first_occurrence(S, S1, S2):
    return S.replace(S1, S2, 1)

S = "Привет, мир! Привет, мир!"
S1 = "Привет"
S2 = "Здравствуйте"

result = replace_first_occurrence(S, S1, S2)
print(result)
