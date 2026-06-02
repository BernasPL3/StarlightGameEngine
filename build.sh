#!/bin/bash

echo "====================================="
echo " Statlight Game Engine Builder"
echo "====================================="

# Verifica Python
if ! command -v python3 &> /dev/null
then
    echo "Python 3 não encontrado!"
    read -p "Pressione Enter para sair..."
    exit 1
fi

# Instala PyInstaller se necessário
python3 -m pip install --upgrade pyinstaller

# Limpa builds antigos
rm -rf build
rm -rf dist
rm -rf __pycache__

# Gera o executável
pyinstaller \
    --windowed \
    --name StatlightGameEngine \
    --add-data "assets:assets" \
    main.py

BUILD_RESULT=$?

echo ""

if [ $BUILD_RESULT -eq 0 ]; then
    echo "Build concluído com sucesso!"
    echo "Arquivos gerados em:"
    echo "dist/StatlightGameEngine"
else
    echo "Erro durante o build!"
fi

echo ""
read -p "Pressione Enter para fechar..."
