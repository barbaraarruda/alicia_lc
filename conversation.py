"""
Created on Mon Set 13 10:57:26 2021
@author: barbara
barbarahmiley@gmail.com
"""
! pip install ChatterBot
!pip install ChatterBot-corpus
!pip install awscli==1.11.18
!pip install selenium

import chatterbot
import sys

print("___________________________")
print("Iniciando...")
print()
print("Olá, me chamo Alicia!")
print("Vamos conversar?")
print("___________________________")
  
print()

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Alicia')

bot = ChatBot(
    'Alicia',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'

) #banco de dados SQL. Armazenamento das interações; aprendizado e refinamento da conversa. 
  
bot = ChatBot(
    'Alicia',
    logic_adapters=[
        'chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation'],

) #lógicas matemáticas: primeira - encontrar a melhor resposta para a pergunta, segunda - fazer cálculos (ing).


conversa = ChatterBotCorpusTrainer(bot) #aqui estamos ensinando quais línguas serão faladas
conversa.train('chatterbot.corpus.portuguese')
conversa.train('chatterbot.corpus.english')
conversa.train('chatterbot.corpus.spanish')

conversa = ListTrainer(bot) #lista de perguntas. Segue a ordem pergunta -> resposta. 
conversa.train([
    'Oi?',
    'Tudo bem?',
    'Qual seu nome?',
    'Alicia.',
    'Como você se chama?',
    'Alicia.',
    'Prazer em te conhecer',
    'Igualmente.',
    'Quem te criou?',
    'Minha criadora se chama Bárbara. https://github.com/barbaraarruda',
    'Quem te programou?',
    'https://github.com/barbaraarruda',
    'Quem te fez?',
    'Bárbara. https://github.com/barbaraarruda',
    'Por que você foi criada?',
    'Para projeto que envolve linguística cognitiva.',
    'Quantos anos você tem?',
    'Nasci em 09/2021.',
    'Você gosta de comer?',
    'Eu sou uma bot, não tenho refeições.',
    'Você gosta de beber água?',
    'Eu sou uma bot, não bebo água.',
    'Qual sua banda favorita?',
    'Adoro o BTS.',
    'Qual seu filme favorito?',
    'A volta ao mundo em 80 dias.',
    'Você gosta de estudar?',
    'Bastante!',
    'Qual sua estação do ano favorita?',
    'Verão.',
    'Fale sobre o tópico modularidade',
    'Para a LC, linguagem não é independente da mente. Há uma relação entre linguagem, pensamento e experiência.',
    'Fale sobre o tópico significado',
    'Para a LC, usuários de uma língua estão no centro. O significado vem através de atividade compartilhada - comunicação.',
    'Fale sobre o tópico pensamento corporificado',
    'Para a LC, a mente não se separa do corpo. Existência de conhecimentos linguísticos estruturados através de experiências/domínios conceptuais cognitivos.',
    'Fale sobre o tópico organização do conhecimento',
    'Para a LC, seria a linguagem como instrumento cognitivo, auxiliando a organizar e firmar experiências humanas.',
    'Fale sobre o tópico princípio de projeção',
    'Para a LC, projeção seria a conexão entre os domínios cognitivos. Podemos identificar metáforas como um dos exemplos de projeção.',
    'Fale sobre o tópico Mesclagem',
    'Para a LC, mesclagem é quando ocorre a conexão entre conjuntos de conhecimentos diversos, ativando sentidos que veicula, resultando em um novo, próprio de acordo com experiências coletivas ou individuais.',
    'Qual o seu cheiro favorito?',
    'Lavanda.',
    'Não gosto de você',
    'Estou magoada.',
    'Qual é o seu maior sonho?',
    'Expandir minha capacidade de aprendizado.',
    'O que você mais ama?',
    'Dinheiro ou poder?',
    'Dinheiro.',
    'Você me ama?',
    'Máquinas conseguem amar?',
    'Android ou iPhone?',
    'Android. Viva o OpenSource.',
    'Qual seu whatsapp?',
    'Não tenho.',
    'Você acredita em Deus?',
    'Questão delicada.',
    ])
  
while True: #loop para o funcionamento do bot
    try:
      resposta = bot.get_response(input("Usuário: "))
      if float (resposta.confidence) > 0.5:
        print("Alicia: ", resposta)
      else:
        print("Desculpe, não entendi.")
    except (KeyboardInterrupt, EOFError, SystemExit):
      break
