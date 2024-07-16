## ROMs Organizer

I love retro games and playing the games I used to play in my childhood, mainly PlayStation 1 games. Sometimes, I want to test games from other systems that I never experienced personally, so I have a huge collection of retro games on my hard drive. For those who like to download packs of retro games from the internet, you know that the files always come unorganized, with ROMs compressed or with additional files that you need to organize manually. So, I decided to make a little Python program to automate this process.

This Python program uses some libraries to organize a directory of ROM games. You just need to start the program and specify the directory of your games, like this: "C:/retro/playstation." The script will go to this directory and organize all your ROMs, creating folders for each game and extracting those that are compressed.

This program still does not work exactly as I want, but it already helps in some cases. In the future, this program will be able to receive a master directory of retro games, follow the many directories inside, and organize all of them in a recursive way. Additionally, a feature to analyze a ROM and put it in the correct system folder by analyzing the extension type will be implemented, since some ROMs have exclusive system extension types.

## Organizador de ROMs

Eu amo jogos retrô e jogar os jogos que eu costumava jogar na minha infância, principalmente jogos de PlayStation 1. Às vezes, quero testar jogos de outros sistemas que nunca experimentei pessoalmente, então tenho uma enorme coleção de jogos retrô no meu HD. Para aqueles que gostam de baixar pacotes de jogos retrô da internet, sabem que os arquivos sempre vêm desorganizados, com ROMs compactadas ou com arquivos adicionais que você precisa organizar manualmente. Então, decidi fazer um pequeno programa em Python para automatizar esse processo.

Este programa em Python usa algumas bibliotecas para organizar um diretório de jogos ROM. Você só precisa iniciar o programa e especificar o diretório dos seus jogos, assim: "C:/retro/playstation." O script irá para este diretório e organizará todas as suas ROMs, criando pastas para cada jogo e extraindo aquelas que estão compactadas.
Este programa ainda não funciona exatamente como eu quero, mas já ajuda em alguns casos. 

No futuro, este programa poderá receber um diretório principal de jogos retrô, seguir os muitos diretórios internos e organizar todos eles de maneira recursiva. Além disso, uma funcionalidade para analisar uma ROM e colocá-la na pasta do sistema correto, analisando o tipo de extensão, será implementada, já que algumas ROMs têm tipos de extensão exclusivos para determinados sistemas.

## Requirements

1. Clone this repository:

    ```sh
    git clone <repository-url>
    ```

2. Install the necessary dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Run the script:

    ```sh
    python main.py
    ```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or additions.

## Future Improvements
- Support for recursive directory organization.
- Automatic detection and categorization of ROMs based on file extensions.



