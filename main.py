def main(): 
    with open("/home/wizar/workspace/github.com/Talell-beep/bookbot/books/frankenstein.txt") as f:
        file_contents=f.read()
    #print(file_contents)
    print(wordCount(file_contents))
def wordCount(passage):
    broken = passage.split()
    return len(broken)
def letterCount(passage):
    readable = passage.lower
    
main()