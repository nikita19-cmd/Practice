# Global, local variables

```
def greet():
    message = "How are you?"          ##local
    print("Message inside function:", message)

message = "How you doing?"           ##global
print("Message outside function:", message)
greet()
```
# Output
```
Message outside function: How you doing?
Message inside function: How are you?
