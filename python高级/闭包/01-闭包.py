def test(number):
	print("-----1----")

	def test_in(number2):
		print("-----2-----")
		print(number+number2)

	print("---3----")
	return test_in

ret = test(10)
print('-'*30)
ret(1)
ret(2)
ret(200)