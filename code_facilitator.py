import traceback
import autopep8
import ast
from difflib import unified_diff
import google.generativeai as genai

genai.configure(api_key="AIzaSyAWJHRUDNo2jqlmSJgKAKq7hOc3c1OHpRA")
# =======================
# Módulo 1: Entrada
# =======================
def receber_pedido_usuario():
    # Função que recebe o texto do usuário
    return input("Digite sua dúvida: ")

def receber_codigo_usuario():
    # Função que recebe o texto do usuário
    return input("Digite seu algoritmo: ")

# =======================
# Módulo 2: Análise de Intenção
# =======================
def detectar_intencao(texto):
    texto = texto.lower()  # Deixa tudo minúsculo para facilitar comparação
    if "erro" in texto or "bug" in texto or "errado" in texto
        return "corrigir"
    elif "refaça com" in texto or "adapte para" in texto
        return "adaptar"
    elif "refaça" in texto or "refazer" in texto or "gere novamente" in texto
        return "refazer"
    elif "converta" in texto or "converter para" in texto or "traduza para" in texto
        return "converter"
    elif "explique" in texto or "o que" in texto
        return "explicar"
    elif "melhore" in texto or "melhorar" in texto
        return "melhorar"
    elif "gere" in texto or "faça" in texto
        return "gerar"
    

# =======================
# Módulo 3: Análise de Emoção
# =======================
def detectar_emocao(instrucao_usuario):
    texto = instrucao_usuario.lower()
    sinais_cansaco = ["cansado", "exausto", "mentalmente", "sem cabeça", "com sono"]
    sinais_urgencia = ["urgente", "agora", "correndo", "sem tempo", "última hora"]
    iniciante = ["iniciante", "comecei", "sou novo", "não sei programar"]

    ced = 1.0 if any(p in texto for p in sinais_cansaco + sinais_urgencia) else 0.3
    ecu = 1.0 if any(p in texto for p in iniciante + sinais_cansaco) else 0.5
    return ecu, ced


# =======================
# Módulo 4: Processamento Técnico
# =======================

def adaptar_codigo(codigo_original, instrucoes):
    model = genai.GenerativeModel("gemini-1.5-pro")

    prompt = (
        "Você é um assistente de programação inteligente. Seu trabalho é adaptar o código "
        "fornecido de acordo com as instruções a seguir. Responda apenas com o código final, "
        "sem explicações ou comentários.\n\n"
        f"Código Original:\n{codigo_original.strip()}\n\n"
        f"Instruções:\n{instrucoes.strip()}\n\n"
        "Código Adaptado:"
    )

    response = model.generate_content(prompt)
    return response.text.strip()

def refazer_codigo(codigo_original):
    model = genai.GenerativeModel("gemini-1.5-pro")

    prompt = (
        "Você é um assistente de programação. Reescreva o seguinte código mantendo exatamente a mesma lógica, "
        "mas utilizando uma estrutura diferente. Pode trocar comandos, estruturas de repetição ou organização geral, "
        "desde que o comportamento do algoritmo permaneça o mesmo.\n\n"
        f"Código original:\n{codigo_original.strip()}\n\n"
        "Código refeito:"
    )

    response = model.generate_content(prompt)
    return response.text.strip()

def converter_codigo(codigo_original, instrucoes):
    model = genai.GenerativeModel("gemini-1.5-pro")

    prompt = (
        "Você é um assistente de programação. Sua tarefa é converter o código fornecido "
        "para outra linguagem especificado pelo usuário.\n\n"
        " -Identifique automaticamente a linguagem do código original.\n"
        " -Converta para a linguagem de destino especificada.\n"
        " -Mantenha a mesma lógica e comportamento do código.\n"
        " -Responda apenas com o código convertido, sem explicações ou comentários.\n\n"
        f"🧾 Código original:\n{codigo_original.strip()}\n\n"
        f"🎯 Instrução do usuário:\n{instrucao_usuario.strip()}\n\n"
        "💡 Código convertido:"
    )

    response = model.generate_content(prompt)
    return response.text.strip()

def melhorar_codigo(codigo_original):
    model = genai.GenerativeModel("gemini-1.5-pro")

    prompt = (
        "Você é um assistente de programação especializado em otimização de código.\n\n"
        "Identifique a linguagem de programação usada e reescreva o seguinte código de forma que ele mantenha exatamente a mesma lógica, "
        "mas com uma ou mais das seguintes melhorias:\n"
        "- Menor tempo de execução (melhor desempenho)\n"
        "- Menor uso de memória\n"
        "- Menor quantidade de linhas (mais conciso)\n\n"
        "Não altere a lógica do que o código faz.\n"
        "Responda apenas com o código melhorado, sem explicações.\n\n"
        f"Código Original:\n{codigo_original.strip()}\n\n"
        "Código Melhorado:"
    )

    response = model.generate_content(prompt)
    return response.text.strip()

def gerar_codigo(instrucoes_usuario):
    model = genai.GenerativeModel("gemini-1.5-pro")

    prompt = (
        "Você é um assistente de programação especializado em geração de algoritmo.\n\n"
        "Gere o algoritmo de acordo com as instruções fornecidas"
        "Caso a linguagem de programação não for fornecida, gerar em Python"
        "Responda apenas com o código gerado"
        f"Instruções fornecidas:\n{instrucoes_usuario.strip()}\n\n"
        "Código gerado:"
    )

def processar_codigo(texto, intencao, algoritmo):
    if intencao == "corrigir":#Correção
        codigo_atual = algoritmo
        max_tentativas = 3
        tentativas = 0

        while tentativas < max_tentativas:
            try:
                exec(codigo_atual, {}, {})
                return (
                    True
                )
            except Exception as e:
                tentativas += 1
                codigo_atual = autopep8.fix_code(codigo_atual)
                if tentativas == max_tentativas
                    max_tentativas += 1
    

    elif intencao == "explicar":#Explicação
        try:
            arvore = ast.parse(codigo_atual)
        except Exception as e:
            return f"❌ Não foi possível analisar o código. Erro de sintaxe: {e}"

        explicacoes = []

        for node in arvore.body:
            if isinstance(node, ast.FunctionDef):
                explicacoes.append(f"🧩 A função `{node.name}` é definida com os parâmetros: {', '.join(arg.arg for arg in node.args.args)}.")

            elif isinstance(node, ast.For):
                target = ast.unparse(node.target)
                iter_ = ast.unparse(node.iter)
                explicacoes.append(f"🔁 Um loop `for` que percorre `{iter_}`, atribuindo cada valor a `{target}`.")

            elif isinstance(node, ast.If):
                cond = ast.unparse(node.test)
                explicacoes.append(f"🔎 Uma estrutura `if` que verifica se `{cond}` é verdadeiro.")

            elif isinstance(node, ast.Assign):
                targets = ', '.join(ast.unparse(t) for t in node.targets)
                value = ast.unparse(node.value)
                explicacoes.append(f"📌 Atribuição: `{targets}` recebe `{value}`.")

            elif isinstance(node, ast.Expr):
                if isinstance(node.value, ast.Call):
                    call_repr = ast.unparse(node)
                    explicacoes.append(f"⚙️ Chamada de função: `{call_repr}`.")
            
            elif isinstance(node, ast.While):
                condicao = ast.unparse(node.test)
                explicacoes.append(f"🔁 Um loop `while` que repete enquanto `{condicao}` for verdadeiro.")

            elif isinstance(node, ast.Return):
                if node.value is not None:
                    valor = ast.unparse(node.value)
                    explicacoes.append(f"🔙 O comando `return` devolve o valor `{valor}` para quem chamou a função.")
                else:
                    explicacoes.append("🔙 O comando `return` devolve `None` (nenhum valor).")
            # outros tipos podem ser adicionados aqui (while, return, etc.)
            return "\n".join(explicacoes)
    elif intencao == "adaptar":
        codigo_original = algoritmo  # essa variável vem da função que recebe o código
        instrucoes = texto    # essa variável vem da função que recebe as instruções
        codigo_adaptado = adaptar_codigo(codigo_original, instrucoes)
        return codigo_adaptado
    elif intencao == "refazer":
        codigo_original = algoritmo
        instrucoes = texto
        codigo_refeito = refazer_codigo(codigo_original, texto)
        return codigo_refeito
    elif intencao == "melhorar":
        codigo_original = algoritmo
        codigo_melhorado = melhorar_codigo(codigo_original)
        return codigo_melhorado
    elif intencao == "gerar":
        instrucoes = texto
        codigo_gerado = gerar_codigo(instrucoes)
        return codigo_gerado

# =======================
# Módulo 5: Utilidade
# =======================
def ajustar_pesos(ecu, ced):
    if ecu > 0.7:
        w1 = 0.4
        w2 = 0.5
    else:
        w1 = 0.6
        w2 = 0.3
    w3 = 0.4 if ced > 0.6 else 0.2
    return w1, w2, w3

def avaliar_feedback(feedback_usuario):
    positivo = ["funcionou", "perfeito", "era isso", "ótimo", "ok", "deu certo"]
    negativo = ["não ajudou", "não entendi", "confuso", "erro", "não foi isso", "outra", "fraco"]

    texto = feedback_usuario.lower()
    qts = 0.9 if any(p in texto for p in positivo) else 0.4
    return qts

def calcular_utilidade(qts, ecu, ced, w1, w2, w3):
    utilidade = (qts * w1) + ((1 / max(ecu, 0.01)) * w2) - (ced * w3)
    return round(utilidade, 3)

    

# =======================
# Módulo 6: Geração da Resposta
# =======================
def explicacoes_codigo_gerado(respostaIA_gerada):
    model = genai.GenerativeModel("gemini-1.5-pro")

    prompt = (
        "Você é um assistente de programação inteligente. Seu trabalho é dar uma pequena explicação ao usuário o que o código gerado faz.\n\n"
        f"Código Rerado:\n{respostaIA_gerada.strip()}\n\n"
    )

    response = model.generate_content(prompt)
    return response.text.strip()

def gerar_resposta(respostaIA_gerada, utilidade, cansaco):
    if cansaco > 0.3:
        print(f"\nAqui está o pedido solicitado:\n{respostaIA_gerada}")
    else:
        print(f"\nResposta final gerada:\n{explicacoes_codigo_gerado(respostaIA_gerada)}")
    

# =======================
# Módulo Principal
# =======================
def code_facilitator():
    # Entrada do usuário
    texto = receber_pedido_usuario()
    algoritmo = receber_codigo_usuario()

    # Análise de intenção e emoção
    intencao = detectar_intencao(texto)
    ecu, ced = detectar_emocao(texto)

    # Processamento da tarefa técnica
    resposta_tecnica = processar_codigo(texto, intencao, algoritmo)

    # Feedback do usuário
    #feedback_usuario = input("\n🗣️ Qual seu feedback sobre a resposta? (ex: funcionou, não entendi, etc.): ")
    #qts = avaliar_feedback(feedback_usuario)

    # Ajuste dinâmico dos pesos com base nas emoções
    w1, w2, w3 = ajustar_pesos(ecu, ced)

    # Cálculo da utilidade final
    #utilidade = calcular_utilidade(qts, ecu, ced, w1, w2, w3)

    # Geração e exibição da resposta final
    gerar_resposta(resposta_tecnica, utilidade, ced)

    #print(f"\n📊 Utilidade estimada da resposta: {utilidade}")


# Executar o agente
if __name__ == "__main__":
    code_facilitator()
