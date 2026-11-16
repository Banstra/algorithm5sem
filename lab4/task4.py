def is_palindrome(text: str) -> bool:

	if len(text) <= 1:
		return True
	if text[0] != text[-1]:
		return False
	return is_palindrome(text[1:-1])

a = input("Введите строку: ")

if is_palindrome(a):
    print(f"Строка '{a}' является палиндромом")
else:
    print(f"Строка '{a}' не является палиндромом")