def gerar_proximo_id(livros):
    if not livros:
        return 1

    maior_id = max(livro["id"] for livro in livros)
    return maior_id + 1


def normalizar_categoria(categoria):
    categoria = categoria.strip().upper()

    if len(categoria) >= 3:
        return categoria[:3]

    return categoria


def gerar_etiqueta(categoria, estante, prateleira, livro_id):
    categoria_codigo = normalizar_categoria(categoria)
    estante = estante.strip().upper()
    prateleira = int(prateleira)

    return f"{categoria_codigo}-{estante}-{prateleira:02d}-{livro_id:04d}"


def livro_existe(livros, titulo, autor):
    titulo = titulo.strip().lower()
    autor = autor.strip().lower()

    for livro in livros:
        mesmo_titulo = livro["titulo"].strip().lower() == titulo
        mesmo_autor = livro["autor"].strip().lower() == autor

        if mesmo_titulo and mesmo_autor:
            return True

    return False


def cadastrar_livro(
    dados,
    titulo,
    autor,
    categoria,
    quantidade,
    estante,
    prateleira,
    isbn=""
):
    titulo = titulo.strip()
    autor = autor.strip()
    categoria = categoria.strip()
    estante = estante.strip().upper()
    isbn = isbn.strip()

    if not titulo:
        return False, "Título é obrigatório."

    if not autor:
        return False, "Autor é obrigatório."

    if not categoria:
        return False, "Categoria é obrigatória."

    if not estante:
        return False, "Estante é obrigatória."

    try:
        quantidade = int(quantidade)
    except ValueError:
        return False, "Quantidade deve ser um número inteiro."

    if quantidade <= 0:
        return False, "Quantidade deve ser maior que zero."

    try:
        prateleira = int(prateleira)
    except ValueError:
        return False, "Prateleira deve ser um número inteiro."

    if prateleira < 1 or prateleira > 5:
        return False, "Prateleira deve estar entre 1 e 5."

    livros = dados["livros"]

    if livro_existe(livros, titulo, autor):
        return False, "Livro já cadastrado com esse título e autor."

    livro_id = gerar_proximo_id(livros)

    etiqueta = gerar_etiqueta(
        categoria=categoria,
        estante=estante,
        prateleira=prateleira,
        livro_id=livro_id
    )

    novo_livro = {
        "id": livro_id,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "isbn": isbn,
        "estante": estante,
        "prateleira": prateleira,
        "quantidade_total": quantidade,
        "quantidade_disponivel": quantidade,
        "etiqueta": etiqueta
    }

    livros.append(novo_livro)

    return True, novo_livro


def listar_livros(dados):
    return dados["livros"]


def buscar_livro_por_id(dados, livro_id):
    for livro in dados["livros"]:
        if livro["id"] == livro_id:
            return livro

    return None


def buscar_livros_por_titulo(dados, titulo):
    titulo = titulo.strip().lower()

    encontrados = []

    for livro in dados["livros"]:
        if titulo in livro["titulo"].lower():
            encontrados.append(livro)

    return encontrados