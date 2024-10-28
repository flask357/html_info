import requests
from pyfiglet import Figlet
from colorama import Fore


def main():
  preview_text = Figlet(font='slant')
  print(Fore.RED + preview_text.renderText('HTML INFO'))


  web = input(Fore.GREEN + "Введите ссылку на ресурс html код которого необходимо получить: ")
  response = requests.post(web)
  print(Fore.GREEN + str(response.text))

if __name__ == '__main__':
  main()