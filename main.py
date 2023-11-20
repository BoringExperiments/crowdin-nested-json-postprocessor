import os
import lib.cleanup as cleanup


def main():
  for file in os.listdir('input'):
    with open(f"{os.path.join('input')}/{file}", 'r', encoding='utf8') as f:
      data = f.read()
      remove_empty = cleanup.remove_empty(data)
      # format = formatter.format_json(remove_empty)
      print(f"⚙️ {file} have been successfully formatted!")
    with open(f"{os.path.join('output')}/{file}", 'w', encoding='utf8') as f:
      f.write(remove_empty)
      print(f"🥞 {file} have been successfully written to output!")


main()
