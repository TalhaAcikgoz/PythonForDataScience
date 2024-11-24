class calculator:
    """ Representation of ft_calculator """
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        product = 0
        for i, j in zip(V1, V2):
            product += i*j
        print(f"Dot product is: {product}")

    def add_vec(V1: list[float], V2: list[float]) -> None:
        li = []
        for i, j in zip(V1, V2):
            li.append(float(i+j))
        print(f"Add Vector is : {li}")

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        li = []
        for i, j in zip(V1, V2):
            li.append(float(i-j))
        print(f"Sous Vector is: {li}")
