# Password cracker 

Developed during October, 2019.

## Description

A simple command-line interface for cracking passwords in parallel on the CPU. It is set up to crack SHA256  passwords appended with salt using dictionary and hybrid attacks, but can be modified with minimal effort. One can easily change the hash function, the salt position, modify attacks and write new ones.

If any passwords are found, they are printed along with the corresponding hash and salt, e.g., `040904iloveth33:35501f52a4652dea:3e345983dd3a04d16301d78558b406c1bf03c1e413404ac254e10ef9a9db0235`.


## Running

Built with Python 3.7.2 using

```
• argparse
• hashlib
• tqdm
• joblib
```

In `/scripts` run `python3 main.py <attacktype> <hashfile> <wordfile>`. <br/>

- `attacktype` <br/>
The attack type used, choices: `d:dictionary`, `h:hybrid`.
- `hashfile` <br/>
The name of the .txt file in `/res` containing the hexadecimal representation of the hashes and the salts, e.g.,  `3e345983dd3a04d16301d78558b406c1bf03c1e413404ac254e10ef9a9db0235:35501f52a4652dea`, on each line.
- `wordfile` <br/>
The name of the .txt file in `/res` containing the password guesses on each line. 


## Parallelism
Both sequential and parallel implementations are provided. Parallelism on the CPU is achieved using joblib. Using the parallel implementation makes sense when there is a lot of hashes to crack, otherwise the parallel overhead gets too high. Also, when handling large wordlists (~50M) the parallel implementations slows down and would require a better memory access pattern to work effectively.


## Author

[Rustam Latypov](mailto:rustam.latypov@aalto.fi)
