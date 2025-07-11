# desafio-criando-um-validador-de-cartao

## 🧠 Validador de Bandeiras de Cartão de Crédito com Python

Este projeto implementa um **validador de bandeiras de cartões de crédito** usando Python, combinando:

- 🔍 **Expressões Regulares (Regex)** para identificar a bandeira pelo prefixo e comprimento.
- ✅ **Algoritmo de Luhn** para validar se o número do cartão é matematicamente válido.
- 💬 **Entrada interativa** via `input()` para o usuário digitar o número do cartão.

---

### 🚀 Como Funciona

1. O número do cartão é recebido do usuário, e espaços ou traços são removidos.
2. O número é testado com o **algoritmo de Luhn**, que verifica se ele é matematicamente válido.
3. Caso passe no Luhn, o número é comparado com **padrões de Regex** que identificam as principais bandeiras:
   - Visa
   - MasterCard
   - American Express
   - Diners Club
   - Discover
   - enRoute
   - JCB
   - Voyager
   - Hipercard (com prefixo atualizado: `606282`)
   - Aura

4. O programa imprime o nome da bandeira correspondente, ou uma mensagem informando se o cartão é inválido ou não reconhecido.

---

### 📄 Exemplo de Uso

```bash
Digite o número do cartão de crédito: 4111 1111 1111 1111
Bandeira: Visa



🛠️ Tecnologias Usadas
Python 3

Biblioteca re (expressões regulares)

Algoritmo de Luhn (implementado manualmente)

🧪 Observações
Os números usados para teste são fictícios e gerados para fins educacionais.

O código pode ser expandido com interface gráfica (Tkinter) ou versão web (Flask), se necessário.

💡 Ideias Futuras
Consultar uma API pública de validação de BINs

Gerar logs ou relatórios de validações

Interface amigável com seleção por bandeira