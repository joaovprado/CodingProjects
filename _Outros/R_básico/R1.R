# Comentário

################################
############ LIMPAR ############
# Ctrl + L > Limpa o console ou ícone de vassoura
# Para limpar algumas variáveis, selecionar as que eu quero e clicar no ícone de vassoura
# Para limpar todas as variáveis, só clicar no ícone de vassoura

##################################
############ EXECUTAR ############
# Ctrl + Enter > Roda a(s) linha(s) selecionadas
# Ctrl + Shift + Enter > Roda tudo

##########################################
############ ATRIBUIR VALORES ############
# Ambos sentidos são válidos:
a <- 10   # PADRÃO para criar variável
10 -> a
a = 10    # PADRÃO para atribuições de funções

############################################
############ VISUALIZAR VALORES ############
print(a)
a

################################################
############ Operadores matemáticos ############
1+2 # Soma
1-2 # Subtração
1*2 # Multiplicação
1/2 # Divisão
2**3 # Potênciação
2^3 # Potênciação

5 == 6 # Igual
5 != 6 # Diferente
5 > 6 # Maior que
5 < 6 # Menor que
5 >= 6 # Maior ou igual que
5 <= 6 # Menor ou igual que

!1 == 1 # NOT (NÃO-NEGAÇÃO)
1 == 1 & 1 != 2 # AND (E)
1 == 1 | 1 != 2 # OR (OU)

###########################################
############ HELP para funções ############
# ?c # Segundo a documentação essa função cria uma lista com os argumentos de entrada

###########################################
############ Usando a função C ############
b <- a**2 # ** ou ^ são equivalentes para potência
nome <- 'João'
nome2 <- 'Victor'

c <- c(a,b)
sobrenome <- c('Prado','de','Souza')
d <- sobrenome[1]

#################################################
############ Usando a função Summary ############
#?summary
summary(c)
e <- summary(c)
summary(sobrenome)
e[1] # Printa só a primeira estatística do resumo

#############################################
############ Usando a função str ############
#?str_c  #Não vai ter resultado se a biblioteca não tiver instalada
# Use o site https://www.rdocumentation.org, para ajudar a descobrir qual lib tem a função necessária
# No caso é o pacote stringr

#install.packages('stringr') # Para instalar
library('stringr') # Semelhante ao include do Python
#?str_c

#nome_completo <- str_c(nome, ' ', nome2, ' ', sobrenome[1], ' ', sobrenome[2], ' ', sobrenome[3])
nome_completo <- str_c(nome,nome2,sobrenome[1], sobrenome[2], sobrenome[3], sep=' ')

#############################################
############ Armazenamento numérico ############

salario <- 3450.89
horas <- 220

SH <- salario/horas
SHi <- as.integer(SH) # Pega só a parte inteira
SHr <- round(SH) # Arredondamento

list <- c(salario, horas)
list[1]

num <- as.numeric('12') # Converte string em número, coloca NA se não conseguir

################################################
############ Armazenamento de caracteres ############
nome1 <- 'João'
nome2 <- 'Victor'
idade <- 23

ls <- c(str_c(nome1,nome2, sep=" "), idade)

nome1 == nome2
nome1 < nome2

##################################################
############ Armazenamento de fatores ############

cargaHoraria <- c(220, 220, 150, 100, 100)
summary(cargaHoraria)
mode(cargaHoraria)
class(cargaHoraria)

cargaHoraria <- as.factor(cargaHoraria) # Categorização, cria uma 'tabela' de frequências 
# cargaHoraria <- as.factor(c(220, 220, 150, 100, 100))
summary(cargaHoraria)
summary(cargaHoraria)[2]
mode(cargaHoraria)
class(cargaHoraria)

##############################################
############ Armazenamento lógico ############

L1 <- salario > horas
L1

L2 <- salario < horas
L2

Logico <- TRUE # ARMAZENAMENTO DE VALOR BOOLEANO
Logico1 <- 'TRUE' # ERRADO
Logico2 <- c(1,Logico1,2) # Converte todos para texto, pq tem 1 texto
Logico3 <- c(FALSE,Logico,2) # Converte todos para numérico, no caso TRUE = 1 e FALSE = 0
Logico4 <- c(Logico3,3,4) # Converte todos para númerico e une as duas listas

#################################
############ VETORES ############
# Uma sequência com dados do mesmo tipo
a <- c(1,2,3,4,5)
is.vector(a) # Retorna se é vetor
is.list(a) # Retorna se é lista
mode(a) # Retorna tipo da variável
a[2] == a[[2]] # Ambos métodos são equivalentes para vetores!

b <- c(1,'2',3,'4',5)
is.vector(b)
is.list(b)
mode(b)


###############################
############ LISTA ############
# Um tipo de vetor especial que aceita dados de tipos diferentes

a <- list(1,2,3,4,5)
is.vector(a)
is.list(a)
mode(a)
str(a)
a[2] == a[[2]] # Ambos métodos são equivalentes para listas simples!

b <- list(1,'2',3,'4',5)
is.vector(b)
is.list(b)
mode(b)
str(b)

c <- list(a,b,c(1,2,3),list(1,'a',TRUE)) #Lista de listas
c[[4]][2] # Selecionar item em uma lista dentro de outra lista
str(c)

################################
############ MATRIZ ############
# Vetor com duas dimensões, aceita só um tipo de dado

m <- matrix(1:9, nrow = 3)
mode(m)
class(m)
m[2,3] #m[linha,coluna]
m

m2 <- matrix(1:10, nrow = 2)
m2[2,3] <- 7
m2[2,3] <- 'a' # Como adicionei um texto, a matriz toda se transforma em string
m2

matrix(NA, nrow=3, ncol=2) # Matriz vazia
matrix(TRUE, nrow=3, ncol=2) # Matriz TRUE
