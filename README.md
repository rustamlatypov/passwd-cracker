# Password cracker 

Developed during October, 2019.

## Description

A simple command-line interface for cracking passwords in parallel on the CPU. It is set up to crack SHA256  passwords appended with salt using dictionary and hybrid attacks, but can be modified with minimal effort. One can easily change the hash function, the salt position, modify attacks and write new ones.

If any passwords are found, they are printed along with the corresponding hash and salt, e.g., `lovemeorhateme:c1bc4ba2b8bfd40f753950d2fe7eccdb9ccc9bdf9940e2b5c5cc8492dd3a3023:c4fb88d80d448d9a`.


## Running

Built with Python 3.7.2 using

```
• argparse
• hashlib
• tqdm 4.36.1
• joblib 0.13.2
```

In `/scripts` run `python3 main.py <attacktype> <hashfile> <wordfile>`. <br/>

- `attacktype` <br/>
The attack type used, choices: `d:dictionary`, `h:hybrid`.
- `hashfile` <br/>
The name of the .txt file in `/res` containing the hashes as a hexadecimal number and the salts, e.g.,  `c1bc4ba2b8bfd40f753950d2fe7eccdb9ccc9bdf9940e2b5c5cc8492dd3a3023:c4fb88d80d448d9a`, on each line.
- `wordfile` <br/>
The name of the .txt file in `/res` containing the password guesses on each line. 


## Parallelism
Both sequential and parallel implementations are provided. Parallelism on the CPU is achieved using joblib. Using the parallel implementation makes sense when there is a lot of hashes to crack, otherwise the parallel overhead gets too high. Also, when handling large wordlists (~50M) the parallel implementations slows down and would require a better memory access pattern to work effectively.


## Author

[Rustam Latypov](mailto:rustam.latypov@aalto.fi)
