# Password cracker 

Developed during October, 2019.

## Description

A simple command-line interface for cracking passwords. It is setup to crack SHA256  passwords appended with salt using dictionary and hybrid attacks, but can be modified with minimal effort. One can easily change the hashfunction, the salt position, and write new attacks.

## Running

Built with Python 3.7.2 using

```
• argparse
• hashlib
• tqdm
```

In `/scripts` use `python3 main.py <attacktype> <hashfile> <wordfile>`. <br/>

- `attacktype` <br/>
The attack type used. Choices: `d: dictionary`, `h:hybrid`.
- `hashfile` <br/>
The name of the .txt file containing the salts and the hexadecimal representation of the hashes, e.g.,  `35501f52a4652dea:8071430e01f99174e749b5787328f900ce6343c330ba607ebb4fbc5c8b15a559`, on each line.
- `wordfile` <br/>
The name of the .txt file containing the password guesses on each line. 

If any passwords are found, they are printed along with the corresponding salt and hash, e.g., `35501f52a4652dea:8071430e01f99174e749b5787328f900ce6343c330ba607ebb4fbc5c8b15a559:tactlessness`.

## Author

[Rustam Latypov](mailto:rustam.latypov@aalto.fi)
