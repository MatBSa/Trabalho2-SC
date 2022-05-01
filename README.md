## Como executar o código

Para rodar o programa para cifrar a mensagem basta dar o seguinte comando caso não tenha/queira usar uma chave prévia:
```
python src/main.py io/msg.txt -o io/cifra.txt
```
Para rodar o programa para decifrar a mensagem basta dar o comando abaixo substituindo "n" pelo número da chave que gerou a mensagem cifrada:
```
python src/main.py io/cifra.txt -k keys/key_sample.pub -s keys/session_sample.pub -o io/out.txt -d
```