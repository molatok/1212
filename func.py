from main import Request, shop1, store1, store2

while True:
    user_input = input("Запрос пользователя: ")
    if user_input == 'стоп':
        print("Ну все, наигрались")
        break
    else:
        try:
            req = Request(user_input)
            req.move()
        except Exception as e:
            print(f'Произошла ошибка {e}, но вы можете попробовать еще раз')
            