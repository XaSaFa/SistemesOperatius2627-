# Exercicis de planificació: FCFS, SJF i Round Robin
 
## Instruccions
 
En cada exercici has de planificar els processos amb **FCFS**, **SJF** (no expropiatiu) i **Round Robin**. Per a cada algorisme:
 
1. Dibuixa el diagrama de Gantt.
2. Calcula el temps de retorn i el temps d'espera de cada procés.
3. Calcula el temps mitjà de retorn i el temps mitjà d'espera.
**Fórmules:**
 
- Temps de retorn = Temps de finalització − Temps d'arribada
- Temps d'espera = Temps de retorn − Temps de CPU
**Recorda:** si a SJF hi ha empat de durada, passa primer el que ha arribat abans. A Round Robin, un procés que no acaba en el seu quàntum torna al final de la cua.
 
## Exercici 1 — La cua del laboratori
 
Tres alumnes envien alhora, a l'instant 0, una feina a l'únic ordinador del laboratori. Arriben en l'ordre P1, P2, P3.
 
| Procés | Temps d'arribada | Temps de CPU |
| --- | --- | --- |
| P1 | 0 | 6 |
| P2 | 0 | 3 |
| P3 | 0 | 1 |
 
Round Robin amb **quàntum Q = 2**.
 
**Pregunta final:** quin algorisme dona el temps mitjà d'espera més baix? Per què creus que passa?
 
## Exercici 2 — Processos que arriben en moments diferents
 
Ara els processos no arriben tots alhora. Fixa't bé: un procés només pot entrar a la CPU si ja ha arribat.
 
| Procés | Temps d'arribada | Temps de CPU |
| --- | --- | --- |
| P1 | 0 | 5 |
| P2 | 1 | 3 |
| P3 | 2 | 8 |
| P4 | 3 | 2 |
 
Round Robin amb **quàntum Q = 4**.
 
**Pista per a SJF:** quan P1 acaba, mira quins processos ja són a la cua i tria el més curt d'aquests.
 
**Pregunta final:** a Round Robin, quin procés surt més perjudicat respecte de FCFS? I quin hi surt guanyant?
