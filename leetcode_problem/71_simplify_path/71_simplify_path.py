# https://leetcode.com/problems/simplify-path/description/
# https://www.youtube.com/watch?v=qYlHrAKJfyA

def simplifyPath(path):
    stack = []
    name = ""

    # /Pictures + "/"
    # /Pictures/
    # + "/" because we want to loop through the end and meet "/"
    # append string to stack
    for c in path + "/":
        if c == "/":
            if name == "..":
                if stack:
                    stack.pop()
            elif name == "." or name == "":
                pass
            else:
                stack.append(name)

            # reset the string
            name = ""
        else:
            # build string name
            name += c

    return "/" + "/".join(stack)



path = "/../"
print(simplifyPath(path))
