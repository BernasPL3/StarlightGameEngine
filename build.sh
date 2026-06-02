#!/bin/bash

set -e

echo "===================================="
echo " Statlight Game Engine - macOS Build"
echo "===================================="

# Verifica Python
if ! command -v python3 >/dev/null 2>&1; then
    echo "Erro: Python 3 não encontrado."
    exit 1
fi

echo "Instalando dependências..."
python3 -m pip install --upgrade pip
python3 -m pip install pyinstaller

echo "Limpando builds antigos..."
rm -rf build dist *.spec

echo "Gerando .app..."

if [ -f "assets/icon.icns" ]; then
    pyinstaller \
        --windowed \
        --onedir \
        --name "StatlightGameEngine" \
        --icon "assets/icon.icns" \
        main.py
else
    pyinstaller \
        --windowed \
        --onedir \
        --name "StatlightGameEngine" \
        main.py
fi

echo ""
echo "✅ Build concluído!"
echo "Aplicativo criado em:"
echo "dist/StatlightGameEngine.app"
echo ""

read -p "Pressione Enter para sair..."
