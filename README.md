# cybersecurity-final-project: Hill Cipher Demonstration

This is a demonstration of the Hill Cipher. We made encryption and decryption methods and also a method for breaking the cipher.

## Dependencies / Instructions

Run

```
pip install sympy
pip install numpy
```

to install sympy and numpy and run the programs.

To encrypt:

```
python3 encode.py <key> <message_to_encrypt>
```

To decrypt:

```
python3 decode.py <key> <cipher_text>
```

## Devlog

12/14

- Josephine: Outlined presentation and started explaining encryption/decryption of Hill Cipher. Made functions for inverting a matrix, converting letters into a matrix, and encrypting a message (all before 12/14).
- Shuprovo: Continued trying to work out how breaking the Hill cipher through known-plaintext attacks would be implemented (both in class and at home). Made functions for inverting a 2x2 matrix and correctly implementing decryption using Josephine's helper functions. (Previous sentence was work done before 12/14)

12/15

- Josephine: Worked on breaking the Hill cipher through frequency analysis
- Shuprovo: After working out known-plaintext attacks on paper, worked on implementing a manual version in code

12/16

- Josephine: Added dependencies/instructions; worked on explaining how the Hill Cipher works in the presentation
- Shuprovo: Continued to work out implementing breaking the cipher; had some issues with the matrix inverse modulo calculations but Mr. K gave us permission to use outside libraries

12/17

- Josephine: Worked on the presentation and coming up with examples/challenges.
- Shuprovo: Worked on the presentation and coming up with examples/challenges.

12/20

- Josephine: Worked on the presentation and coming up with examples/challenges to explain matrix operations and encryption.
- Shuprovo: Worked on the presentation and coming up with examples/challenges to explain matrix operations and decryption.

12/21

- Josephine: Finished doing encryption example; came up with encryption challenge.
- Shuprovo: Finished doing decryption example; started thinking of decryption challenges and ways to upscale our code to higher dimensions

12/22

- Josephine: Came up with more encryption challenges.
- Shuprovo: Fixed some mathematical errors in decryption example, started explaining how to break the cipher through known-plaintext attacks

12/23
- Josephine: Finished coming up and solving encryption challenges.

1/3
- Josephine: Completed finishing touches; added sources.
