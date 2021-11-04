from Symbols import *
pos = 0

class HashSymbols:

    def __init__(self,tam):
        self.tab = {}
        self.tam_max = tam

    def HashFunction(self, chave):
        #print(hash(chave)%self.tam_max)
        return hash(chave)%self.tam_max

    def Full(self):
        return len(self.tab) == self.tam_max

    def PrintAll(self):
        for i in self.tab:
            print("Hash[%s] = " %i, end="")
            print (self.tab[i].format())

    def Delete(self, chave):
        pos = self.LookUp(chave)
        if pos != -1:
           del self.tab[pos]
           print("Dado da posicao %d Deletedo" %pos)  
        else:
           print("Item nao encontrado")

    def LookUp(self, chave):
        pos = self.HashFunction(chave)
        if self.tab.get(pos) == None: # se esta posição não existe
               return -1 #saida imediata
        if self.tab[pos] == chave: # se o item esta na posição indicada pela função hash
            return pos
        else:
            for i in self.tab: # busca do item em toda hash (pois ele pode ter sido inserido apos colisão)
                if self.tab[i]==chave:
                    return i
        return -1

    def Insert(self, item):
          if self.Full():
               print("ATENÇÃO Tabela Hash CHEIA")
               return
          pos = self.HashFunction(item)
          if self.tab.get(pos) == None: # se posicao vazia
               self.tab[pos] = item
               print("Inserido HASH[%d]" %pos)
          else: # se posicao ocupada
               print("Ocorreu uma colisao na posicao %d" %pos)
               while True:
                    if self.tab[pos] == item: # se o item ja foi cadastrado
                        print("ATENCAO Esse item ja foi cadastrado")
                        return
                    if pos == (self.tam_max - 1):
                         pos = -1
                    pos = pos + 1 # incrementa mais uma posição
                    if self.tab.get(pos) == None:
                        self.tab[pos] = item
                        print("Inserido apos colisao HASH[%d]" %pos)
                        break                
   
tamanho = 6
tab = HashSymbols(tamanho)


Simbolo = Symbols("123","string")
Simbolo1 = Symbols("123","string")
Simbolo2 = Symbols("3.3","float")
tab.Insert(Simbolo)
tab.Insert(Simbolo1)
tab.Insert(Simbolo2)
#tab.Insert("teste")
tab.PrintAll()
#tab.Delete(Simbolo2)
print(tab.LookUp(Simbolo2))