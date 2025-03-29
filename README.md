# Wordle Guesser
## **NOTICE**
 - *This was made on windows using WSL Ubuntu and nix flakes*
 - *If you don't know what is a nix flake or nix refer to [this](https://nix.dev/manual/nix/2.24/introduction)*
 - *All packages for python also are managed by nix. the "reqirements.txt" is only for refference*
 - *This doesn't include a pre-packaged IDE or text editor like neovim for now.*
 - *The reason i didn't use docker is because of the rapid prototyping while being consistent and reproducible nature of nix*
 - *For now .gitignore is blank so it can be ignored*
 - *There might be a future cpp rewrite of this so i will be using as little libreries as possible*
 - *if you aren't familiar with mypy. it's just a static type checker which helps avoid runtime errors*
 - *I'm not sure what to use as the shell so ill just stick with bash but it might be migrated to nu or zsh*
 - *i know this may sound stupid but nix intergrates with git so unless a file is added by git running "nix develop" will not include the file*
 - *flake.lock stores the information for what version of what packages to use*

## quick
 - *flake.nix* contains the required configs for running everything (dev environment will be included later)
 - *.gitignore* is blank for now
 - *src/* contains the project files **(python)**
 - *src/allowed_words.txt* just has all the possible wordle combinations

## Todo
 - [X] complete single word check
    - [X] complete letter ignore
    - [X] complete letter must
    - [X] complete letter somewhere
 - [ ] add second word / 6 words
 - [ ] add checks for error correction