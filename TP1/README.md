Título: TP1 - Somador on/off
Autor: Jorge Costa, A104617
Resumo:
   - Programa em Python que soma todas as sequências de dígitos que encontra num texto;
   - Sempre que encontra a string "Off" em qualquer combinação de maiúsculas, esse comportamento é desligado;
   - Sempre que encontra a string "On" em qualquer combinação de maiúsculas, esse comportamento é retomado;
   - Na soma são apenas considerados números inteiros positivos, pelo que o valor da soma é sempre positivo e crescente;
   - Sempre que encontra o carácter "=", o resultado atual da soma é colocado em stdout;
   - O programa é inicializado no modo "On", ou seja, a realizar a soma de todas as sequencias de dígitos que encontra;
   - O programa recebe o input linha a linha, via stdin, por parte do utilizador;
   - Para terminar o fio de execução do programa, utiliza-se um sinal KeyboardInterrupt (Ctrl+C);
   - Na saída da execução do programa é retornado em stdout o último valor da soma das sequências.