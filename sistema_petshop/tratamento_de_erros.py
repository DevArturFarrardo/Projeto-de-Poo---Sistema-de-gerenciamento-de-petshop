def ler_str(prompt: str, *, allow_blank: bool = False, default=None) -> str:
    while True:
        entrada = input(prompt).strip()
        if entrada == "" and not allow_blank:
            print("⚠️ Este campo não pode ficar em branco.")
            continue
        return entrada or default

def ler_int(prompt: str, *, allow_blank: bool = False, default=None) -> int:
    while True:
        entrada = input(prompt).strip()
        if entrada == "" and allow_blank:
            return default
        try:
            return int(entrada)
        except ValueError:
            print("⚠️ Por favor, informe um número inteiro válido.")

def ler_float(prompt: str, *, allow_blank: bool = False, default=None) -> float:
    while True:
        entrada = input(prompt).strip()
        if entrada == "" and allow_blank:
            return default
        try:
            return float(entrada)
        except ValueError:
            print("⚠️ Por favor, informe um número válido (use ponto).")
