# Image-cryptography-python
Encrypting and decrypting an message


## To run virtaul environment
```
pip3 install virtualenv
```

create virtual-environment file:
```
python -m virtualenv venv 
```

to activate:
```
venv/Scripts/activate
```
to deactivate:
```
deactivate 
```
## Install dependencies:
```
pip install -r requirements.txt
```
## To run app
creating ciphered.png (encryption)
```
python app.py -vvv --message message.png --secret secret.png
```
decryption
```
python show.py ciphered.png secret.png
```
