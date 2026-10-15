<img width="738" height="330" alt="image" src="https://github.com/user-attachments/assets/5006fce2-4f4a-44e9-aa0f-1c7cdd9b3e3b" />

## Càlcul del temps de retorn i del temps d'espera (Round Robin)

**Quantum: Q = 3**

**Fórmules:**
- Temps de retorn = Temps de finalització − Temps d'arribada
- Temps d'espera = Temps de retorn − Temps de CPU

### Càlcul per a cada procés

**P1**
- Temps de retorn: $14 - 0 = 14$
- Temps d'espera: $14 - 5 = 9$

**P2**
- Temps de retorn: $12 - 4 = 8$
- Temps d'espera: $8 - 2 = 6$

**P3**
- Temps de retorn: $21 - 1 = 20$
- Temps d'espera: $20 - 7 = 13$

**P4**
- Temps de retorn: $7 - 2 = 5$
- Temps d'espera: $5 - 1 = 4$

**P5**
- Temps de retorn: $23 - 3 = 20$
- Temps d'espera: $20 - 8 = 12$

### Temps mitjans

**Temps mitjà de retorn:**

$$
\frac{14+8+20+5+20}{5}=13,4
$$

**Temps mitjà d'espera:**

$$
\frac{9+6+13+4+12}{5}=8,8
$$
