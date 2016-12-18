import collections

def main():
    # Read in the input
    with open("InputDay06.txt") as f:
        inputStr = f.readlines()
    wordList = [w.strip() for w in inputStr]

    # Initialize the result string
    ans = ""

    # For each column...
    for i in range(len(wordList[0])):

        # Find the least common letter and add it to the result
        letterList = [w[i] for w in wordList]
        letterCount = collections.Counter(letterList)
        ans += letterCount.most_common()[-1][0]

    # Print the result
    print(ans)

if __name__ == "__main__":
    main()