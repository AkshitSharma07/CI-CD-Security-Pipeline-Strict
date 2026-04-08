def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def main():
    user_name = "Akshu"
    message = greet(user_name)
    result = add(5, 3)

    print(message)
    print(f"Addition result: {result}")


if __name__ == "__main__":
    main()