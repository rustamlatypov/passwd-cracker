# Password cracker 

Developed during October, 2019.

## Description

A simple command-line interface for cracking passwords. It is setup to crack salted SHA256  passwords, . 

## Running

Built with Python 3.7.2 using

```
argparse
hashlib
tqdm
```

In `/scripts` use `python3 main.py <attacktype> <hashfile> <wordfile>`. <br/>

- `attacktype`: char <br/>
The attack type used. Choices: `d: dictionary`, `h:hybrid`.
- `hashfile`: str <br/>
The name of the `.txt` file containing the salts and the hexadecimal representation of the hashes, e.g.,  `35501f52a4652dea:8071430e01f99174e749b5787328f900ce6343c330ba607ebb4fbc5c8b15a559`, on each line.
- `wordfile`: str <br/>
The name of the `.txt` file containing the password guesses on each line. 

## Remarks
The scripts are easy to read and modify. One can easily switch the hashfunction, the salt position, add different attack types and more.

## Author

[Rustam Latypov](mailto:rustam.latypov@aalto.fi)
