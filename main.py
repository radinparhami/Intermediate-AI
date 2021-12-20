from re import finditer


def find_text(data, element) -> dict:
    result = finditer(element.lower(), data.lower())
    output: dict = {}
    for results in result:
        if element in output:
            output[element].append(results.span())
        else:
            output[element] = [results.span()]
    return output


Text = "Python programmers know that Python is a high-level programming language !"
Element = "Python"
if __name__ == "__main__":
    print(find_text(Text, Element))
