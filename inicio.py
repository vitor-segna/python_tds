from datetime import datetime
ano_atual = datetime.now().year
clube = "SPFC"
campeonato_mundial = 3
ano_fundacao = 1930
print(f"{clube} possui {campeonato_mundial} títulos mundiais.")
print(f"São {ano_atual - ano_fundacao} anos de existência.") 


escola = 'Senai'
curso = 'Técnico em Desenvolvimento de Sistemas'
uc = 'Lógica de Programação e Algoritmos'
print(
    f"Escola: {escola}\n"
    f"Curso: {curso}\n"
    f"Unidade Curricular: {uc}"
)


print(f"Matrícula do Junior é {25:06d}.")
print(f"Matrícula da Alice é {14785:07d}.")
print(f"Matrícula do José é {100258:08d}.")


print(f"Valor de pi é {3.14159265352384626433}.")
print(f"Valor de pi é {3.14159265352384626433:.20f}.")