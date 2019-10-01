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

- `attacktype` <br/>
- `hashfile` <br/>
- `wordfile` <br/>

## Remarks
The scripts are easy to read and modify. One can easily switch the hashfunction, the salt position, add different attack types and more.

## Author

[Rustam Latypov](mailto:rustam.latypov@aalto.fi)
