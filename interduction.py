# %%
print("Hello")
# by adding # %%, you can create a cell in VS Code
# %%
print("Hello","to","Python")

# %%
print("number",end=":" )
print(1)
print(2)
# %%
name = input("Enter your name: ")
print("welcome", name)

# %%
x = input("Enter First Number: ")
y = input("Enter Second Number: ")
x = int(x)
y = int(y)
res = x + y
print("Sum is", res)
# %%
def evenodd(n):
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")  
n = int(input("Enter a number: "))
evenodd(4)
# %%
