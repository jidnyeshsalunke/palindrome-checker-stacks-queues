# palindrome-checker-stacks-queues
A Python implementation of a Palindrome Checker using Stack and Queue data structures. The program checks whether a word or phrase reads the same forward and backward by comparing characters using LIFO and FIFO operations.

# Palindrome Checker Using Stacks and Queues

## Project Information
- Subject: Data Structures
- Course: SPPU SE Computer Engineering
- Programming Language: Python
- Concepts: Stack and Queue

## Abstract
This project checks whether a given word or phrase is
a palindrome using stack and queue data structures.
A palindrome reads the same forward and backward.

The stack follows the Last In, First Out (LIFO)
principle, while the queue follows the First In,
First Out (FIFO) principle. By comparing characters
removed from both structures, the program determines
whether the input is a palindrome.

Spaces, punctuation, and letter case are ignored.

## Objectives
- Understand stack and queue operations.
- Implement LIFO and FIFO principles.
- Check words and phrases for palindrome properties.
- Apply data structures to a practical problem.

## Data Structures Used
- Stack: Stores characters in reverse-removal order.
- Queue: Stores characters in original order.

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Run:

   python palindrome_checker.py

5. Enter a word or phrase.

## Algorithm
1. Read the input string.
2. Convert it to lowercase and remove spaces
   and punctuation.
3. Insert each character into a stack and queue.
4. Remove one character from each structure.
5. Compare the characters.
6. If any pair differs, the input is not a palindrome.
7. If all pairs match, the input is a palindrome.

## Complexity Analysis
Time Complexity: O(n)
Space Complexity: O(n)

Here, n is the length of the input string.

## Applications
- Text processing.
- String analysis.
- Learning stack and queue operations.
- Basic word and phrase validation.

## Conclusion
This project demonstrates the practical use of stacks
and queues to check palindrome strings. It provides
an understanding of LIFO and FIFO operations and
their application in string processing.
```

## 5. Sample output

<box border radius="lg" padding={3} gap={2}>
  <text color="secondary" size="sm">Example 1</text>
  ```text
  Enter a word or phrase: madam
  Result: It is a palindrome.
  ```
  <divider color="subtle"/>
  <text color="secondary" size="sm">Example 2</text>
  ```text
  Enter a word or phrase: hello
  Result: It is not a palindrome.
  ```
  <divider color="subtle"/>
  <text color="secondary" size="sm">Example 3</text>
  ```text
  Enter a word or phrase: Never odd or even
  Result: It is a palindrome.
  ```
</box>

## 6. GitHub topics

`python` · `data-structures` · `stack` · `queue` · `palindrome-checker` · `string-processing` · `sppu`

## 7. Upload to GitHub

1. Open <Link url="https://github.com/new" title="GitHub — Create a new repository"/>.
2. Enter the repository name `palindrome-checker-stacks-queues`.
3. Add the repository description given above.
4. Select **Public** if you want to showcase the project.
5. Create the repository.
6. Add `palindrome_checker.py` and `README.md`.
7. Click **Commit changes**.

**Mini-project concept:** The stack retrieves characters in reverse order, whereas the queue retrieves them in their original order. If every corresponding character matches, the input is a palindrome.