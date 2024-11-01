dictionary = {
  "яблоко": {"apple", "pome"},
  "банан": {"banana"},
  "груша": {"pear"},
  "апельсин": {"orange"},
  "киви": {"kiwi"}
}
print("Добро пожаловать в словарь!")
while True:
  print("\nСписок возможных действий:")
  print('1) нажмите "ctrl+f" для поиска в словаре')
  print('2) нажмите "+" для добавления в словарь')
  print('3) нажмите "esc" для выхода')
  user_input = input("Введите действие: ")
  if user_input == "ctrl+f":
    russian_word = input("Введите русское слово: ")
    if russian_word in dictionary:
      print(f"Переводы слова '{russian_word}': {', '.join(dictionary[russian_word])}")
    else:
      print(f"Слово '{russian_word}' не найдено в словаре.")
  elif user_input == "+":
    russian_word = input("Введите русское слово: ")
    if russian_word in dictionary:
      print("Введите перевод(ы) слова (через пробел). Нажмите 'tab' для завершения ввода, 'enter' - для подтверждения.")
      translations = input()
      while translations.strip() != "":
        if translations.strip() != "\t":
          new_translations = set(translations.split())
          dictionary[russian_word].update(new_translations)
          print(f"Добавлены переводы: {', '.join(new_translations)}")
        translations = input()
      print(f"Переводы слова '{russian_word}': {', '.join(dictionary[russian_word])}")
    else:
      print("Введите перевод(ы) слова (через пробел). Нажмите 'tab' для завершения ввода, 'enter' - для подтверждения.")
      translations = input()
      new_translations = set(translations.split())
      dictionary[russian_word] = new_translations
      print(f"Добавлено новое слово: '{russian_word}' с переводами: {', '.join(new_translations)}")
  elif user_input == "esc":
    print("Завершение работы...")
    break
  else:
    print("Некорректный ввод. Попробуйте снова.")
