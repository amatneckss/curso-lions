import traceback
import ast
import re
import google.generativeai as genai

# =======================
# Módulo 0: Configuração da IA
# =======================

# ⚠️ Insira sua chave de API aqui
genai.configure(api_key="AIzaSyAHQxOFBbQjiMsmBu9kHXf2oBg-uyra45k")
model = genai.GenerativeModel("gemini-2.0-flash")

# =======================
# Módulo 1: Entrada
# =======================

def receber_pedido_usuario():
    """Função que recebe o texto do usuário."""
    return input("Digite sua dúvida ou pedido: ")

def receber_codigo_usuario():
    """Tenta ler o arquivo. Se não existir, informa o usuário."""
    try:
        with open('teste.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            return conteudo
    except FileNotFoundError:
        print("⚠️  Aviso: O arquivo 'teste.txt' não foi encontrado. Certifique-se de que ele existe e está no mesmo diretório.")
        return None

# =======================
# Módulo 2: Análise de Intenção (com LLM)
# =======================

def detectar_intencao_com_llm(texto_usuario):
    """Usa a LLM para detectar a intenção principal do usuário."""
    prompt = (
        "Analise o pedido do usuário e classifique-o em uma das seguintes categorias: "
        "'adaptar', 'refazer', 'converter', 'corrigir', 'explicar', 'melhorar', 'gerar'.\n"
        "Responda apenas com a palavra da categoria.\n\n"
        f"Pedido do usuário: \"{texto_usuario}\"\n\n"
        "Categoria:"
    )
    try:
        response = model.generate_content(prompt)
        # Limpa a resposta para garantir que apenas a palavra-chave seja retornada
        intencao = response.text.strip().lower().replace("'", "").replace(".", "")
        return intencao
    except Exception as e:
        print(f"⚠️ Erro ao detectar intenção: {e}")
        return "desconhecida"

# =======================
# Módulo 3: Análise de Emoção (com LLM)
# =======================

def detectar_emocao_com_llm(instrucao_usuario):
    """
    Usa a LLM para avaliar o Esforço de Compreensão (ECU) e a Carga Emocional (CED).
    """
    prompt = (
        f"Analise o texto do usuário para estimar dois fatores:\n"
        f"1.  **ECU (Esforço de Compreensão pelo Usuário)**: Um score de 0.1 a 1.0. Um valor alto (próximo a 1.0) significa que o usuário é iniciante, está com dificuldade ou precisa de uma explicação muito simples.\n"
        f"2.  **CED (Carga Emocional Demonstrada)**: Um score de 0.1 a 1.0. Um valor alto (próximo a 1.0) indica que o usuário parece cansado, apressado ou frustrado.\n\n"
        f"Texto do usuário: \"{instrucao_usuario}\"\n\n"
        f"Responda apenas com os scores no formato 'ECU: [valor], CED: [valor]'. Por exemplo: 'ECU: 0.8, CED: 0.9'."
    )
    try:
        response = model.generate_content(prompt)
        texto_resposta = response.text.strip()
        
        match_ecu = re.search(r'ECU:\s*([0-9.]+)', texto_resposta, re.IGNORECASE)
        match_ced = re.search(r'CED:\s*([0-9.]+)', texto_resposta, re.IGNORECASE)
        
        ecu = float(match_ecu.group(1)) if match_ecu else 0.5
        ced = float(match_ced.group(1)) if match_ced else 0.3
        
        return ecu, ced
    except Exception as e:
        print(f"⚠️ Erro ao detectar emoção: {e}. Usando valores padrão.")
        return 0.5, 0.3

# =======================
# Módulo 4: Processamento Técnico (com LLM)
# =======================

def gerar_codigo(instrucoes_usuario):
    prompt = (
        "Você é um assistente de programação especializado em geração de algoritmos.\n"
        "Gere o algoritmo de acordo com as instruções fornecidas.\n"
        "Caso a linguagem de programação não seja fornecida, gere em Python.\n"
        "Responda apenas com o código gerado, dentro de um bloco de código Markdown.\n\n"
        f"Instruções fornecidas:\n{instrucoes_usuario.strip()}\n\n"
        "Código gerado:"
    )
    response = model.generate_content(prompt)
    return response.text.strip()

def corrigir_codigo(algoritmo, texto_problema):
    prompt = (
        "Você é um especialista em depuração de código. Analise o código e a descrição do problema. "
        "Corrija o erro e retorne apenas o código corrigido, dentro de um bloco de código Markdown e sem explicações adicionais.\n\n"
        f"Descrição do problema: {texto_problema}\n\n"
        f"Código com erro:\n{algoritmo}\n\n"
        "Código corrigido:"
    )
    response = model.generate_content(prompt)
    return response.text.strip()

def explicar_codigo(algoritmo):
    prompt = (
        "Você é um professor de programação. Analise o código a seguir e explique, de forma clara e didática, o que ele faz, "
        "passo a passo. Se o código for complexo, divida a explicação em partes (funções, loops, condicionais).\n\n"
        f"Código para explicar:\n{algoritmo}\n\n"
        "Explicação:"
    )
    response = model.generate_content(prompt)
    return response.text.strip()

def converter_codigo(algoritmo, instrucoes):
    """Usa a LLM para converter o código para outra linguagem."""
    prompt = (
        "Você é um especialista em conversão de linguagens de programação.\n"
        "Analise o código fonte e as instruções para convertê-lo para a linguagem de destino.\n"
        "Retorne apenas o código convertido, dentro de um bloco de código Markdown e sem explicações adicionais.\n\n"
        f"Instruções (indicando a linguagem de destino): {instrucoes}\n\n"
        f"Código para converter:\n{algoritmo}\n\n"
        "Código convertido:"
    )
    response = model.generate_content(prompt)
    return response.text.strip()

def adaptar_codigo(algoritmo, instrucoes):
    """Usa a LLM para adaptar o código a um novo requisito ou contexto."""
    prompt = (
        "Você é um programador sênior especializado em adaptar códigos existentes.\n"
        "Analise o código fonte e as instruções para adaptá-lo a um novo requisito, contexto ou funcionalidade.\n"
        "Retorne apenas o código adaptado, dentro de um bloco de código Markdown e sem explicações adicionais.\n\n"
        f"Instruções para a adaptação: {instrucoes}\n\n"
        f"Código original:\n{algoritmo}\n\n"
        "Código adaptado:"
    )
    response = model.generate_content(prompt)
    return response.text.strip()

def refazer_codigo(algoritmo, instrucoes):
    """Usa a LLM para refazer o código, possivelmente com uma nova abordagem."""
    prompt = (
        "Você é um arquiteto de software que irá refazer o código a seguir.\n"
        "Reimplemente o código com base nas instruções, que podem sugerir uma nova lógica, estrutura ou abordagem, mantendo o objetivo final do algoritmo.\n"
        "Retorne apenas o novo código, dentro de um bloco de código Markdown e sem explicações adicionais.\n\n"
        f"Instruções para refazer o código: {instrucoes}\n\n"
        f"Código original:\n{algoritmo}\n\n"
        "Código refeito:"
    )
    response = model.generate_content(prompt)
    return response.text.strip()

def melhorar_codigo(algoritmo, instrucoes):
    """Usa a LLM para melhorar o código (eficiência, clareza, etc.)."""
    prompt = (
        "Você é um especialista em otimização e boas práticas de programação.\n"
        "Analise o código a seguir e melhore-o. O objetivo pode ser aumentar a eficiência, a legibilidade, seguir as convenções de estilo ou reduzir a complexidade. As instruções do usuário podem dar uma dica do que focar.\n"
        "Retorne apenas o código melhorado, dentro de um bloco de código Markdown e sem explicações adicionais.\n\n"
        f"Instruções ou foco da melhoria: {instrucoes}\n\n"
        f"Código original:\n{algoritmo}\n\n"
        "Código melhorado:"
    )
    response = model.generate_content(prompt)
    return response.text.strip()

def processar_codigo(texto, intencao, algoritmo):
    """Direciona a tarefa para a função correta com base na intenção."""
    if intencao == "gerar":
        return gerar_codigo(texto)
    elif intencao == "corrigir" and algoritmo:
        return corrigir_codigo(algoritmo, texto)
    elif intencao == "explicar" and algoritmo:
        return explicar_codigo(algoritmo)
    elif intencao == "converter" and algoritmo:
        return converter_codigo(algoritmo, texto)
    elif intencao == "adaptar" and algoritmo:
        return adaptar_codigo(algoritmo, texto)
    elif intencao == "refazer" and algoritmo:
        return refazer_codigo(algoritmo, texto)
    elif intencao == "melhorar" and algoritmo:
        return melhorar_codigo(algoritmo, texto)
    elif not algoritmo and intencao in ["corrigir", "explicar", "adaptar", "refazer", "melhorar", "converter"]:
        return "Para essa intenção, preciso que você forneça um código no arquivo 'teste.txt'."
    else:
        return "Não consegui entender seu pedido ou a intenção não corresponde a uma ação válida."

# =======================
# Módulo 5: Utilidade (com LLM no Feedback)
# =======================

def ajustar_pesos(ecu, ced):
    """Ajusta os pesos da fórmula de utilidade com base nos fatores emocionais."""
    if ecu > 0.7:
        w1, w2 = 0.4, 0.5
    else:
        w1, w2 = 0.6, 0.3
    
    w3 = 0.4 if ced > 0.6 else 0.2
    return w1, w2, w3

def avaliar_feedback_com_llm(feedback_usuario):
    """Usa a LLM para interpretar o feedback do usuário e retornar um score QTS."""
    prompt = (
        f"Analise o feedback do usuário sobre uma solução de código. Com base no texto, "
        f"determine a Qualidade Técnica da Solução (QTS) percebida por ele e retorne um único número decimal entre 0.0 (muito ruim) e 1.0 (perfeito).\n"
        f"Exemplos:\n"
        f"- 'não funcionou de jeito nenhum, deu outro erro': 0.1\n"
        f"- 'confuso, não ajudou muito': 0.3\n"
        f"- 'ok, mas tive que ajustar': 0.6\n"
        f"- 'perfeito, era exatamente isso, obrigado!': 1.0\n\n"
        f"Feedback do usuário: \"{feedback_usuario}\"\n\n"
        f"Score QTS:"
    )
    try:
        response = model.generate_content(prompt)
        return float(response.text.strip())
    except (ValueError, TypeError):
        print("⚠️ Não foi possível converter o score do feedback. Usando valor neutro.")
        return 0.5

def calcular_utilidade(qts, ecu, ced, w1, w2, w3):
    """
    Calcula a utilidade final da interação.
    U(P) = (QTS * w1) + (1/ECU * w2) - (CED * w3)
    """
    utilidade = (qts * w1) + ((1 / max(ecu, 0.01)) * w2) - (ced * w3)
    return round(utilidade, 3)

# =======================
# Módulo Principal
# =======================

def code_facilitator():
    """Ciclo principal de execução do agente."""
    algoritmo = ""
    texto_usuario = receber_pedido_usuario()
    
    intencao = detectar_intencao_com_llm(texto_usuario)
    print(f"🤖 Intenção detectada: {intencao}")
    
    if intencao in ["corrigir", "adaptar", "converter", "explicar", "melhorar", "refazer"]:
        algoritmo = receber_codigo_usuario()
        if algoritmo is None:
            return 

    ecu, ced = detectar_emocao_com_llm(texto_usuario)
    
    resposta_tecnica = processar_codigo(texto_usuario, intencao, algoritmo)
    if intencao == "explicar":
        print(f"\n---\nResposta:\n{resposta_tecnica}\n---\n")
    else:
        escrever_arquivo(resposta_tecnica)
    
    print(f"\n---\nResposta (também salva em teste.txt):\n{resposta_tecnica}\n---\n")

    feedback_usuario = input("\n🗣️  A resposta foi útil? (ex: 'sim, funcionou', 'não ajudou', 'confuso', etc.): ")
    qts = avaliar_feedback_com_llm(feedback_usuario)

    w1, w2, w3 = ajustar_pesos(ecu, ced)
    utilidade = calcular_utilidade(qts, ecu, ced, w1, w2, w3)

    print(f"\n📊 Utilidade estimada da interação: {utilidade}")
    print(f"(Pesos aplicados: w1={w1}, w2={w2}, w3={w3} | Scores: QTS={qts:.2f}, ECU={ecu:.2f}, CED={ced:.2f})")


def escrever_arquivo(codigo):
    if not isinstance(codigo, str):
        codigo = str(codigo)
        
    if codigo.startswith("```python"):
        codigo = codigo[len("```python"):].lstrip()
    if codigo.startswith("```"):
        codigo = codigo[3:].lstrip()
    if codigo.endswith("```"):
        codigo = codigo[:-3].rstrip()
        
    with open('teste.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(codigo)

# Execução do programa
if __name__ == "__main__":
    while True:
        try:
            code_facilitator()
            continuar = input("\n🔁 Deseja fazer outro pedido? (s/n): ").strip().lower()
            if continuar in ["n", "nao", "não", "exit", "sair"]:
                print("👋 Encerrando o Code Facilitator. Até a próxima!")
                break
        except KeyboardInterrupt:
            print("\n⛔ Interrompido pelo usuário. Encerrando...")
            break
        except Exception as e:
            print(f"⚠️ Ocorreu um erro inesperado: {e}")
            print(traceback.format_exc())