from typing import Dict

def addition(a: int, b: int) -> Dict[str, int]:
    result = a + b
    return {"result": result}

def subtraction(a: int, b: int) -> Dict[str, int]:
    result = a - b
    return {"result": result}

def multiplication(a: int, b: int) -> Dict[str, int]:
    result = a * b
    return {"result": result}