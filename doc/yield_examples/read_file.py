from typing import Iterator


def read_file(file_name: str) -> Iterator[str]:
    print("j'ai encore rien fait pour l'instant")

    try:
        with open(file_name, 'r') as file:
            print("j'ai bien reussi a ouvrir le fichier")
            if file:
                for line in file:
                    print(f"je viens de lire la ligne : {line}")
                    yield line
                    print("je reprend mon job et on passe a la ligne suivante")
    except FileNotFoundError as e:
        print(f"Fichier introuvable : {e}")
    except Exception as e:
        print(f"une erreur est survenu : {e}")
    else:
        print("Tout le fichier a été lu, autodesctruction du generator")


def main() -> None:
    my_file = read_file("test.txt")
    # print(my_file)

    try:
        for one_line in my_file:
            print(f"cette ligne = {one_line}")
    except Exception as e:
        print(f"Une erreur s'est produite ({e})")


if __name__ == "__main__":
    main()
