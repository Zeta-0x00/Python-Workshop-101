#!/usr/local/bin/python
#-*- coding: utf-8 -*-

def demo_function(value: int) -> None:
    """
        Uso de try-except-finally
    """
    try:
        # Uso de if-elif-else:
        if value < 0:
            result = "Negative"
        elif value == 0:
            result = "Zero"
        else:
            result = "Positive"

        # Uso de match-case (Python 3.10+)
        match result:
            case "Negative":
                print("The value is negative")
            case "Zero":
                print("The value is zero")
            case "Positive":
                print("The value is positive")
    except Exception as err:
        print(f"An error ocurred: {err}")
    finally:
        print("Execution completed")


if __name__ == "__main__":
    demo_function(-10)
    demo_function(0)
    demo_function(10)
