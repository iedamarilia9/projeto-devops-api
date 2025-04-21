# Usa a imagem oficial do Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o diretório de trabalho
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que o app usa (ajuste conforme necessário)
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

