# ram-compiler
Semplice programma che simula una RAM (Random Access Machine), scritto in python.

Le istruzioni di un programma per RAM agiscono su **operandi** ed **etichette**. 
Nel modello che consideriamo ogni istruzione agisce al più su un operando o una etichetta.

Ogni operando *<op>* può avere una delle forme seguenti:
- n : <op> indica l’intero memorizzato nel registro n
- \#n : <op> indica il numero n
- (n) : <op> indica l’intero memorizzato nel registro indirizzato dal registro n (non ancora implementato)

Ogni etichetta <et> ha la forma n, ed indica il numero intero n.

## Istruzioni della RAM - tipi
- ### Istruzioni di trasferimento
  * LOAD \<op> : R\[0] := \<op>; CI := CI + 1;
  * STORE \<op> : R\[\<op>] := R\[0]; CI := CI + 1; (<op> non può essere \#n)
- ### Istruzioni aritmetiche
  * ADD \<op> : R\[0] := R\[0] + \<op>; CI := CI + 1;
  * SUB \<op> : R\[0] := R\[0] - \<op>; CI := CI + 1;
  * MULT \<op> : R\[0] := R\[0] * \<op>; CI := CI + 1;
  * DIV \<op> : R\[0] := R\[0] / \<op>; CI := CI + 1;
- ### Istruzioni di I/O
  * READ \<op> : R\[\<op>] := IN; CI := CI + 1; (\<op> non può essere #n)
  * WRITE \<op> : OUT := \<op>; CI := CI + 1;
- ### Istruzioni di salto
  * JUMP \<et> : CI := \<et>;
  * JGTZ \<et> : if (R\[0] > 0) then CI := \<et> else CI := CI + 1;
  * JZERO \<et> : if (R\[0] = 0) then CI := \<et> else CI := CI + 1;
- ### Istruzioni di controllo
  * HALT : fine del programma; il calcolo si arresta;
 
## Utilizzo
Nella cartella in cui è presente sia il file `ram_compiler.py` che il file testuale del programma per RAM, scrivere il comando:
```
python3 ram_compiler.py <file.txt>
```
