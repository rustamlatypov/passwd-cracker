# Password cracker 

Developed during October, 2019.

## Description

A command-line tool for cracking passwords in parallel on CPU. It is set up to crack SHA256 passwords appended with salt using dictionary and hybrid attacks. The code can be modified with minimal effort. One can easily change the hash function, the salt position, modify attacks and write new ones.

If any passwords are found, they are printed along with the corresponding hash and salt, e.g., `GlumifloraE1:50634e432b26e49e8146fb1d83f3e6918e42e2fecb1024238f2ad9cd0da0cd33:732271f0d8517cf2`.


## Running

Built with Python 3.7.2.

In `/scripts` run `python3 main.py <attacktype> <hashfile> <wordfile>`. <br/>

- `attacktype` <br/>
The attack type used, choices: `d:dictionary`, `h:hybrid`.
- `hashfile` <br/>
The name of the .txt file in `/res` containing the hashes as a hexadecimal number and the salts, e.g.,  `50634e432b26e49e8146fb1d83f3e6918e42e2fecb1024238f2ad9cd0da0cd33:732271f0d8517cf2`, on each line.
- `wordfile` <br/>
The name of the .txt file in `/res` containing the password guesses on each line. 


## Parallelism
Both sequential and parallel implementations are provided. Parallelism on the CPU is achieved using `joblib`. Using the parallel implementation makes sense when there is a lot of hashes to crack, otherwise the parallel overhead gets too high. Also, when handling large wordlists (~50M) the parallel implementations slows down and would require a better memory access pattern to work effectively.


## Author

[Rustam Latypov](mailto:rustam.latypov@aalto.fi)
