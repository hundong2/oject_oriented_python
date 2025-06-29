# oject_oriented_python
python study project 

## uv install 

```
curl -LsSf https://astral.sh/uv/install.sh | sh


source $HOME/.local/bin/env (sh, bash, zsh)
source $HOME/.local/bin/env.fish (fish)
```

## uv execute venv environment 

```sh
uv venv .venv
uv venv -p 3.13 #setting python version 
```

## uv pip install

```sh
uv pip install pytests
```

## requirement.txt

```sh
pip freeze > requirements.txt
```

```sh
pip freeze | xargs pip uninstall -y
pip freeze > unins && pip uninstall -y -r unins && del unins
```