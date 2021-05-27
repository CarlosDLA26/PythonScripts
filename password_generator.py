# Password generator with Python
import random

def password_generator(size=10):
  password = []
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}[]/!#$~%&()=?¿¡+*"
  for i in range(size):
    password.append(random.choice(characters))
  return "".join(password)

def main():
  print(password_generator())

if __name__ == "__main__":
  main()