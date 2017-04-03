# Let's look at the lowercase letters.
import string
string.ascii_lowercase

# We will consider the alphabet to be these letters, along with a space.
alphabet = string.ascii_lowercase + " "
'''
# create `letters` here!
letters={}
for i in range(0,len(alphabet)):
    letters[i]=alphabet[i]
'''
letters = dict(enumerate(alphabet))

#print(letters)
encoding={}
encryption_key=3
for k,v in letters.items():
    if encryption_key+k>26:
        encoding[v]=(encryption_key+k)%27
    else:
        encoding[v] = (encryption_key + k)

#print(encoding)

message = "hi my name is caesar"

def caesar(message, encryption_key):
    # return the encoded message as a single string!
    encoding = {}
    for k, v in letters.items():
        if encryption_key + k > 26:
            encoding[v] = (encryption_key + k) % 27
        elif encryption_key+k<0:
            encoding[v] = encryption_key + k+27
        else:
            encoding[v] = (encryption_key + k)

    result=""
    for letter in message:
        result+=letters[encoding[letter]]
    return result

coded_message=caesar(message,3)
print(coded_message)

decoded_message=caesar(coded_message,-3)
print(decoded_message)